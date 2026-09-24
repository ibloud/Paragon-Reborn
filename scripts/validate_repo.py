#!/usr/bin/env python3
"""Dependency-free repository checks."""
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "LICENSE", "CONTRIBUTING.md", "ROADMAP.md",
    "docs/ARCHITECTURE.md", "docs/AGENT-SECURITY.md",
    "docs/PARAGON_ASSET_NOTES.md", "index.html",
    "security/agent_policy.py", "tests/test_agent_policy.py",
]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = False
        self.title_text = ""
        self.errors = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "title":
            self.title = True
        if tag == "a" and values.get("target") == "_blank":
            rel = set(values.get("rel", "").split())
            if not {"noopener", "noreferrer"}.issubset(rel):
                self.errors.append("target=_blank link missing noopener noreferrer")

    def handle_endtag(self, tag):
        if tag == "title":
            self.title = False

    def handle_data(self, data):
        if self.title:
            self.title_text += data.strip()

errors = [f"missing required file: {path}" for path in REQUIRED if not (ROOT / path).is_file()]
page = PageParser()
page.feed((ROOT / "index.html").read_text(encoding="utf-8"))
errors.extend(page.errors)
if not page.title_text:
    errors.append("index.html has no non-empty title")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
if "Project status: concept and pre-production" not in readme:
    errors.append("README must state project status")

if not errors:
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        errors.append("security/rules tests failed:\n" + result.stdout + result.stderr)

if errors:
    print("\n".join(f"ERROR: {error}" for error in errors))
    sys.exit(1)
print("Repository validation passed.")

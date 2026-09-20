#!/usr/bin/env python3
"""Validate the Phase 1 rules contract and deterministic first-slice fixture."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
schema_path = ROOT / "docs/rules/schemas/rules-contract-v1.json"
fixture_path = ROOT / "docs/rules/fixtures/first-slice-v1.json"

errors = []

try:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    fixture = json.loads(fixture_path.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    print(f"ERROR: unable to load rules contract: {exc}")
    sys.exit(1)

if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
    errors.append("rules schema must declare JSON Schema draft 2020-12")

if fixture.get("version") != 1:
    errors.append("fixture version must be 1")

hero = fixture.get("hero", {})
ability = fixture.get("ability", {})
card = fixture.get("card", {})
scenario = fixture.get("fixture", {})
expected = scenario.get("expected", {})

required = [
    ("hero.id", hero.get("id")),
    ("ability.id", ability.get("id")),
    ("card.id", card.get("id")),
]
for name, value in required:
    if not value:
        errors.append(f"missing required fixture field: {name}")

damage_bonus = card.get("effect", {}).get("damage_bonus", 0)
expected_damage = ability.get("base_damage", 0) + damage_bonus
if expected.get("damage_per_successful_cast") != expected_damage:
    errors.append("expected damage does not equal base damage plus card modifier")

casts = scenario.get("cast_at_seconds", [])
cooldown = ability.get("cooldown_seconds", 0)
successful = 0
last_successful_cast = None
for t in casts:
    if last_successful_cast is None or t >= last_successful_cast + cooldown:
        successful += 1
        last_successful_cast = t

expected_resource = hero.get("starting_resource", 0) - successful * ability.get("resource_cost", 0)
if expected.get("resource_after_casts") != expected_resource:
    errors.append("expected resource does not match successful casts and resource cost")

if expected.get("cooldown_after_successful_cast") != cooldown:
    errors.append("expected cooldown does not match ability cooldown")

if successful != 2:
    errors.append(f"fixture should demonstrate exactly 2 successful casts; found {successful}")

if errors:
    print("\n".join(f"ERROR: {error}" for error in errors))
    sys.exit(1)

print("Rules contract validation passed.")
print(f"Successful casts: {successful}")
print(f"Damage per successful cast: {expected_damage}")
print(f"Resource remaining: {expected_resource}")

# Microsoft workspace integration

## Purpose

This repository remains the source of truth for project code, architecture contracts, public documentation, and versioned IP-development artifacts. The Microsoft workspace is the companion document/evidence layer.

## Pilot workspace

The Paragon-Reborn workspace is organized as:

- `00_PROJECT-ADMIN/` — project administration and coordination
- `01_RESEARCH/` — research corpus and working analysis
- `02_PRIMARY-SOURCES/` — source PDFs, scans, and reference material
- `03_RIGHTS-AND-PROVENANCE/` — rights, provenance, permissions, and evidence records
- `04_IP-DEVELOPMENT/` — working IP-development material that is not yet canonical GitHub content
- `05_REVIEW/` — review packages and feedback material
- `06_RELEASE/` — release and handoff material
- `99_ARCHIVE/` — superseded material

## Boundary rules

1. GitHub is authoritative for code, schemas, tests, architecture contracts, roadmap state, and published project documentation.
2. Microsoft is authoritative for working documents, source material, correspondence, review packets, and administrative records where those records are not appropriate for public source control.
3. Do not copy restricted or proprietary assets into the public repository.
4. A research conclusion becomes canonical project knowledge only when it is deliberately promoted into version-controlled documentation or structured data.
5. The browser prototype and future Unreal implementation continue to share behavior through versioned fixtures rather than by sharing implementation-specific files.

## Current pilot status

The document workspace has been provisioned in the connected OneDrive as `Paragon-Reborn/`. No existing files were moved or overwritten during provisioning.

## Next integrations

- Add review/approval conventions for architecture decisions.
- Establish a repeatable intake path from research documents into GitHub issues or pull requests.
- Add Azure deployment configuration only after the public-site deployment target is selected and credentials/secrets are available.
- Extend the same boundary model to `narrative-provenance` and the Pixie repository family after the Paragon pilot is reviewed.

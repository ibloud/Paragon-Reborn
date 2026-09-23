# Architecture Decision: Microsoft companion workspace

**Status:** Proposed for pilot
**Scope:** Paragon-Reborn

## Decision

Use GitHub as the canonical source-control and project-architecture system, with the connected Microsoft document workspace serving as the research, source-material, review, rights, and administrative layer.

The pilot workspace is provisioned under `Paragon-Reborn/` with numbered lifecycle folders so material can move from source/evidence through development, review, release, and archive without conflating working documents with canonical source.

## Why

Paragon-Reborn already contains explicit repository boundaries, a roadmap, architecture contracts, and automated validation. Moving those canonical artifacts into a document platform would weaken the existing version-control boundary. Conversely, putting primary-source PDFs, correspondence, review packets, and rights records into a public code repository would mix evidence/admin material with published project content.

## Consequences

- GitHub remains the public/canonical project record.
- Microsoft becomes the private working-document and evidence corpus.
- Promotion from Microsoft to GitHub is intentional and reviewable.
- No bulk migration of the other repositories occurs as part of this pilot.
- Azure deployment remains a later implementation step; this decision does not create cloud resources or credentials.

## Pilot acceptance checks

- Workspace exists with the documented folder structure.
- Existing Paragon-Reborn GitHub content remains unchanged on `main`.
- Integration documentation is reviewable through a pull request.
- No restricted assets are copied into the public repository.

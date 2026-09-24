# Paragon Asset Integration Contract

**Status:** ACTIVE PRODUCTION / COMPLIANCE GATE  
**Scope:** Paragon-Reborn project, Epic Games Paragon-derived Fab assets, and any future Unreal Engine 5 vertical-slice integration  
**Authority:** Project compliance/production contract. This document does not define game mechanics, gameplay authority, or project IP ownership.  
**Last verified:** 2026-09-24

## 1. Purpose

This contract establishes the minimum provenance, licensing, branding, repository, and release controls for using Epic Games' Paragon-derived assets in this project.

It exists to keep the visual-production layer separate from:
- original project rules and gameplay systems;
- original project IP;
- research and design references;
- third-party licensed material;
- source-controlled project code and documentation.

The contract is a production gate, not legal advice. Where a question is not answered here or by the applicable asset license, stop and obtain a human/legal determination rather than infer permission.

## 2. Current verified license baseline

The current Fab Standard License states that a licensee may:
- use Fab assets commercially or privately;
- modify and adjust assets to incorporate them into Projects;
- commercially distribute Projects with Fab assets incorporated;
- use assets with compatible tools; the current standard license is not categorically limited to Unreal Engine;
- share assets with collaborators working on the Project.

The current Fab Standard License also prohibits reselling or redistributing an asset on a standalone basis.

**Important:** The general Fab Standard License is not a substitute for checking the individual listing. An asset's listing, license tier, format, or other applicable terms may impose additional constraints.

## 3. Paragon-specific listing controls

Current Paragon Fab listings reviewed for this contract (including Paragon: Terra and Paragon: Greystone) state:
- the released material is supplied for use in Unreal Engine projects;
- Included formats: Unreal Engine;
- the trademark **PARAGON** may not be used to advertise or name the game.

Therefore, this project adopts the following mandatory production controls:

### 3.1 Public game identity

The shipped/public-facing game title, advertising, store presentation, promotional copy, and product identity must not use the **PARAGON** trademark as the game name or advertising identity.

The repository/project may retain historical or research identifiers where needed for provenance, documentation, or asset identification. That does not authorize use of PARAGON as the shipped game identity.

### 3.2 Standalone asset distribution

Do not commit, package, publish, sell, or otherwise redistribute Epic/Fab Paragon assets as standalone downloadable assets.

Do not create a repository, sample pack, marketplace listing, or downloadable bundle whose purpose is to redistribute the third-party assets independently of the Project.

### 3.3 Project incorporation

Paragon-derived assets may be used only as incorporated project content under the applicable asset terms.

Keep third-party source assets outside public source control unless the applicable license explicitly permits that distribution.

### 3.4 Provenance

Every imported Paragon-derived asset must have an auditable provenance record containing, at minimum:
- asset/listing name;
- Fab listing URL;
- acquisition/source date;
- applicable license or terms reference;
- intended Project use;
- whether the asset is modified;
- repository/storage location;
- release disposition.

### 3.5 Names, lore, and presentation

Do not treat Epic's Paragon character names, lore, branding, factions, or presentation as original project IP.

Where a source asset is visually adapted into an original project character, faction, world, or mechanic, the project must separately document the original design layer.

Do not imply Epic endorsement, sponsorship, affiliation, or ownership of the resulting project unless separately authorized.

## 4. Unreal production path

The current Paragon listings reviewed for this contract identify Unreal Engine as the included format and describe the assets for Unreal Engine projects.

Accordingly, **Unreal Engine 5 is the target production path for the Paragon-derived vertical slice.**

This is a production decision based on the current asset delivery/format and project architecture. It is not a claim that the current general Fab Standard License prohibits compatible non-Unreal tools.

Before importing a new asset family:
1. verify the current Fab listing;
2. verify the included format;
3. verify the applicable license/terms;
4. record provenance;
5. test import and packaging in the target UE5 version;
6. record any compatibility exception.

## 5. Repository boundary

Paragon-derived binary/source assets must not be added to this public repository unless the applicable license has been explicitly verified to permit that exact distribution.

The repository should contain:
- contracts;
- provenance records;
- import manifests;
- compatibility notes;
- original project code;
- original project design;
- tests and validation;
- links to official asset sources.

The repository should not become a redistribution channel for Epic's asset files.

## 6. Release gate

A release containing Paragon-derived assets is blocked until all applicable checks below pass:

- [ ] Asset provenance recorded.
- [ ] Current Fab listing/license reviewed.
- [ ] Included format verified.
- [ ] No standalone asset redistribution.
- [ ] Public game identity does not use PARAGON as the game name/advertising identity.
- [ ] No unverified Epic endorsement/affiliation claim.
- [ ] Third-party assets are not accidentally committed to public source control.
- [ ] UE5 import/package test completed for the target build.
- [ ] Modified/original project material is distinguishable from third-party material.
- [ ] Any unresolved legal question is escalated instead of guessed.

## 7. What this contract does not establish

This contract does **not** establish:
- ownership of Epic Games' assets;
- ownership of third-party face scans or other embedded third-party material;
- a blanket prohibition on all non-Unreal tooling under the Fab Standard License;
- permission to use any particular asset without checking its current listing;
- permission to reproduce, recreate, or emulate an Epic game;
- permission to use Paragon character names, lore, trademarks, or other Epic IP;
- any claim about Epic endorsement or affiliation;
- any specific gameplay or mechanics rule.

Those questions require the applicable current terms and, where necessary, human/legal review.

## 8. Source record

Primary sources reviewed for this contract on 2026-09-24:

- Fab Standard License: https://www.fab.com/eula
- Paragon: Terra listing: https://www.fab.com/listings/5ea6bcb6-e43e-4bbe-813f-c19d8c907565
- Paragon: Greystone listing: https://www.fab.com/listings/122fd7bf-6f12-4304-a930-cccbbacdaebc

The contract should be re-reviewed whenever:
- the Fab EULA changes;
- a Paragon asset listing changes;
- a new Paragon-derived asset family is introduced;
- the target engine/version changes materially;
- the project approaches public release or distribution.

## 9. Implementation relationship

This contract sits below the project's architecture and above asset import/release procedures.

It does not alter:
- the game's constitutional rules;
- the shared mechanics layer;
- Veiled Dominion canon;
- Money Game architecture;
- the project's original gameplay systems.

It governs only the third-party asset integration boundary.

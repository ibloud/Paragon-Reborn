# Original hero cards and consequential stories

Date: 2026-10-08  
Status: owner-approved design direction; mechanics proposed, not implemented or balanced.  
Scope: original successor experiment coordinated here; not a Paragon sequel or a change to Veiled Dominion canon.  
Tracking: [design issue #16](https://github.com/ibloud/Paragon-Reborn/issues/16).

## Purpose and authority

Build an original game in which a hero's central tension, combat choices, and story consequences reinforce each other. Acknowledge historical influence through documented research and appropriately reviewed attribution; develop independent characters, setting, visual language, audio, writing, and rules expression. Changing an existing character's name alone is not the transition.

This direction supersedes the historical tarot roster as the source for NEW production content. It does not rewrite that archive, import it into runtime, or change the existing v1 shared rules fixture. Return to the Void remains a working title, not a cleared trademark. The repository identifier remains for continuity and is not the proposed product branding.

The research lesson from Paragon is the value of preparing a build and making meaningful in-match choices. Epic's executive producer identified clarity, ease of use, and impact as redesign goals in [2017](https://blog.playstation.com/2017/02/03/paragon-whats-next-in-2017/). We adopt those goals, not an obligation to reproduce an earlier implementation.

## Three distinct layers

| Layer | Responsibility | Limit |
| --- | --- | --- |
| Hero archetype / Major Arcana | Central tension, signature play pattern, character choices | No inherited Epic character identity or numeric power ranking |
| Build / Minor Arcana | Tactical modifiers selected by the player | Costs, cooldowns, stacking and counters are explicit; no numerological balance claims |
| Story spread | Situation, pressure and turning-point opportunities | Does not decide the player's action or ending; no hidden competitive stat changes |

Upright/reversed are optional presentation terms for contrasting approaches, not good/evil labels or automatic buffs/debuffs. Every path must have a viable purpose and a cost. Plain-language labels must accompany them. Tarot symbolism is a creative vocabulary, not a claim about a player's personality or destiny.

| Suit | Proposed tactical identity | Cost or counter to evaluate |
| --- | --- | --- |
| Swords | Precision, information, interruption | Timing, exposure, limited control duration |
| Staves | Movement, initiative, burst | Commitment, recovery, resource use |
| Cups | Protection, links, shared support | Range, positioning, divided resources |
| Coins | Preparation, equipment, reserves | Setup delay, slower immediate payoff |

Numbers indicate theme or progression, not damage or mandatory power. Use stable card IDs independent of displayed numbers. Preserve Justice VIII / Strength XI as the initial presentation convention and record it explicitly. Playing-card/cardology mappings are deferred adapters: they require explicit treatment of the extra tarot courts and Major Arcana, not a claim of automatic equivalence.

## Original character incubation

These are generic working briefs, not cleared names, approved canon, final art directions, or renamed legacy heroes. Design from independent motivations and social relationships before choosing silhouettes, powers and voices. No one-to-one replacement roster is required.

| Temporary ID / archetype | Independent premise | Play hypothesis | Story question |
| --- | --- | --- | --- |
| hero_01 / Temperance | A civic heat steward allocates a settlement's finite warmth between infrastructure and emergency teams | Release reserves for immediate pressure or retain them for stable protection; no free conversion loop | Who gets help first when needs conflict? |
| hero_02 / Hanged Man | A route surveyor must surrender a trusted map when a changing landscape makes it dangerous | Commit to a vulnerable survey action to reveal a route; opponents can interrupt it | Can expertise remain useful when certainty is relinquished? |
| hero_03 / Star | A seed archivist reconnects separated communities after a failed harvest | Place a visible, destructible recovery site that requires allies to stay nearby | What makes a promise of recovery credible? |

Develop new origin, relationships, silhouette, equipment, voice and ability expression for each. Do not transfer signature weapons, costumes, animations, biographies, factions or dialogue from the historical roster. These briefs are original proposals for review, not a legal determination of clearance.

## Lessons from the historical assignment review

The old Khaimera/Temperance and Gideon/Hanged Man pairings showed why an archetype can be a challenge to overcome rather than a trait already mastered. Riktor/Justice raised the distinction between punishment and fairness. Morigesh/Cups and Wraith/Cups exposed cases where a reversed interpretation was being presented as an upright fit. Keep those names in historical critique only.

In new content, show how a choice expresses a tension. Do not equate age with emotional maturity, possession with prosperity, opposition with partnership, or power with justice. Imagined scenes in the old Minor Arcana research are adaptations, not verified game lore. Neither their preservation nor a project license clears their commercial use.

## Build and balance proposal

After the existing one-hero slice, test three original heroes, twelve build cards (three per suit), two approaches per hero, and one branching solo/cooperative mission. Three equipped build slots is an initial hypothesis. All gameplay cards are equally available during tests; progression may unlock original art or stories, not competitive power.

Each card specification must identify eligibility, trigger, exact effect, cost, cooldown, duration, stacking rule, maximum applications, cancellation/refund behavior and opponent response. Budget burst, sustained damage, control, healing, mobility and information separately. A shared point total alone does not prove comparable value.

Allow multiple builds per hero and situational adjustment at defined safe checkpoints. Avoid locking essential counters or information tools behind rare cards or a single suit. Prevent recursive resource/heal triggers and unbounded stacking. Bots and human players use the same rules and legal information; narrative tags grant neither hidden bot knowledge nor mechanical advantages.

Measure matchup outcomes by skill and mode, time-to-defeat, control uptime, resource loops, build selection and abandonment. For cooperative play also measure completion, failure causes and role usefulness. Bot simulations detect exploits; human tests assess clarity, agency and enjoyment. Do not claim balance from a small aggregate win rate or symbolic symmetry.

## Story selection and state

Start with authored, original encounters. A spread selects a situation, pressure and turning-point opportunity. Filter candidates by present characters, location, prior choices, prerequisites, exclusions and content preferences. Use versioned content plus a recorded seed, stable candidate ordering and a documented random algorithm. Persist actual selected IDs and choice events; a seed alone is insufficient across versions.

Required future data: contentVersion, rulesVersion, seed, selectedEncounterIds, partyIds, locationId, relationshipFlags, choiceEvents, resolvedConsequences, seenEncounterIds and provenanceRefs. Separate combat events from narrative state. Do not infer sensitive personal traits from play.

When no encounter is eligible, use an authored neutral fallback. Avoid recent repeats. Apply consequences atomically and once per choice-event ID; reject choices not offered in the current state. State must survive save/resume without changing outcomes. Keep irreversible consequences visible before confirmation where appropriate.

Example original mission: a reservoir failure threatens an isolated settlement. Five of Coins supplies scarcity, Tower disruption and Star a recovery opportunity. The player chooses evacuation, repair or negotiation; each changes the next available objective and an ending condition. No option is declared morally correct by the card draw. This is a proposed scenario, not a playable mission.

Competitive modes may vary approved narration but keep combat rules fixed and disclosed. Cooperative modifiers must be selected within tested difficulty bounds. If generative dialogue is later introduced, use only approved original inputs; it cannot author mechanics, rewards, canon or authoritative state. Provide an authored fallback and record generated text separately from canon.

## Acceptance scenarios for the future prototype

| Case | Required result |
| --- | --- |
| Same versions, initial state, seed and choices | Identical encounter selection and consequences |
| Missing party member or contradictory flag | Ineligible scene never selected |
| No eligible scene | Safe authored fallback; no soft lock |
| Replayed choice event | Consequence applied exactly once |
| Save/resume | Same pending choices and state as uninterrupted run |
| Different meaningful choice | At least one later objective or ending condition changes |
| Swapped story spread in competitive mode | No change to damage, costs, cooldowns or rewards |
| Build combination stress test | No unbounded resource loop or permanent control lock |
| Narrative presentation disabled | Full rules and choice consequences remain understandable |

Use large touch targets, text suit labels, screen-reader order, readable contrast and optional reduced motion. Never rely on color or upside-down text to convey a path. Offer pause/reading time in solo play, transcript access and optional narration; test on iPad. These are acceptance requirements, not implemented accessibility claims.

## Staged delivery and ownership

1. This increment: design, rights boundary, historical labels, and receiving contract.
2. Preserve the existing v1 fixture. Design a separate v2 proposal only when its exact effects are specified; include migration and replay fixtures.
3. Deliver one original hero, one modifier and one authored choice in an isolated prototype; demonstrate rules and consequence replay.
4. Expand to the three-hero/twelve-card study only after that slice passes.
5. Consider Unreal integration, networking and wider production after evidence and rights review.

The receiving boundary is [Veiled Dominion's experiment contract](https://github.com/Loptr-Lab/veiled-dominion-engine/blob/feature/original-tarot-direction/docs/contracts/original-tarot-experiment.md) (companion review branch). Its canonical four-player rulebook, PIXIE identity, and coding exercise remain separate. Duet, artist-specific projects and unrelated bots receive no new mechanics through this decision. A Codex presentation adapter may later index approved status and provenance, but does not define rules.

See [original-content and rights boundary](ORIGINAL_CONTENT_RIGHTS.md). No playable system, new license grant, complete IP migration, or legal clearance is asserted by this document.

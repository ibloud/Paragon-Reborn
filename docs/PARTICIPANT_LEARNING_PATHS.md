# Participant Learning Paths

Return to the Void is intended to be a skill ladder, not a credential gate. A contributor should be able to begin with writing, research, wireframing, audio editing, testing, or another accessible discipline and move toward systems, programming, Unreal, or technical art as their skills grow.

## The learning sequence

**Read → document → diagram → prototype → test → implement → integrate**

External courses are useful when they teach a transferable skill. They are not prerequisites for joining the project, and a certificate is not a substitute for a working exercise.

## Start where your existing skills are

| Starting point | First project skill | Next step | Longer-term path |
|---|---|---|---|
| Writer / researcher | Technical documentation | Markdown, diagrams, requirements | Systems / UX / QA |
| Visual thinker | Wireframes and flows | Figma or equivalent | UX/UI / level design / technical art |
| Game enthusiast | Game-design methods | Rules, prototypes, playtesting | Systems design |
| Beginning programmer | Programming + Git | Small deterministic systems | Prototype Engineer |
| Artist / animator | Presentation contracts | Unreal fundamentals | Technical Artist |
| Musician / sound hobbyist | Audacity + audio editing | Dynamic game audio | Audio / Audio Aura |
| Existing developer | Testing + architecture | Unreal / networking | Prototype Engineer |
| Existing technical artist | Materials / VFX / state contracts | Unreal integration | Technical Artist |

## Common Core

### 1. Technical writing

**Recommended starting resource:** [Google Technical Writing](https://developers.google.com/tech-writing)

Google's Technical Writing courses cover audience, scope, clear prose, structure, task-based documentation, illustrations, code samples, tutorials, and self-editing.

**Paragon exercise:** write one page explaining one project concept, such as:

- Audio Aura
- Veil state
- authoritative game state
- card modifier
- ability event flow
- Technical Artist presentation contract

A second-pass exercise should turn the page into reusable project documentation with explicit inputs, outputs, assumptions, and acceptance criteria.

### 2. Wireframing and UX

Good introductory options include:

- [Coursera — Build Wireframes and Low-Fidelity Prototypes](https://www.coursera.org/learn/wireframes-low-fidelity-prototypes)
- [Coursera — UX Design: From Concept to Prototype](https://www.coursera.org/learn/ux-design-concept-prototype)
- [edX UX Design courses](https://www.edx.org/learn/ux-design)

**Paragon exercise:** wireframe a player-facing flow such as hero selection, card selection, Audio Aura settings, accessibility settings, or a match result screen. Include keyboard/controller navigation and reduced-motion considerations.

### 3. Game and systems design

**Strong conceptual starting point:** [MIT OpenCourseWare — Introduction to Game Design Methods](https://ocw.mit.edu/courses/cms-301-introduction-to-game-design-methods-spring-2016/)

It emphasizes game-design methods, rapid prototyping, playtesting, and player-centered design.

For a structured Unreal-centered route, see the [Epic Games Game Design Professional Certificate](https://www.coursera.org/professional-certificates/epic-games-game-design-professional-certificate).

**Paragon exercise:** specify one small mechanic as:

1. player intent;
2. game event;
3. authoritative state change;
4. resolved outcome;
5. presentation/audio response;
6. automated rule tests.

Do not put gameplay authority inside animation, audio, or rendering.

### 4. Programming and prototype engineering

A beginner can use [Unity Learn](https://learn.unity.com/learn/) for programming, version control, debugging, scripting, and game-project fundamentals even if the eventual production engine is Unreal.

When ready for Unreal, use Epic's [Unreal Engine for New Users](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-for-new-users) and [Understanding the Basics](https://dev.epicgames.com/documentation/en-us/unreal-engine/understanding-the-basics-of-unreal-engine).

The goal is not to memorize an engine API. The goal is to learn deterministic state, tests, version control, interfaces, debugging, and integration.

**Paragon exercise:** implement a tiny authoritative rules system with explicit state and automated tests before connecting it to presentation.

### 5. Technical Art

Technical Art is a specialization rather than the first gate.

Recommended progression:

**visual fundamentals → game presentation → Unreal fundamentals → materials/VFX → state-driven presentation → Paragon asset adaptation**

Epic's Unreal documentation covers materials, textures, VFX/Niagara, lighting, post-processing, content import, and related rendering systems.

**Paragon exercise:** receive an authoritative state such as Veiled, Sheltered, Frozen, or an Aura intensity and express it visually without allowing the material, animation, shader, or renderer to determine the state.

> Artists own expression of state, not determination of state.

A technically correct implementation must remain independent of render frame rate and must not feed presentation state back into the rules engine.

### 6. Audio and Audio Aura

**No expensive DAW is required.**

[Audacity](https://www.audacityteam.org/) is an appropriate officially supported entry tool for recording and editing project audio. It is free, open source, and cross-platform.

Suggested audio progression:

**Level 1 — Sound editor**
- trim, split, fade, normalize;
- basic EQ/compression;
- noise cleanup;
- looping;
- WAV export;
- consistent naming and metadata.

**Level 2 — Sound designer**
- layering;
- ambience;
- transitions;
- dynamic intensity;
- state-specific cues;
- accessibility-aware mixes.

**Level 3 — Interactive audio**
- GAME EVENT → AUDIO STATE;
- intensity and duration controlled by authoritative state;
- audio and visual presentation both remain downstream of gameplay state.

**Level 4 — Professional specialization**
- Reaper, Logic, Ableton, Pro Tools, FMOD, Wwise, or equivalent may be used where useful.
- These are optional specialization tools, not entry requirements.

**Paragon exercise:** create a three-state Audio Aura set:

~~~
EVENT
  ↓
AURA INTENSITY = 0.7
  ↓
choose/create sound
  ↓
edit in Audacity
  ↓
export WAV
  ↓
document:
  trigger
  duration
  intensity
  loop behavior
  accessibility behavior
~~~

For 2D presentation, audio can drive sprite, canvas, CSS, or animation-state changes. Real-time 3D shader work is not required merely to make the system audio-reactive.

## Audio Aura as a core design system

Audio Aura is not merely an accessibility tutorial.

The intended architecture is:

~~~
PLAYER ACTION
     ↓
GAME EVENT
     ↓
AUTHORITATIVE STATE
     ├──────────────→ RULES / MOVEMENT
     ├──────────────→ AUDIO STATE
     │                    ↓
     │               AUDIO CUE
     └──────────────→ VISUAL STATE
                          ↓
                    VISUAL CUE
~~~

The same underlying state can therefore be communicated through sight, sound, animation, text, or combinations of those channels without making any one presentation channel the authority.

## Turning courses into project work

Every course should end with a project-sized exercise.

| Learning resource | Project-sized outcome |
|---|---|
| Google Technical Writing | AUDIO_AURA.md or another implementation contract |
| UX / Figma | accessible player-flow wireframe |
| MIT Game Design Methods | one mechanic specification + paper prototype |
| Unity Learn / programming fundamentals | deterministic rules exercise + tests |
| Unreal for New Users | small presentation prototype |
| Unreal materials/VFX | state-driven visual effect |
| Audacity | three-state Aura sound set |
| Interactive audio study | event → audio-state implementation plan |

## Hardware is a routing decision, not a status judgment

Not every contributor needs a high-end Unreal workstation.

- **Tier 1 — Documentation / Rules / Web:** browser, Git, editor, modern CPU, and ordinary development hardware.
- **Tier 2 — UX / 2D / Audio / Technical Art preparation:** stronger CPU/RAM and, where appropriate, a dedicated GPU; Audacity itself does not require an expensive workstation.
- **Tier 3 — Unreal / Paragon asset work:** use the current Epic Unreal Engine hardware/software requirements for the selected engine version.

If a participant cannot run Tier 3, route them to documentation, rules, UX, audio, testing, web prototypes, or other work that produces useful project artifacts.

## Recommended order for a new participant

1. Read README.md, CONTRIBUTING.md, and docs/ARCHITECTURE.md.
2. Choose one accessible starting discipline.
3. Complete one small external learning module.
4. Recreate the concept as a Paragon-Reborn-sized exercise.
5. Document what was learned.
6. Move one level deeper only when the previous level is comfortable.
7. Submit evidence, not credentials.

The project should make it possible for someone to enter through writing or wireframing and eventually reach systems engineering or technical art without pretending that everyone starts at the same skill level.

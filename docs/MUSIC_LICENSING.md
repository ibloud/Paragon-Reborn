# Independent Music Licensing for Return to the Void

This document describes a practical intake model for independent artists who may want their music in Return to the Void or related prototypes.

**This is project guidance, not legal advice.** Music rights vary by territory, contract, publisher, label, co-writer, performer, and recording. When a commercial release is contemplated, the project should obtain qualified legal review of the actual agreement.

## The first rule: Bandcamp is not a license

An artist having a Bandcamp page does not by itself tell us that the artist can license a recording to a game.

Bandcamp's current Terms of Use require artists to represent that they own or control the rights in music they upload, while also recognizing that some performance and mechanical rights may be administered by PROs, MROs, CMOs, publishers, or other entities. Bandcamp also asks artists to identify songwriter affiliations. See the Bandcamp Terms of Use and its 2026 publishing-rights update.

Therefore the project should treat a Bandcamp page as **discovery and contact information**, not as proof of licensing authority.

## Two rights questions must be answered

A recorded song commonly involves at least two distinct copyrighted works:

1. **Musical work / composition** — music and lyrics.
2. **Sound recording / master** — the particular recorded performance.

The U.S. Copyright Office explains that these are separate works and may have different owners. See What Musicians Should Know about Copyright and Musical Compositions, Sound Recordings & Copyright.

For a game using the artist's existing recording, the project generally needs the rights to use **both** the composition and the specific master, unless the proposed use is structured differently and the necessary rights are otherwise cleared.

## What an independent artist should know before saying "yes"

An artist should be able to answer:

### Ownership

- Who owns the master recording?
- Who owns the composition?
- Are there co-writers?
- Is there a publisher or publishing administrator?
- Is the artist signed to a label?
- Are there producer agreements, sample licenses, or other third-party claims?
- Did a distributor, label, publisher, or another agreement already grant exclusive rights that would conflict with the proposed game license?

### Authority

The person signing must actually have authority to grant the rights promised.

A band member saying "this is our song" is not enough if a label, publisher, co-writer, producer, or other rights holder owns or controls a relevant right.

### Collecting societies and administrators

Ask whether the composition is registered with a PRO, MRO, CMO, publisher, or other rights administrator, and identify the relevant organization.

The project should not assume that a direct payment to the performer resolves every royalty or administration obligation.

## What the game license should expressly cover

For a game, do not rely on a vague statement such as "you can use my song."

The written license should identify, at minimum:

### 1. The track

- artist name;
- track title;
- version/remix;
- ISRC if available;
- album/release;
- exact master being licensed.

### 2. The composition

- songwriters/composers;
- publisher/publishing administrator if any;
- ISWC if available;
- ownership or control percentages where relevant.

Bandcamp added publishing-rights fields for songwriter/composer names, publisher information, and ISWC in 2026, which can make the artist's Bandcamp metadata a useful starting point for rights research. It is still not a substitute for a signed rights confirmation.

### 3. Game use

The agreement should expressly state whether the track may be:

- synchronized with gameplay;
- played in menus, lobbies, matches, trailers, or other game content;
- used in downloadable content;
- used in demos and prototypes;
- used in promotional gameplay videos and trailers;
- streamed or transmitted as part of the game;
- cached or downloaded to the player's device;
- used offline;
- bundled with or delivered as part of the game;
- used on PC, console, mobile, web, or other specified platforms.

### 4. Rhythm-game / charting rights

If the project ever uses the track as a rhythm-game or beat-matching track, say so explicitly.

The license should address the creation and use of:

- beat maps;
- note charts;
- timing data;
- difficulty levels;
- stems or separated tracks if supplied;
- edited or shortened versions;
- loops or gameplay-specific edits;
- metadata;
- preview clips.

This is especially important because the project is not merely playing music in the background: a rhythm-game-style system can create additional game-specific data derived from the musical performance.

### 5. Promotional use

The project should separately identify whether the artist permits:

- trailers;
- screenshots containing the song;
- livestreams;
- social clips;
- website embeds;
- store-page videos;
- press materials;
- convention/demo presentations.

### 6. Territory and term

Specify:

- territory: e.g. worldwide or named territories;
- term: fixed period or continuing;
- whether the license survives game updates, archival builds, or previously downloaded copies.

### 7. Exclusivity

State whether the license is:

- non-exclusive;
- exclusive for a particular game/category/platform/period.

For an independent project, a **non-exclusive** license is generally the simplest starting structure, but the actual agreement should reflect what the artist and project negotiate.

### 8. Money

The agreement should state:

- upfront fee, if any;
- royalties, if any;
- revenue share, if any;
- payment timing;
- reporting requirements;
- whether promotional/demo use is included;
- whether additional uses require a new fee.

Do not promise an artist that "Bandcamp royalties" or streaming royalties automatically cover game use. Game synchronization and master-use rights are a separate licensing question.

### 9. Credit

Specify the requested credit:

- artist;
- track;
- writers;
- label/publisher where required;
- website/social link if agreed.

### 10. Takedown / termination

The contract should say what happens if:

- the license expires;
- the artist terminates under the agreement;
- a third-party rights problem appears;
- the game is discontinued;
- the track is removed from future downloads.

It should also distinguish future distribution from copies already legitimately distributed if the parties agree to do so.

## A practical rights packet for each track

Before integration, create a small rights record:

~~~
TRACK
  artist:
  title:
  version:
  ISRC:

MASTER
  owner:
  licensing contact:
  authority confirmed: yes/no

COMPOSITION
  writers:
  publisher/admin:
  PRO/MRO/CMO:
  ISWC:
  ownership/control confirmed: yes/no

GAME LICENSE
  sync:
  master use:
  gameplay:
  rhythm/chart use:
  edits/loops/stems:
  trailers/promotional:
  platforms:
  territory:
  term:
  exclusivity:
  fee/royalty:
  credit:
  termination:

EVIDENCE
  signed agreement:
  rights confirmations:
  provenance:
  final approved audio:
~~~

No track should enter a production build until the rights record is complete enough for the intended use.

## A simple independent-artist intake flow

~~~
DISCOVERY
   ↓
ARTIST CONTACT
   ↓
WHO OWNS THE MASTER?
WHO OWNS THE COMPOSITION?
   ↓
RIGHTS / ADMINISTRATION CHECK
   ↓
AGREE ON GAME USE
   ↓
WRITTEN LICENSE
   ↓
RIGHTS RECORD
   ↓
AUDIO + METADATA INTEGRATION
   ↓
CREDIT / REPORTING
~~~

This makes licensing an engineering intake process rather than a last-minute legal cleanup.

## What the Tap Tap Revenge model teaches us

Historical reporting on Tap Tap Revenge shows why this distinction matters. Tapulous released artist-specific and licensed music content, including a Nine Inch Nails edition and later downloadable music packs. Contemporary reporting also documents licensed independent music entering Tap Tap Tour through MuseIQ's independent-artist catalog.

The important project lesson is not to copy any historical contract. It is that a music game can be designed around a **catalog-and-content pipeline** in which individual tracks are cleared, packaged, delivered, credited, and updated.

That model is compatible with an independent-artist program for Return to the Void.

## What Clone Hero teaches us

Clone Hero demonstrates a different technical model: songs are treated as content packages containing an audio file, chart data, and metadata such as artist and song title. Its documentation describes a minimum package containing notes.chart or notes.mid, an audio file, and song.ini.

For Return to the Void, that suggests a useful internal separation:

~~~
LICENSED MUSIC
   ├── MASTER AUDIO
   ├── COMPOSITION METADATA
   ├── CHART / BEAT DATA
   ├── GAMEPLAY METADATA
   └── RIGHTS RECORD
~~~

The license should cover the actual package the project intends to distribute, not merely permission to "play the song."



## Digital interactive use: rhythm game vs. standalone adventure

For **50 Ways to Leave Another**, the licensing model should distinguish between simply including a song in a game and making the song an interactive game object.

The U.S. Copyright Office specifically identifies video games as audiovisual works for which incorporating music requires the relevant synchronization and master-use permissions; there is no general compulsory sync/master license for this use. citeturn0search35

### A. Standalone adventure / soundtrack use

If a licensed recording is simply part of the soundtrack of a standalone adventure, the rights package should cover:

- synchronization of the recording with game visuals;
- master use of the specific recording;
- in-game playback in the intended scenes, locations, menus, credits, etc.;
- looping, fading, ducking, or other technical playback changes;
- loading/caching the audio with the game;
- the intended platforms;
- demos, beta builds, review copies, and public releases as applicable;
- trailers and promotional material if desired;
- territory and term;
- credits;
- updates, patches, DLC, and successor/expanded editions if intended.

The key distinction is that the music is **presentation content**. The player may trigger or encounter it, but the game is not necessarily transforming the recording into a playable rhythm chart.

### B. Rhythm-game use — Clone Hero / Tap Tap-style

If the song becomes a playable chart, the agreement should go beyond ordinary soundtrack language.

The project may need permission to create and distribute game-specific data such as:

- beat and tempo maps;
- note charts;
- timing windows;
- difficulty levels;
- instrument-specific lanes;
- score/combo events;
- practice sections;
- loop points;
- preview clips;
- gameplay-specific edits;
- stems or separated parts, if used.

The contract should also make clear whether the chart may be distributed **with the recording**, separately from the recording, or both.

A rhythm chart is not itself the copyrighted sound recording, but it is a project-created derivative/content layer built around the musical work. The safe engineering practice is therefore to treat the chart and its relationship to the licensed track as part of the negotiated game use rather than assuming that a normal soundtrack license automatically covers it.

### C. VR rhythm / spatial interaction — Beat Saber-style

A Beat Saber-like implementation adds another layer of interaction.

If the recording is used as the basis for timed VR gameplay, the license should expressly cover:

- synchronized gameplay;
- beat mapping;
- timing data;
- note/object placement;
- difficulty variants;
- practice/replay systems;
- preview clips;
- any gameplay edits or shortened versions;
- distribution of the chart/map with the audio;
- promotional footage showing the song in interactive play.

If the game also spatializes, remixes, stems, or otherwise materially transforms the recording, the agreement should expressly address those operations rather than relying on a generic "game use" sentence.

### D. The important distinction for 50 Ways to Leave Another

For our project, define three separate digital-use modes:

```
MODE 1 — SOUNDTRACK
Song
  ↓
Game scene / menu / ending
  ↓
Player experiences the music

MODE 2 — INTERACTIVE SONG
Song
  ↓
Beat / timing data
  ↓
Player acts in synchronization with music

MODE 3 — STANDALONE MUSIC EXPERIENCE
Song
  ↓
Dedicated interactive environment
  ↓
Music drives exploration, visuals, events, or progression
```

Mode 3 matters because a standalone adventure can be more than a conventional soundtrack placement. If the music itself drives visual events, exploration, puzzles, timing, or progression, the agreement should describe those uses specifically.

### E. One license can cover multiple modes — if it says so

There is no reason to create three unrelated licensing programs if an artist is comfortable granting all three.

Instead, the rights schedule can use explicit checkboxes or fields:

| Digital use | Licensed? |
|---|---|
| Standalone adventure soundtrack | ☐ |
| Menu / lobby / credits | ☐ |
| Gameplay synchronization | ☐ |
| Rhythm / beat-matching gameplay | ☐ |
| VR / spatial rhythm gameplay | ☐ |
| Beat maps / charts | ☐ |
| Gameplay edits / loops | ☐ |
| Stems / separated parts | ☐ |
| Offline / cached game delivery | ☐ |
| DLC / expansions | ☐ |
| Trailers / promotional video | ☐ |
| Livestream / recorded gameplay promotion | ☐ |
| Demo / beta / review builds | ☐ |

That gives an independent artist a much clearer choice than asking them to sign a blanket "video game rights" clause.

## The 50 Ways digital-rights record

For the 50 Ways project, a track record should therefore contain:

```
TRACK
  artist:
  title:
  version:
  ISRC:

RIGHTS HOLDERS
  master:
  composition:
  writers:
  publisher/admin:

DIGITAL USE
  soundtrack: yes/no
  standalone adventure: yes/no
  rhythm gameplay: yes/no
  VR/spatial gameplay: yes/no
  chart/beat-map creation: yes/no
  stems: yes/no
  edits/loops: yes/no
  trailers: yes/no
  livestream/promotional capture: yes/no

DELIVERY
  platforms:
  territory:
  term:
  offline/cached:
  DLC/updates:
  exclusivity:

BUSINESS
  fee:
  royalty/revenue share:
  reporting:
  credit:

EVIDENCE
  signed license:
  rights confirmations:
  approved master:
  approved chart/data:
```

**Do not let the filename, MP3/WAV, Bandcamp URL, or chart file itself become the rights record.** The rights record is the authority; the media package is the implementation.

## A particularly useful independent-artist offer

For an independent artist, we can make the first conversation unusually simple:

> **Your music stays yours. We are asking for a non-exclusive license for specified digital game uses. You choose whether we may use it as a soundtrack, an interactive/rhythm track, a standalone music experience, promotional material, or some combination. We identify the exact recording, credit you, and keep a rights record.**

That is much more understandable than asking an artist to navigate traditional record-industry terminology before they even know what the project wants to do.

The actual agreement should then convert those choices into legally precise grant language and should be reviewed by qualified counsel before commercial release.

## Original music is the easiest intake path

The cleanest first catalog is music where the submitting artist can document that they control both:

- the master; and
- the underlying composition.

Instrumental tracks can also simplify certain content and presentation concerns, although they still require proper rights clearance.

Music containing samples, cover versions, leased beats, third-party vocals, commissioned production, or label/publisher obligations needs additional review.

A cover is particularly important: owning an artist's recording of a cover does not necessarily mean the artist owns the underlying composition. Bandcamp itself warns artists not to upload covers without the required written permissions.

## Suggested project licensing tiers

### Tier A — Prototype / non-distributed

Artist permits use in a private or contributor-only prototype under a short written permission.

No public distribution unless the permission says so.

### Tier B — Public demo

Written license covers the named demo, website/demo video, and specified distribution channels.

### Tier C — Game release

Full agreement covering master, composition, game synchronization, distribution, platforms, territory, term, promotion, credits, compensation, and termination.

### Tier D — Rhythm / interactive music catalog

Everything in Tier C plus explicit charting, gameplay, edits, stems, preview, offline/cached delivery, and other interactive-music rights actually required by the implementation.

## What we should ask an artist

A short first-contact questionnaire can be:

1. Do you control the master recording?
2. Do you control the underlying composition?
3. Are there any co-writers or co-owners?
4. Is the song signed to a label or publisher?
5. Is it administered by a PRO, MRO, CMO, or publishing administrator?
6. Does the recording contain samples or other third-party material?
7. Are you authorized to grant a non-exclusive game license?
8. Are you interested in game use, rhythm-game/chart use, or both?
9. Are you open to prototype/demo use before a commercial release?
10. What credit should the project provide?
11. Do you have a preferred license fee or royalty structure?
12. What contact should receive the final agreement?

The questionnaire is a screening tool, not a substitute for the agreement.

## Recommended policy for Return to the Void

1. **Discover artists anywhere, including Bandcamp.**
2. **Never treat a storefront listing as proof of ownership.**
3. **Prefer artists who can document control of both master and composition.**
4. **Use a written license before public distribution.**
5. **Keep a per-track rights record.**
6. **Separate music files from rights metadata.**
7. **Explicitly clear rhythm/chart rights if the game uses them.**
8. **Do not accept samples or covers without checking the additional rights chain.**
9. **Keep prototype permissions distinct from commercial-release permissions.**
10. **Have counsel review the production license before commercial release.**

## Useful references

- [U.S. Copyright Office — What Musicians Should Know about Copyright](https://www.copyright.gov/engage/musicians/)
- [U.S. Copyright Office — Musical Compositions, Sound Recordings & Copyright](https://www.copyright.gov/engage/docs/recording.pdf)
- [Bandcamp Terms of Use](https://bandcamp.com/terms_of_use)
- [Bandcamp — Publishing Rights and Royalties update](https://blog.bandcamp.com/2026/02/25/updates-to-help-songwriters-get-credited-and-paid/)
- [Clone Hero — Adding Custom Songs](https://wiki.clonehero.net/books/clone-hero-manual/page/adding-custom-songs)
- [Clone Hero — song.ini guide](https://wiki.clonehero.net/books/guides-and-tutorials/page/songini-guide)

The project should periodically re-check these external resources because licensing terms and platform documentation can change.

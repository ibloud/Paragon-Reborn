## Return to the Void — Technical Breakdown

This repo documents a technical analysis of **rtn2thevoid**: an open-source MOBA framework built around Epic's released Paragon assets, a modular card/tarot system, and a browser-native WebGL companion layer.

Full project context: [sites.google.com/view/rtn2thevoid/journey](https://sites.google.com/view/rtn2thevoid/journey)

### What Epic's assets cover

Epic released 39+ Paragon hero packages — fully rigged models, animation blueprints, Niagara VFX, audio, and the Agora/Monolith environment packs — free for use in Unreal Engine projects via the [Fab marketplace](https://www.unrealengine.com/en-US/blog/paragon-assets-now-available-for-free-on-the-unreal-engine-marketplace). These form the 3D visual and audio foundation.

### What has to be built

| Component | Covered by Epic | Action |
|---|---|---|
| 3D Hero Models & Rigging | ✅ Yes | Import via Unreal Engine |
| Hero Animations & VFX | ✅ Yes | Built into character packages |
| Environments & Props | ✅ Yes | Agora / Monolith packs on Fab |
| Card UI / 2D Tarot Art | ❌ No | Custom illustration & UI design |
| Core Game Code & GAS | ❌ No | C++ / Blueprint from scratch |
| Card Engine / Deck Logic | ❌ No | Custom data tables & mechanics |

### Integration strategy

**[veiled-dominion-engine](https://github.com/Loptr-Lab/veiled-dominion-engine)** handles the web layer: deck builder, hero lore viewer, and rapid prototype environment for validating game rules before porting to Unreal C++.

**Unreal Engine 5** handles the core game: character abilities via the Gameplay Ability System, Niagara VFX, network replication, and the open-source C++ architecture for community contribution.

---

## For beginners

This project is a **living environment** — built explicitly so newcomers can find where they fit and contribute to a real production pipeline.

Before writing code, read:
- [Clean Coders](https://cleancoders.com/) — the philosophy behind how this project is organized
- [Tom Looman's Unreal tutorials](https://www.tomlooman.com/) — recommended entry point for Unreal C++ and GAS
- [Open Source Guide](https://opensource.guide/) — how to contribute to an open-source project

Contribution areas beyond programming: 2D illustration, card frame design, technical art (poly reduction, shader rewrites for WebGL), and documentation.

---

## License

MIT — see [LICENSE](LICENSE). Paragon assets are subject to Epic's EULA and are not distributed here.

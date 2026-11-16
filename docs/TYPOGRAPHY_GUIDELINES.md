# Typography and reading accessibility

Owner direction: 16 November 2026. Applies to this project's public pages.
Preserve Space Grotesk and Space Mono on the homepage. Keep the grant page's established system-font family. Do not replace the font identity as a side effect of accessibility work.

- Body, explanatory text, table cells and reading links use at least 1rem. Default root size is 112.5% (18px at a 16px browser default).
- Supporting labels use at least .9rem (16.2px at the default browser setting). Essential instructions and actions must not be reduced to tiny display text.
- Provide the visible native “Larger text” toggle on both public pages: root 137.5% (22px at the browser default), aria-pressed state, keyboard access and a minimum 48px target.
- Browser text preferences and zoom must remain available. Use relative font units; never disable zoom or constrain the viewport's maximum scale.
- Shared assets/reading-size.js stores only the text-size preference on this browser/origin. Storage failure must not prevent use; no account, tracking or server record.
- The larger option supplements a readable default. Do not use it to justify shrinking default prose.
- Use readable line height (body 1.7), normal heading tracking, sufficient contrast, wrapping navigation and flexible content heights. Main navigation is sticky in document flow so enlarged/wrapped links do not cover reading content.
- Keep existing page styles as their current presentation authority; this task does not authorize a stylesheet migration or a second theme.
- Verify both sizes at 320, 390, 820 and 1440 CSS pixels, 200% zoom/text enlargement, keyboard toggle/focus, persistence across pages/reload, storage denied, JavaScript unavailable, and reduced motion. Essential content remains readable without JavaScript; the nonfunctional control remains hidden.
- Record checks actually run. Do not claim physical iPad/Safari/VoiceOver acceptance from Chromium automation.

# Hyperframes Composition Brief: Golden Hour Coffee Co.

## Objective
Create a short launch-style brag video for Golden Hour Coffee Co. — a cozy neighborhood café in East Austin. The video should feel like the first sip of a latte: warm, inviting, and exactly what you needed.

## Output
- Composition directory: `brag-output-2026-09-19-153000/composition/`
- Rendered video: `brag-output-2026-09-19-153000/brag.mp4`
- Format: landscape — 1920x1080
- Duration: 20 seconds

## Source Material
- Project root: `D:\Ibrahim106\Downloads\goldenhour`
- Primary files read: `index.html`, `src/index.css`, `src/App.tsx`, `src/components/Home.tsx`, `src/components/Header.tsx`, `src/data.ts`, `README.md`, `package.json`
- Product name: Golden Hour Coffee Co.
- Tagline / strongest claim: "Slow mornings, strong coffee."
- Key UI or visual moment to recreate: the terracotta hero card with rounded corners overlapping the sunlit café interior photo
- Copy that must appear verbatim:
  - "Slow mornings, strong coffee."
  - "A cozy neighborhood café where locals linger over pour-overs, catch up over brunch, and watch the light change through the front window all day long."
  - "Loved by Locals"
  - "Open Daily 7AM–3PM · 1214 E 6th St, Austin, TX"
  - "Est. 2023 • East Austin, TX"

## Creative Direction
- Tone preset: polished
- Creative direction: "quiet premium neighborhood café film — warm, inviting, sun-drenched"
- Interpretation: Fewer scenes, longer holds. Confidence through restraint. The product speaks for itself through warm imagery and clean typography. No rush.
- Angle: This isn't a tech product launch. This is a love letter to slow mornings. The video should feel like the first sip of a Golden Hour Latte — warm, inviting, and exactly what you needed.
- Hook: The sunlit café interior fills the screen — warm light, trailing ivy, rustic wood. A single word fades in: "linger."
- Outro / punchline: The Golden Hour logo holds center frame with "Open Daily 7AM–3PM · East Austin, TX" — quiet confidence. No call to action needed.
- Avoid:
  - Generic SaaS language
  - Abstract filler visuals
  - Unrelated visual redesign
  - Startup energy or aggressive pacing

## Visual Identity
- Background: #FBF3E7 (cream)
- Text: #3B2A20 (espresso)
- Accent: #C1633D (terracotta)
- Secondary: #8A9A5B (sage), #E08E45 (burnt-orange)
- Display font: Kalam (cursive script) — for headlines and the "linger." word
- Body font: Inter (sans-serif) — for body text and descriptions
- Visual references from the project: the terracotta hero card with rounded corners, the sunlit café interior photo, the "G" logo circle, the featured dish cards with badges and price tags

## Storyboard
Use the storyboard in `brag-output-2026-09-19-153000/brag-plan.md` as the creative contract.

Scene summary:
1. The Golden Light — 5s — Sunlit café interior fills screen, "linger." fades in at center in Kalam script
2. The Promise — 5s — Terracotta hero card slides up with "Slow mornings, strong coffee." tagline, buttons appear
3. From the Kitchen — 6s — Three dish cards arrive one by one: Golden Hour Latte, Whipped Ricotta Toast, Cinnamon Roll Skillet
4. Loved by Locals — 4s — "Loved by Locals" heading, three testimonial cards slide in with star ratings
5. The Logo — 5s — Clean cream background, Golden Hour logo scales in, text fades below

## Audio
- Audio role: warm bed — gentle acoustic guitar, ambient café texture
- Audio arc: warm acoustic guitar fades in over sunlit café, stays low through dish reveals and testimonials, swells gently at the logo, fades to silence
- Music: `happy-beats-business-moves-vol-12-by-ende-dot-app.mp3` — steady and clean, 109.96 BPM
- Music treatment: fade in at 0s, volume 0.30-0.35, gentle swell at logo reveal (scene 5), fade out over last 2 seconds
- Music cue guidance: bundled preset available at `assets/music/cues/happy-beats-business-moves-vol-12-by-ende-dot-app.music-cues.json`; strong cues at 8.74s, 13.11s, 17.47s, 22.93s; beat grid every ~0.55s; target 22.93s for logo reveal, 8.74s for hero card reveal
- Audio-reactive treatment: subtle; use music RMS to gently warm the cream background tint, nothing aggressive
- Audio-coupled moments:
  - Scene 2 (hero card reveal) — card slides up aligned to strong cue at ~8.74s
  - Scene 3 (dish cards) — three cards arrive one by one snapped to consecutive beats
  - Scene 5 (logo reveal) — logo scales in aligned to strong cue at ~22.93s
- SFX selection guidance: sparse, polished — one soft `interface/drop_001` for the "linger." word, gentle `casino/card-place-*` for dish card arrivals, `interface/drop_002` for testimonial cards, `impact/impactSoft_medium_000` for logo reveal
- SFX analysis guidance: use `sfx-analysis.md` for file selection; prefer low/medium HF risk for polished moments
- Exact SFX choice: Hyperframes should choose filenames, timestamps, density, and volume based on the implemented animation
- Audio files: music and selected SFX already copied into `brag-output-2026-09-19-153000/composition/assets/`

## Hyperframes Instructions
Load the composition-building Hyperframes domain skills — `hyperframes-core` (composition contract + `data-*` timing), `hyperframes-animation` (motion), `hyperframes-creative` (design spec, beats, audio-reactive), `hyperframes-keyframes` (seek-safe keyframes), and `hyperframes-cli` (lint/check/render). /brag is its own workflow: do not enter the `hyperframes` entry-point intent interview and do not route into its generic promo / launch-video workflow. Prefer native Hyperframes conventions over anything in `/brag`.

Requirements:
- Show at least one real UI, copy, or visual element from the source project (the terracotta hero card, the dish cards, the café interior photo).
- Keep all text readable in the final render — "linger." holds 3s, "Slow mornings, strong coffee." holds 2s+, dish names hold 1.5s+ each.
- Keep the video within 15-25 seconds (target 20s).
- Include the planned music/SFX layer — music is enabled, SFX is enabled.
- Treat `/brag` audio notes as guidance, not a fixed cue sheet. Choose SFX after the visual animation exists.
- Treat music cue metadata as optional timing hints. Hyperframes decides exact animation timing and should ignore cues that hurt readability, scene pacing, or the product story.
- Major reveals may move toward nearby strong cues within about 0.15s. Use 1-3 strong cue locks in this 20s video.
- Use SFX to support motion: card sounds for dish reveals, soft drop sounds for text pop-ins, one soft impact for the logo.
- Honor planned music treatment: fade-in at 0s, volume 0.30-0.35, gentle swell at logo, fade-out over last 2s.
- Consider Hyperframes audio-reactive workflow: extract audio data and use RMS/frequency bands for subtle background warmth. No waveform/equalizer visuals.
- Use local assets for audio — files are already in `composition/assets/`.
- Run `hyperframes check` before render — it is brag's single gate.

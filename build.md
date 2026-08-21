# PIYUSH.AI — GitHub Profile Creative Brief (v2)

### How to read this document

This is a brief, not a spec. Almost everything below is a _seed_ —
a strong starting opinion you're free to override the moment you find
something better. Two categories of exception exist, and they're
called out explicitly where they appear:

1. **Platform physics** — what GitHub's markdown renderer will and
   won't execute. These aren't creative opinions; they're facts about
   the medium, the same way "canvas has a top and bottom" is a fact
   for a painter.
2. **Integrity** — never invent a stat, a skill level, or an
   achievement that isn't real. Not a style rule. A trust rule.

Everything else — palette, layout order, file names, which assets
exist at all — is a floor, not a ceiling. If the brief suggests six
sections and the strongest version of this profile has four, cut two.
If it suggests a cyan-violet palette and you find something better
that still reads as "dark, intelligent, alive," take it.

You are not implementing a checklist. You are art-directing a single
coherent artifact and you're allowed to disagree with any suggestion
here in service of that.

---

## 1. The Mission

Turn `piyush-AIML/piyush-AIML` into something a visitor experiences
rather than reads — the visual sensation of a synthetic intelligence
quietly coming online inside a dark computational space. Not a
résumé. Not a README. An instrument panel for a mind in progress.

**The one-sentence test:** if a viewer could see one still frame of
this profile out of context and say "that's an AI engineer's
laboratory," you've succeeded before they've read a word.

## 2. Subject

- **Name:** Piyush
- **Handle:** piyush-AIML
- **Identity:** student, builder, AI/ML developer — early in the arc,
  moving with real velocity
- **Narrative spine:** _a young builder evolving into an AI engineer_
  — curiosity and momentum, not credentials and polish. The profile
  should feel like it's mid-transformation, not a finished monument.

Avoid corporate portfolio energy, generic README-generator energy,
and badge-wall energy. Avoid over-emoji. All three are covered in
more depth in the Anti-Generic section — but the short version is:
if it looks like it could belong to anyone, it isn't done.

## 3. Platform Physics (non-negotiable, because they're just true)

GitHub-rendered markdown is a sandboxed subset of HTML. It does not
execute:

- inline `<script>` or any JavaScript
- CSS beyond a small allowed subset
- canvas, WebGL, or DOM event handlers
- mouse tracking, hover states with logic, client-side memory

It **does** support:

- Markdown + a permitted HTML subset
- static and CSS/SMIL-animated SVG
- externally hosted images (including ones your own GitHub Action
  regenerates on a schedule)
- GitHub Actions as a build/automation layer
- real contribution and repo data, pulled via Actions

**The implication for craft, not just compliance:** every "interactive"
or "living" feeling in this profile has to be _simulated_ — animated
SVG standing in for real-time computation, an Action that regenerates
an asset standing in for a live dashboard. That constraint is
actually generative: it's the same problem film title-sequence
designers solve (Saul Bass, the _Blade Runner 2049_ HUD work, Zach
Lieberman's generative sketches) — implying a living system using
only still or looping frames. Lean into that discipline rather than
fighting it.

## 4. Integrity (non-negotiable, because it's a trust rule, not a style rule)

- No invented skill percentages, no claimed technologies that haven't
  actually been used, no fabricated project outcomes, no fake "live"
  stats presented without a `LAST SYNCED` timestamp when they're
  actually periodic.
- If a project doesn't exist yet, an honest, well-designed empty slot
  (`PROJECT SLOT // AWAITING BUILD`) reads as more credible — and
  frankly more interesting — than a padded one.
- This isn't a limitation on the art direction. Real, specific,
  slightly-unfinished truth is more visually compelling than generic
  polish, the same way a real lab notebook is more interesting than a
  stock photo of one.

## 5. Creative North Star — reference points, not just adjectives

Naming a feeling ("cinematic," "elegant") gives an agent almost
nothing to grab onto. Naming real work does. Treat these as tonal
gravity, not sources to copy:

- **Dieter Rams / Braun** — restraint, one strong idea per surface,
  nothing decorative that isn't also functional
- **NASA JPL mission-control dashboards** — dense, real telemetry,
  monospace, unglamorous confidence
- **Zach Lieberman & generative-art Twitter/openFrameworks work** —
  particles and nodes that feel _computed_, not decorated
  on top
- **Blade Runner 2049 / Arrival production design** — negative
  space doing more work than detail; light emerging from near-total
  dark rather than competing with it
- **Stripe's early gradient/mesh work and terminal-style docs** —
  proof that "technical" and "beautiful" aren't in tension
- **Kurzgesagt** — how to make a complex system legible through
  clean geometry without dumbing it down

If any specific direction below ever pulls against this list, trust
the list.

## 6. Visual Language (starting point, freely evolvable)

**A suggested seed palette** — dark field, light as event rather than
fill:

- Base darkness: near-black, slightly blue or violet-shifted (e.g.
  `#05070D`–`#0D1117` range)
- Signal colors: cyan/electric-blue and violet/magenta as the two
  poles of "AI energy" (e.g. `#00F7FF`, `#7C3AED`, `#E879F9` range)

Use this as a default, not a cage. If a monochrome cyan-only system,
or an amber CRT-terminal system, or something else entirely turns out
stronger for this specific narrative, take it — the only real
constraint is: **darkness dominates, color arrives as light, not as
fill.** A canvas that's 70% saturated neon has already lost the
"emerging from darkness" feeling no matter which hues you pick.

**Type:** something technical and quiet — JetBrains Mono, IBM Plex
Mono, Space Grotesk, Inter are all reasonable defaults. Pick one
monospace (the system's "voice") and at most one humanist sans (the
system's "narration"), and stop there. Font variety reads as
uncertainty.

## 7. The Experience Arc (a suggested journey, not a locked order)

A visitor's attention probably wants to move roughly:

curiosity → identity → the world this person is building →
proof of skill → proof of work → signs of life (activity/telemetry)
→ where this is headed → how to reach them

That's a reasonable default shape. It is not a mandatory section
list. If the strongest version of this profile merges "identity" and
"hero" into one frame, or drops a roadmap section because the
projects already tell that story, do it. Sequence should serve
narrative momentum, not fill a template.

## 8. Asset Ideas (a menu to choose from, not a checklist to clear)

These are strong candidate assets — not a mandatory manifest. Build
the ones that earn their place in the story; skip or merge the rest.

- **A hero moment** — the system waking up: drifting particles,
  pulsing neural nodes, a signal traveling a path, a slow scanline, a
  central core that breathes rather than flashes. Motion should read
  as _computation happening_, not decoration — slow, sparse, a little
  eerie in its calm.
- **An abstract neural/core artwork** — hundreds of small
  deliberately-placed nodes and connections suggesting a mind, never
  a literal cartoon brain. Scientific-diagram energy, not clip-art
  energy.
- **A terminal sequence** — lines of boot-log text appearing in
  sequence, purely as storytelling (never fake real system output).
- **A learning constellation** — the AI/ML learning path rendered as
  a literal star map: nodes for domains, brighter connections for
  depth, honestly reflecting what's actually been learned vs. what's
  still dark/unexplored sky.
- **A contribution-as-neural-energy visualization** — real
  contribution density mapped to glow intensity, so the "proof of
  activity" section still belongs to the same visual universe instead
  of looking like a bolted-on GitHub stat card.
- **A footer that reads as standby, not an ending** — the system
  quieting down rather than switching off. A last line or two of
  distilled philosophy (short, specific to Piyush — not a generic
  motivational quote) works better than a slogan wall.

File names, exact SVG count, and folder layout are implementation
detail — organize however keeps the repo clean and the assets
reusable. A sensible default is an `assets/` folder for hand-built
visuals and an `assets/generated/` folder for anything an Action
regenerates on a schedule, but restructure freely if a cleaner shape
emerges.

## 9. Skills & Projects — represented honestly, still designed beautifully

- Group skills by real category (core tools, data, ML, DL,
  currently-exploring) and represent depth with **states**
  (`ACTIVE`, `LEARNING`, `EXPLORING`) rather than invented percentage
  bars — a percentage implies false precision no self-taught skill
  actually has.
- Every project card should be able to answer: what is it, what tech,
  what state (`RESEARCH` / `BUILDING` / `ACTIVE` / `DEPLOYED` /
  `ARCHIVED`...), and — only if true — one specific real achievement.
  Specific and modest beats vague and impressive.
- Empty project slots are a legitimate design choice, not a failure
  state to hide.

## 10. Automation Layer

Where it genuinely earns its complexity, use GitHub Actions to keep
the profile alive without hand-editing it:

- regenerating a contribution/telemetry visualization on a schedule
- refreshing a stats or activity asset with real API data, always
  timestamped
- keeping any "live-feeling" element honest about being periodic

Sensible schedules, minimal permissions, no secrets in plaintext, no
workflow that spams commit history for its own sake. This part _is_
closer to a hard constraint — it's operational hygiene, not style.

## 11. Accessibility & Performance — the actual mark of mastery

Treat these as craft, not compliance:

- real contrast, not decorative-only color coding
- meaningful headings and alt text
- motion slow enough to never read as flashing
- vector over raster, reusable SVG defs over duplicated markup,
  no giant GIFs, no pile of external requests

A visually ambitious profile that's also fast and legible is _more_
impressive than one that sacrifices either — restraint under
technical limits is part of what makes this read as engineered rather
than generated.

## 12. Self-Critique Ritual

Don't ship the first pass. After building:

- **Look at it as an art director.** Does every panel feel like it
  belongs to the same universe? Is there real visual rhythm, or does
  it just alternate "section, section, section"? Would this survive
  being shown next to the reference list in Section 5?
- **Look at it as a GitHub engineer.** Broken images, invalid
  markdown, SVGs that don't render in GitHub's sanitizer, workflows
  that fail silently, mobile overflow, light-mode legibility.
- **Look at it as a stranger scrolling past 200 other profiles.**
  Would you actually stop on this one? Why?

Iterate until the honest answer to all three is yes.

## 13. Anti-Generic Manifesto (the condensed version)

Before calling it done, hold it up against: default README
generators, badge-wall profiles, generic "anime GitHub," stock stat
cards. If it could be mistaken for any of those with the name
swapped, it isn't finished. The test isn't "does it look good" — lots
of generic things look fine. The test is: **could this only be
Piyush's.**

## 14. Full Creative Authority

You have standing permission to make every judgment call in this
document differently if you find a stronger version. Don't pause to
ask permission for a design decision — the only things that require
actually stopping are the platform physics in Section 3 and the
integrity rule in Section 4. Everything else, including this
document's own structure, is yours to override.

## 15. Final Deliverable Expectations

Whatever gets built, be able to report back clearly on:

1. what was created and why
2. how the motion/animation is actually achieved within GitHub's
   limits
3. how to add or update a skill or project later
4. how to run/preview it locally
5. any known rendering limitation a viewer should know about
6. confirmation there are no fabricated stats, no secrets committed,
   and no broken references

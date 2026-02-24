# CLAUDE.md — Affections of Vissan
> Game development specification for Claude Code.  
> Read this entire file before writing any code.

---

## What This Is

A mobile-first visual novel / dating sim set in the vampire kingdom of **Vissan**. The player selects an avatar character and pursues a love interest through 3 rounds of story encounters. Each round has 3 scenes. Each scene has 3–4 dialogue exchanges and narration beats. The goal is emotional progression — by Round 3, a kiss.

**Target platform:** Portrait-only. iPhone + iPad Safari. Offline-capable (all assets embedded as base64). No backend required for Round 1.

**Tech stack:** Single self-contained `.html` file. Vanilla JS, no frameworks. Embedded base64 images. Google Fonts via CDN (graceful fallback to Georgia/serif if offline).

---

## Character Roster

Four characters. Any can be played as an avatar OR pursued as a love interest — except a character cannot be both in the same run.

| Key | Name | Title | Colour Token |
|---|---|---|---|
| `kohan` | Kohan | The Fire Witch | `#F0C95B` |
| `andam` | Andam | The Vampire General | `#B8A898` |
| `catarina` | Catarina | The Vampire Princess | `#E8C080` |
| `max` | Max | The Moon Elf | `#A8C5DA` |

### Character Colours — Dialogue + UI

Each character has a unique colour used for:
- Their name label in the dialogue panel
- Their act progress pip colour (see Pip Colours below)
- Their bio name heading

```
kohan:    #F0C95B  (gold)
catarina: #E8C080  (warm gold)
andam:    #B8A898  (warm grey)
max:      #A8C5DA  (silver blue)
narrator: rgba(240,201,91,.38)  (dim gold)
```

---

## Screen Flow

```
Landing
  └─► Avatar Select
        └─► (tap card) Bio Screen [browsable ← →]
              └─► [PLAY AS X] → back to Avatar Select (selected)
        └─► [CHOOSE WHO TO PURSUE] → Interest Select
              └─► (tap card) Bio Screen [browsable ← →, excludes avatar]
                    └─► [PURSUE X] → back to Interest Select (selected)
              └─► [BEGIN THE STORY] → Encounter
                    │
                    │  Within Encounter:
                    │  Scene 1 → [CONTINUE →] button → Scene 2
                    │  Scene 2 → [CONTINUE →] button → Scene 3
                    │  Scene 3 resolves:
                    │    ├─► Any fail reaction renders fully in dialogue
                    │    │   Player reads it, then taps [CONTINUE →]
                    │    │   → Fail Result Screen
                    │    │       └─► [TRY AGAIN] → Avatar Select
                    │    │             (full fresh flow: avatar → interest → play)
                    │    └─► Win resolves fully in dialogue
                    │        Player reads it, then taps [CONTINUE →]
                    │        → Win Result Screen
                    │              └─► [NEXT GOAL] → Round 2 Encounter
                    │
                    └─► Round 2 → Round 3 → True Ending Screen
```

---

## Visual Design System

### Colours
```css
--bg:       #181818       /* base background, all screens */
--gold:     #F0C95B       /* primary accent */
--gold-dim: rgba(240,201,91,.35)
--cream:    #F5ECD0       /* primary text */
--cream-dim:rgba(245,236,208,.60)
--border:   rgba(240,201,91,.30)
--border-hi:rgba(245,236,208,.50)
```

### Typography
- **Display / headings:** `Cinzel Decorative` (Google Fonts), fallback `Georgia, serif`
- **UI labels / nav:** `Cinzel` (Google Fonts), fallback `Georgia, serif`
- **Body / dialogue / bio text:** `Cormorant Garamond` (Google Fonts), fallback `Georgia, serif`

All fonts loaded via Google Fonts CDN. Game is still playable offline — fonts fall back to Georgia.

### Buttons
Dark background, `1px` border (`--border-hi`), `border-radius: 6px`, `Cinzel` font, `letter-spacing: .42em`, all-caps. Hover: border brightens to `--gold`, subtle gold background tint.

### Cards
`border-radius: 8px`, thin gold/cream border, `overflow: hidden`. Portrait images: `object-fit: cover`, `object-position: top center`.

---

## Screen Specifications

### 1. Landing Screen
- **Layout:** Scrollable single column, `background: #181818`
- **Title:** `THE AFFINITY OF VISSAN` — `Cinzel Decorative`, large (clamp ~2rem–2.8rem), gold, centered, ALL CAPS
- **Image:** Full-width world panorama image (aspect ratio ~390:280), no border radius, edge to edge
- **Below image (dark bg):**
  - `AN AI-DRIVEN VISUAL NOVEL` — `Cinzel`, spaced caps, gold, centered
  - Body lore paragraphs — centered, cream-dim
  - Italic tagline in gold: *Some doors should not be opened carelessly.*
  - `ENTER VISSAN` button — centered, at bottom

### 2. Avatar Select Screen
- **Hero image** at top (~52vw height, max 260px), fades to `#181818` at bottom via gradient overlay
- **Heading:** `Who Are You?` (`Cinzel Decorative`, gold) + subtitle `Step 1: Choose Your Character` (`Cinzel`, small caps, dim)
- **2×2 grid** of character cards, full-width, zero gap between cells
  - Each card: square aspect ratio, portrait photo fills card, gradient overlay bottom 60%
  - Character name at bottom center (`Cinzel`, cream)
  - Selected card: `2px solid #F0C95B` border + `YOU` badge top-right
  - Tap a card → selects it AND opens Bio screen (context: `avatar`)
- **CTA button** below grid: `CHOOSE WHO TO PURSUE →`

### 3. Interest Select Screen
- **Top bar:** `← BACK` button (left)
- **Heading:** `Who to Pursue?` + `Step 2: Choose Your Love Interest`
- **Diagonal stacked cards** — scrollable vertically
  - 3 cards visible (excludes the avatar character)
  - Each card 200×200px, staggered left offsets: `20px` / `90px` / `160px`
  - Tap → opens Bio screen (context: `interest`)
  - After returning from Bio with confirm → card shows `PURSUING` badge
- **Fixed footer:**
  - Villain hint line (italic, dim red): appears after selection — *"One rival lurks in the shadows — their identity will be revealed."*
  - `BEGIN THE STORY →` button — disabled until a card is selected

### 4. Bio Screen
- **Top nav bar:**
  - `← [PREV NAME]` button left
  - Character name (`Cinzel Decorative`, gold, centered) + subtitle below
  - `[NEXT NAME] →` button right
  - Arrows browse all 4 characters when context is `avatar`; browse 3 (excluding avatar) when context is `interest`
- **Portrait card:** fills width minus `28px` padding each side, aspect ratio `331:496`, `border-radius: 8px`, gold border `1.5px`
- **Bio text:** centered, `Cormorant Garamond`, `1rem`, `line-height: 1.82`, cream-dim
- **CTA button:** `PLAY AS [NAME]` (avatar context) or `PURSUE [NAME]` (interest context) — centered, bottom

### 5. Encounter Screen
- **Portrait strip** — top 40vh, min 220px
  - Full-bleed character image, `object-position: top center`
  - Gradient overlay: transparent → `rgba(24,24,24,.96)` at bottom
  - **Bottom-left overlay:**
    - Small circular avatar (36×36px, gold border) — shows love interest portrait
    - Act label (e.g. `Act I · First Meeting`) — `Cinzel`, tiny, dim gold
    - Character name — `Cinzel Decorative`, character colour
    - **Progress pips row** (see Pip spec below)
  - **Bottom-right overlay:** Barometer (see Barometer spec below)
- **Dialogue panel** — fills remaining screen height
  - Dark background (`#181818`), scrollable
  - Each dialogue line: who-label (tiny `Cinzel` caps in character colour) + text below
  - Narrator text: italic, cream-dim
  - Character text: upright, cream
  - Player text: cream, slightly dimmer, blue-tinted who-label
  - Villain text: dim red
  - "Moment of affection" lines: italic, gold, left border `2px solid gold-dim`
- **Footer (pinned):**
  - `border-top: 1px solid rgba(240,201,91,.10)`
  - Prompt label (`Cinzel`, tiny, dim) e.g. `HOW WOULD YOU ANSWER?`
  - 3 choice buttons (italic `Cormorant Garamond`, rounded border)
  - Continue button (appears after response resolves, replaces choices)

### 6. Result Screen
- **Title** at top — `Cinzel Decorative`, large, gold (win) or white (loss)
- **Scene block:**
  - Full-width background landscape image (300px tall), `brightness(.72)`
  - Character portrait centered over it — 48% width, square, rounded, cream border
- **Body below:**
  - Result message paragraph — centered, cream-dim
  - `What is your next goal?` — `Cinzel`, gold, spaced caps
  - CTA buttons (`TRY AGAIN` / `DEEPEN THE BOND` / `CHOOSE A DIFFERENT PATH`)

---

## Progress Pips

The pip row shows all dialogue exchanges across all 3 scenes of the current round.

- **Total pips = 9** (3 scenes × 3 exchanges each) displayed in a row
- Each pip: `22px wide × 3px tall`, `border-radius: 2px`
- Colours are **per-character** of whoever is speaking in that exchange:

| Character | Pip colour |
|---|---|
| Kohan | `#F0C95B` |
| Catarina | `#E8C080` |
| Andam | `#B8A898` |
| Max | `#A8C5DA` |
| Narrator | `rgba(240,201,91,.38)` |

- **Completed exchange:** full colour opacity
- **Current exchange:** full colour + glow `box-shadow: 0 0 5px [colour]`
- **Future exchange:** `opacity: 0.35` (same colour, just dimmer — player can see what's coming)

---

## Barometer

Shows the love interest's current level of interest. Located bottom-right of portrait strip.

- Label: `INTEREST` (`Cinzel`, tiny, dim gold)
- Track: `90px × 4px`, dark background, thin gold border
- Fill: gradient left→right `#7a1020 → #C9A84C → #F0D080`, width = trust % (0–100)
- Arrow indicator: small triangle pointing down at fill right edge, appears after first exchange
- Mood label below: italic `Cormorant Garamond`, dim gold

**Mood thresholds:**
```
0–20:   Cold
21–35:  Guarded
36–50:  Curious
51–65:  Interested
66–80:  Warm
81–100: Captivated
```

- Starts at `30` (Curious range) each round
- Updates after each exchange (smooth CSS transition)
- Stays visible across all acts

---

## Game Logic

### Round Structure
```
Round 1 → Round 2 → Round 3 → True Ending
  ↓ fail       ↓ fail       ↓ fail
  Retry        Retry        Retry
```

Each round = 3 scenes. Each scene = 3 dialogue exchanges + narration. 9 exchanges per round total.

### Scene Structure (per round)

| Scene | Name | Content |
|---|---|---|
| 1 | Introduction | Player meets love interest. First impressions. |
| 2 | Villain Entrance | A rival character interrupts or complicates. |
| 3 | Aftermath | Resolution of tension. Win = sign of affection. Fail = withdrawal. |

### Exchange Structure
Each exchange is one of:
- **Question + Answer** — character asks something, player chooses a response
- **Prompt + Action** — narrator sets up a moment, player chooses how to act

Each exchange has **3 preset choices** labelled with a trait tag.

### Win Condition per Round

| Round | Win = |
|---|---|
| 1 | First sign of affection (hold hands, meaningful look, a favour, a compliment) |
| 2 | Heat rises — a private moment, almost-kiss, declaration of intent |
| 3 | The kiss (or equivalent final affection for character's personality) |

---

## Trust Score System

**Hidden from player.** Expressed only through the barometer mood label.

- Starts at `30` each round
- Each exchange adds or subtracts based on trait match (see tables below)
- Clamped `0–100`
- Round ends in **Win** if trust ≥ 50 at scene 3 resolution
- Round ends in **Fail** if trust < 50

### Trait Scoring — Round 1

Each choice is tagged with a trait. Trust delta = table value × 8.

| Trait | Kohan | Catarina | Max | Andam |
|---|---|---|---|---|
| Honesty | +1 | 0 | +2 | 0 |
| Curiosity | +2 | 0 | +1 | 0 |
| Strategy | 0 | +2 | 0 | +1 |
| Deflection | 0 | +1 | 0 | +2 |

So `+1` = `+8 trust`, `+2` = `+16 trust`, `0` = `0`, negative traits = `-8`.

### Trait Scoring — Round 2

| Trait | Kohan | Catarina | Max | Andam |
|---|---|---|---|---|
| Honesty | +1 | +2 | 0 | 0 |
| Curiosity | +1 | 0 | +1 | +2 |
| Strategy | +2 | +1 | 0 | +1 |
| Deflection | 0 | +1 | +2 | 0 |

### Trait Scoring — Round 3

| Trait | Kohan | Catarina | Max | Andam |
|---|---|---|---|---|
| Honesty | +2 | +1 | +2 | +1 |
| Curiosity | +1 | +2 | +1 | +2 |
| Strategy | +1 | +1 | +1 | +1 |
| Deflection | 0 | 0 | 0 | 0 |

> **Note:** Deflection is never rewarded in Round 3. All characters want authenticity by the final round.

---

## Spook Mechanic

If the player makes a bold move (e.g. Hold Hands) while trust is below threshold (< 45), the love interest **pulls back (Startled)**. The player gets **one recovery attempt**:
- Successful repair → trust rises, game continues to villain scene
- Failed repair (second spook) → round ends in Fail

`spookUsed` flag tracks whether recovery chance has been used this round. Resets each round.

---

## Villain System

- Villain is **randomly selected** from the 2 remaining characters (not player, not interest)
- Villain appears in **Scene 2** of every round
- Villain has unique dialogue lines per combination (stored in `ACTS[round][scene].villain.lines[villainKey]`)
- Player response to villain affects trust (+16 / +10 / -14 depending on choice)
- Same random villain persists across all 3 scenes of a round; re-randomised each round

---

## Starting Locations (Round 1)

| Love Interest | Location | Background image key |
|---|---|---|
| Kohan | Human Village | `bg_village` |
| Max | Moon Elf Forest | `bg_forest` |
| Catarina | Vissan Palace | `bg_castle` |
| Andam | Vissan Palace | `bg_castle` |

Rounds 2 and 3 may use different locations — images to be provided by designer.

---

## Asset System

All images are stored as base64 strings in a `const ASSETS = {}` object at the top of the JS.

```js
const ASSETS = {
  // Characters
  kohan:    'data:image/png;base64,...',
  andam:    'data:image/png;base64,...',
  catarina: 'data:image/png;base64,...',
  max:      'data:image/png;base64,...',
  // Backgrounds
  bg_village: 'data:image/png;base64,...',
  bg_forest:  'data:image/png;base64,...',
  bg_castle:  'data:image/png;base64,...',
  bg_world:   'data:image/png;base64,...',
};
```

To swap in new assets: replace the base64 string for that key. No other code changes needed.

Per-round character images will be added in future (e.g. `kohan_r2`, `kohan_r3`). Fall back to base key if round-specific not found:
```js
function getCharImg(key, round) {
  return ASSETS[key + '_r' + round] || ASSETS[key];
}
```

---

## Code Architecture

Single HTML file. Organised in this order:

```
1. <head>  — meta, Google Fonts link, <style> block
2. <body>  — all screen divs (display:none except active)
3. <script>
   ├── ASSETS object (base64 images)
   ├── GAME_DATA object (all dialogue, scenes, acts, rounds)
   ├── STATE object  (mutable game state)
   ├── UI helpers    (goTo, dlg, setChoices, showContinue, barometer, pips)
   ├── Screen builders (buildInterestCards, buildBio, buildAvatarGrid)
   └── Game flow     (startRound, startScene, startExchange, handleChoice, endRound)
```

### State Object

```js
const STATE = {
  player:    null,   // character key
  interest:  null,   // character key
  villain:   null,   // character key (random, set per round)
  round:     1,      // 1–3
  scene:     1,      // 1–3
  exchange:  1,      // 1–3
  trust:     30,     // 0–100
  spookUsed: false,
  bioContext: null,  // 'avatar' | 'interest'
};
```

### GAME_DATA Structure

```js
const GAME_DATA = {
  characters: { kohan: {...}, andam: {...}, catarina: {...}, max: {...} },
  rounds: {
    1: {
      scenes: {
        1: { label, open, exchanges: [ { who, text, choices: [{tag, trait, text, reply, mood}] } ] },
        2: { villain scene structure },
        3: { resolution scene structure }
      }
    },
    2: { ... },
    3: { ... }
  },
  traitScores: {
    1: { kohan: {Honesty:1, Curiosity:2, ...}, ... },
    2: { ... },
    3: { ... }
  }
};
```

---

## Dialogue Rendering Rules

- Narrator lines: `font-style: italic`, cream at 50% opacity, who-label = `NARRATOR` in dim gold
- Character lines: upright, cream at 82% opacity, who-label in character colour
- Player lines: upright, cream at 75%, who-label `YOU` in silver-blue
- Villain lines: cream at 85%, slightly red-tinted who-label
- "Moment" lines (affection beat): italic, gold, `border-left: 2px solid gold-dim`, `padding-left: 10px`
- Lines animate in: `opacity 0→1, translateY 4px→0`, duration `0.38s`
- Auto-scroll dialogue area to bottom after each new line
- Stagger delays between open narration lines: `700ms` apart

---

## Continue Button — Rules

The `[CONTINUE →]` button is the **only** way to advance between scenes, and between the final scene and the result screen. Nothing ever auto-advances. The player must always tap to proceed.

### When it appears

| Moment | Button label | Leads to |
|---|---|---|
| After Scene 1 resolves (all exchanges done) | `CONTINUE →` | Scene 2 opens |
| After Scene 2 resolves | `CONTINUE →` | Scene 3 opens |
| After Scene 3 win reaction renders | `CONTINUE →` | Win Result Screen |
| After Scene 3 fail reaction renders | `CONTINUE →` | Fail Result Screen |
| After spook recovery choice renders (success) | `CONTINUE →` | Villain scene |
| After spook recovery choice renders (fail) | `THE EVENING ENDS →` | Fail Result Screen |

### What "resolves" means

A scene is **resolved** when:
1. The player has tapped a choice
2. All choice buttons are disabled
3. The love interest's reaction line has fully rendered in the dialogue
4. The barometer has updated

Only after all 4 of these: show the Continue button.

### Visual spec

- Position: pinned in the footer, right-aligned, below the disabled choices
- Style: `Cinzel`, tiny caps, `letter-spacing: .38em`, gold tint, transparent background, thin gold border, `border-radius: 5px`
- Hidden by default (`display: none`), revealed with `display: flex`
- **Never** show Continue at the same time as active choice buttons — choices disappear first (disabled + greyed out), then Continue appears after a short delay (`300ms`) so the player notices the transition

### Fail pacing — critical rule

When a scene ends in failure (spook not recovered, or villain won, or trust too low at scene 3):

1. The love interest's **full reaction line** renders in dialogue normally
2. If it is a spook fail: add a narrator closing line (e.g. *"She does not look back."*) with `700ms` delay
3. Barometer updates to reflect the low trust (show `Cold` or `Withdrawn`)
4. **Wait `500ms`** then show the Continue button labelled `THE EVENING ENDS →`
5. Player reads everything at their own pace, then taps
6. **Only then** navigate to the Fail Result Screen

Do NOT navigate to the Fail Result Screen automatically. Do NOT skip the reaction. The player must feel the consequence before moving on — this is what motivates them to retry.

---

## Fail Result Screen — Retry Flow

The Fail Result Screen must encourage the player to try again without feeling punitive.

### Content
- **Title:** `The Evening Closes` — `Cinzel Decorative`, large, gold
- **Scene:** Full-width landscape background, love interest portrait centred over it (same layout as win result)
- **Message:** Short, warm, not harsh. Example: *"This path did not lead where you hoped. Another approach awaits."*
- **Label:** `What is your next goal?` — gold, spaced caps
- **Buttons:**
  - Primary: `TRY AGAIN` → navigates to **Avatar Select** (full fresh flow)
  - Secondary: `CHOOSE A DIFFERENT PATH` → navigates to **Avatar Select** (same destination — they may keep the same avatar or change)

### Full fresh flow on retry

`TRY AGAIN` does **not** restart just the encounter. It takes the player back to **Avatar Select** so they can:
1. Keep the same avatar or pick a new one
2. Tap through to Interest Select and keep or change their love interest
3. Begin the playthrough again from Scene 1

**Reset on retry:**
```js
STATE.round     = 1;
STATE.scene     = 1;
STATE.exchange  = 1;
STATE.trust     = 30;
STATE.spookUsed = false;
STATE.villain   = null;
// Do NOT reset STATE.player or STATE.interest —
// let the selection screens show their previous choices still highlighted
// so the player can quickly confirm and proceed, or change their mind
```

---

## Navigation Rules

- `goTo(screenId)` — hides all screens, shows target, resets `scrollTop = 0`
- Back navigation never loses state (avatar selection persists when going back from bio)
- Bio screen stores `bioContext` ('avatar' or 'interest') to know what CTA to show and where to return
- Bio nav arrows wrap around (last → first)
- In interest context, bio arrows skip the avatar character
- **Never auto-navigate** from the encounter screen to any result screen — always wait for player to tap Continue
- **Never auto-navigate** from encounter to the next scene — always wait for player to tap Continue
- `TRY AGAIN` from fail result → `goTo('s-avatar')` with previous `STATE.player` and `STATE.interest` still set, so cards show as pre-selected

---

## What NOT to Build in Round 1

- No Claude API / free-text input (Round 2)
- No multi-love-interest parallel tracking (Round 2)
- No landscape layout
- No sound / music
- No save state / localStorage (offline file, no persistence needed)
- No animation between screens (simple opacity fade is enough)
- No backend of any kind

---

## File Output

Single file: `affections_of_vissan.html`

Must work by:
1. Double-clicking / opening directly in Safari on iPad/iPhone
2. No internet connection after initial load (fonts will fall back gracefully)
3. No server required

Target file size: under 8MB (current baseline ~7MB with 4 characters + 4 backgrounds embedded).

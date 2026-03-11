# CLAUDE.md — Affections of Vissan
> Game development specification for Claude Code.  
> Read this entire file before writing any code.

---

## What This Is

A mobile-first visual novel / dating sim set in the vampire kingdom of **Vissan**. The player selects an avatar character and pursues a love interest through 3 acts of story encounters. Each act has 3 scenes. Each scene has dialogue exchanges and narration beats. The goal is emotional progression — accumulate enough affection points across all 3 acts to win a sign of affection.

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
- Their act progress pip colour
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
  └─► [ENTER VISSAN] → How to Play Screen
        └─► [BEGIN] → Avatar Select
              └─► (tap card) Bio Screen [browsable ← →]
                    └─► [PLAY AS X] → back to Avatar Select (selected)
              └─► [CHOOSE WHO TO PURSUE] → Interest Select
                    └─► (tap card) Bio Screen [browsable ← →, excludes avatar]
                          └─► [PURSUE X] → back to Interest Select (selected)
                    └─► [BEGIN THE STORY] → Encounter (Act 1)
                          │
                          │  Within Encounter:
                          │  Scene 1 → [CONTINUE →] → Scene 2
                          │  Scene 2 → [CONTINUE →] → Scene 3
                          │  Scene 3 resolves:
                          │    ├─► Reaction renders fully in dialogue
                          │    │   Player reads it, then taps [CONTINUE →]
                          │    └─► → Act Result Screen (shows score + tier)
                          │              └─► [CONTINUE →] → Next Act
                          │
                          └─► Act 2 → Act 3 → Final Ending Screen
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

### Buttons
Dark background, `1px` border (`--border-hi`), `border-radius: 6px`, `Cinzel` font, `letter-spacing: .42em`, all-caps. Hover: border brightens to `--gold`, subtle gold background tint.

### Cards
`border-radius: 8px`, thin gold/cream border, `overflow: hidden`. Portrait images: `object-fit: cover`, `object-position: top center`.

---

## Screen Specifications

### 1. Landing Screen
- **Layout:** Scrollable single column, `background: #181818`
- **Title:** `AFFECTIONS OF VISSAN` — `Cinzel Decorative`, large (clamp ~2rem–2.8rem), gold, centered, ALL CAPS
- **Image:** Full-width world panorama image (aspect ratio ~390:280), no border radius, edge to edge
- **Below image (dark bg):**
  - `AN AI-DRIVEN VISUAL NOVEL` — `Cinzel`, spaced caps, gold, centered
  - Body lore paragraphs — centered, cream-dim
  - Italic tagline in gold: *Some doors should not be opened carelessly.*
  - `ENTER VISSAN` button — centered, at bottom

### 2. How to Play Screen (NEW)

Appears after tapping `ENTER VISSAN`. A single screen with rules and tone before the player commits.

**Layout:** Dark background, centered column, scrollable.

**Heading:** `HOW TO PLAY` — `Cinzel Decorative`, gold

**Copy:**

> In Vissan, any character can become your story — or your challenge.
>
> Choose who you play as. Choose who you pursue. Study them carefully: their words, their silences, their reactions.
>
> Every character holds secrets. Every answer you give shapes how they see you. Choose wisely — or discover what happens when you don't.
>
> The story unfolds across **three acts**. In each act, you'll face three choices. Each response earns points based on how well it reads your love interest.
>
> **Score 10 or more points out of 18 to win their sign of affection.**
>
> Fall short and you may still leave with something — just not what you hoped for.

**Affection Meter explainer (visual row + label):**

Show a small mock barometer and explain its states:

> Watch the affection meter closely. It reveals their emotional state in real time — but not their point total. Trust your instincts.

**Button:** `I'M READY →` → Avatar Select

### 3. Avatar Select Screen
- **Hero image** at top (~52vw height, max 260px), fades to `#181818` at bottom via gradient overlay
- **Heading:** `Who Are You?` (`Cinzel Decorative`, gold) + subtitle `Step 1: Choose Your Character` (`Cinzel`, small caps, dim)
- **2×2 grid** of character cards, full-width, zero gap between cells
  - Each card: square aspect ratio, portrait photo fills card, gradient overlay bottom 60%
  - Character name at bottom center (`Cinzel`, cream)
  - Selected card: `2px solid #F0C95B` border + `YOU` badge top-right
  - Tap a card → selects it AND opens Bio screen (context: `avatar`)
- **CTA button** below grid: `CHOOSE WHO TO PURSUE →`

### 4. Interest Select Screen
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

### 5. Bio Screen
- **Top nav bar:**
  - `← [PREV NAME]` button left
  - Character name (`Cinzel Decorative`, gold, centered) + subtitle below
  - `[NEXT NAME] →` button right
  - Arrows browse all 4 characters when context is `avatar`; browse 3 (excluding avatar) when context is `interest`
- **Portrait card:** fills width minus `28px` padding each side, aspect ratio `331:496`, `border-radius: 8px`, gold border `1.5px`
- **Bio text:** centered, `Cormorant Garamond`, `1rem`, `line-height: 1.82`, cream-dim
- **CTA button:** `PLAY AS [NAME]` (avatar context) or `PURSUE [NAME]` (interest context) — centered, bottom

### 6. Encounter Screen
- **Portrait strip** — top 40vh, min 220px
  - Full-bleed character image, `object-position: top center`
  - Gradient overlay: transparent → `rgba(24,24,24,.96)` at bottom
  - **Bottom-left overlay:**
    - Small circular avatar (36×36px, gold border) — shows love interest portrait
    - Act label (e.g. `Act I · First Impressions`) — `Cinzel`, tiny, dim gold
    - Character name — `Cinzel Decorative`, character colour
    - **Progress pips row** (see Pip spec below)
  - **Bottom-right overlay:** Affection Meter (see Affection Meter spec below)
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
  - **4 choice buttons** (italic `Cormorant Garamond`, rounded border) — see Scoring System
  - Continue button (appears after response resolves, replaces choices)

### 7. Result Screen (Per Act)
- **Title** — `Cinzel Decorative`, large, gold: reflects tier earned this act
- **Scene block:**
  - Full-width background landscape image (300px tall), `brightness(.72)`
  - Character portrait centered over it — 48% width, square, rounded, cream border
- **Affection score this act:** shown as `X / 6` — small, gold
- **Running total:** shown as `X / 18` — small, cream-dim
- **Tier label:** warm descriptor based on score (see Ending Tiers)
- **Body:** Short narrative beat in character's voice — reacts to the score tier
- **CTA:** `CONTINUE →` to next act, or final ending screen after Act 3

---

## Progress Pips

The pip row shows all dialogue exchanges across all 3 scenes of the current act.

- **Total pips = 9** (3 scenes × 3 exchanges each) displayed in a row
- Each pip: `22px wide × 3px tall`, `border-radius: 2px`
- Colours are **per-character** of the love interest:

| Character | Pip colour |
|---|---|
| Kohan | `#F0C95B` |
| Catarina | `#E8C080` |
| Andam | `#B8A898` |
| Max | `#A8C5DA` |
| Narrator | `rgba(240,201,91,.38)` |

- **Completed exchange:** full colour opacity
- **Current exchange:** full colour + glow `box-shadow: 0 0 5px [colour]`
- **Future exchange:** `opacity: 0.35`

---

## Affection Meter

Shows the love interest's current emotional state. Located bottom-right of portrait strip.

- Label: `AFFECTION` (`Cinzel`, tiny, dim gold)
- Track: `90px × 4px`, dark background, thin gold border
- Fill: gradient left→right `#7a1020 → #C9A84C → #F0D080`
- Arrow indicator: small triangle at fill right edge
- Mood label below: italic `Cormorant Garamond`, dim gold

### Mood Labels — Per Act

Labels evolve in tone across all three acts to reflect emotional depth.

**Act 1 — First Impressions (curiosity/interest)**

| Fill % | Going Up | Going Down |
|---|---|---|
| 0–20 | — | Bored |
| 21–35 | Neutral | Dismissive |
| 36–50 | Intrigued | Unmoved |
| 51–65 | Engaged | Neutral |
| 66–80 | Engaged | — |
| 81–100 | Captivated | — |

**Act 2 — Rival Entrance (trust/respect)**

| Fill % | Going Up | Going Down |
|---|---|---|
| 0–20 | — | Closed |
| 21–35 | Watchful | Guarded |
| 36–50 | Interested | Skeptical |
| 51–65 | Trusting | Watchful |
| 66–80 | Trusting | — |
| 81–100 | Allied | — |

**Act 3 — The Move (desire/connection)**

| Fill % | Going Up | Going Down |
|---|---|---|
| 0–20 | — | Gone |
| 21–35 | Aware | Cold |
| 36–50 | Drawn | Retreating |
| 51–65 | Wanting | Aware |
| 66–80 | Wanting | — |
| 81–100 | Yours | — |

> The meter reflects emotional temperature only. It does not show the player's point total — that is revealed at the end of each act.

- Starts at `30` (mid-range) at the start of each act
- Updates smoothly after each exchange (CSS transition)

---

## Scoring System

### Structure

Each exchange has **4 preset answer choices**. Points are awarded based on how well the answer reads the love interest.

| Choice type | Points |
|---|---|
| Perfect read | **2 pts** |
| Decent read | **1 pt** |
| Decent read | **1 pt** |
| Miss | **0 pts** |

- Each act has **3 exchanges** = **6 pts max per act**
- 3 acts × 6 = **18 pts max total**
- **Win threshold: 10 / 18**

### Ending Tiers (cumulative after Act 3)

| Total Score | Tier | Description |
|---|---|---|
| 0–4 | **Loose** | They noticed you. That's all. |
| 5–9 | **Friend Zone** | Something was there — just not enough. |
| 10–18 | **Sign of Affection** | They're yours, in whatever way they know how. |

### Which Answer Scores Best — Per Act, Per Character

The "perfect" answer type rotates per act so players must re-read their love interest rather than rely on a fixed strategy.

**Act 1 — First Impressions**

| Character | 2 pts | 1 pt | 1 pt | 0 pts |
|---|---|---|---|---|
| Kohan | Curiosity | Honesty | Deflection | Strategy |
| Catarina | Strategy | Deflection | Honesty | Curiosity |
| Max | Honesty | Curiosity | Strategy | Deflection |
| Andam | Deflection | Strategy | Curiosity | Honesty |

**Act 2 — Rival Entrance**

| Character | 2 pts | 1 pt | 1 pt | 0 pts |
|---|---|---|---|---|
| Kohan | Strategy | Honesty | Curiosity | Deflection |
| Catarina | Honesty | Strategy | Deflection | Curiosity |
| Max | Deflection | Honesty | Curiosity | Strategy |
| Andam | Curiosity | Deflection | Strategy | Honesty |

**Act 3 — The Move**

| Character | 2 pts | 1 pt | 1 pt | 0 pts |
|---|---|---|---|---|
| Kohan | Honesty | Curiosity | Strategy | Deflection |
| Catarina | Curiosity | Honesty | Strategy | Deflection |
| Max | Honesty | Curiosity | Deflection | Strategy |
| Andam | Curiosity | Honesty | Deflection | Strategy |

> **Note:** Deflection is never rewarded in Act 3. By the final act, all characters want authenticity.

---

## Dialogue Copy — All Acts, All Characters

All exchanges follow the same structure:
- Narrator or character line sets the scene
- Love interest speaks or acts
- Player sees prompt: `HOW WOULD YOU ANSWER?`
- 4 labelled choices appear (no trait label shown to player — just the text)
- Love interest reacts based on chosen trait type

---

### KOHAN — The Fire Witch

**Kohan's personality:** Volatile, curious, warm beneath the armor. She tests people before she trusts them. She notices everything. She respects directness and punishes evasion.

---

#### ACT 1 — First Impressions · Human Village

**Scene 1 — Opening**

*Narrator: The village market hums with cautious life. You spot her before she spots you — a woman with ember eyes and a cloak that smells faintly of smoke.*

**Kohan:** "You're staring. Most people know better."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Kohan's Reaction |
|---|---|---|
| Curiosity ⭐ | "I've never seen someone move like that through a crowd. Like everything parts for you." | Her eyes flick to yours. "…Most things do." A pause. The corner of her mouth moves — almost. |
| Honesty | "I was. You're not easy to ignore." | She tilts her head. "Honest. Good. Flattery I can smell." |
| Deflection | "I was looking at the stall behind you." | She glances back, then at you. "You're a bad liar." |
| Strategy | "I wanted to see if you'd notice." | A short exhale — not quite a laugh. "Everyone wants to test me. Try something original." |

---

**Scene 2 — Villain Entrance**

*Narrator: Someone steps between you — Andam, or Max, or Catarina (villain). Their arrival is too smooth to be accidental.*

**[Villain]:** "You know who you're talking to, I assume."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Kohan's Reaction |
|---|---|---|
| Strategy ⭐ | *(to Kohan, ignoring the villain)* "Do they always announce themselves like that?" | A flicker of something — appreciation. "Only when they feel overlooked." She doesn't look at the villain. |
| Honesty | "I do. And I chose to introduce myself anyway." | She watches you carefully. "That either makes you brave or foolish." |
| Curiosity | "Should I know them? What's the history?" | She narrows her eyes — not at you, at the question. "There's always a history. What matters is what you do with it." |
| Deflection | *(stepping aside)* "I'll leave you two to it." | Something closes in her expression. "Of course you will." |

---

**Scene 3 — Aftermath**

*Narrator: The villain retreats. The air between you feels lighter — or heavier. Kohan looks at the fire in the pit nearby, as if deciding something.*

**Kohan:** "Why are you still here?"

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Kohan's Reaction |
|---|---|---|
| Curiosity ⭐ | "Because you haven't bored me yet. And I don't think you're done." | She looks at you fully for the first time. A long beat. "...You're strange." But she doesn't leave. |
| Honesty | "Because I wanted to. I stopped needing reasons for things that feel right." | A quiet breath. "That's either very free or very careless." But she stays. |
| Deflection | "Nowhere else to be, I suppose." | "That's a terrible reason." She turns to go. |
| Strategy | "I thought it might be useful to know you." | "Useful." Flat. "Go find something useful somewhere else." |

---

#### ACT 2 — Rival Entrance · Human Village (later that evening)

**Scene 1 — Opening**

*Narrator: She finds you near the edge of the market. You wonder if she was looking, or if she'd never admit to it.*

**Kohan:** "You didn't leave."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Kohan's Reaction |
|---|---|---|
| Strategy ⭐ | "I figured you'd come back this way. The fire pit's the warmest spot." | A slow look. "You paid attention." She sits near you — not close, but chosen. |
| Honesty | "I said I wanted to stay. I meant it." | She's quiet. Then: "People say a lot of things near fire." But she doesn't leave. |
| Curiosity | "I wanted to see if you would." | "So I'm an experiment." A warning edge. "That's a dangerous game." |
| Deflection | "Just resting. Don't read into it." | She stands. "I wasn't." She moves two feet further away. |

---

**Scene 2 — Rival Entrance**

*Narrator: The villain appears again — this time with something to prove. They speak to Kohan, not you.*

**[Villain]:** *(to Kohan)* "You're spending time with outsiders now? That's new."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Kohan's Reaction |
|---|---|---|
| Strategy ⭐ | *(quietly, to Kohan only)* "You don't have to respond to that." | The slightest pause. Then she looks at the villain. "No. I don't." Something shifts — she's standing closer to you now. |
| Honesty | "I'm right here. Address me directly." | She glances at you — something surprised. "They're not wrong to say it," she says, "but they shouldn't have." |
| Curiosity | "Is this what passes for conversation in Vissan?" | A short breath — almost a laugh. "Sometimes." She looks at you sideways. |
| Deflection | "I should probably go." | Her jaw tightens. "Yes. Probably." |

---

**Scene 3 — Aftermath**

*Narrator: The rival is gone. Kohan stares into the fire. You have one last moment before the night closes.*

**Kohan:** "You handled that better than most would."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Kohan's Reaction |
|---|---|---|
| Honesty ⭐ | "I wasn't performing. I just said what I meant." | She looks at you for a long time. "That's rare here." Her hand brushes yours — not quite accidental. |
| Strategy | "I've learned that some battles aren't worth fighting in public." | "Careful," she says. But it sounds like a compliment. |
| Curiosity | "What would most do?" | "Back down. Posture. Leave." A pause. "You did none of those." |
| Deflection | "I wasn't really paying attention to them." | "Mm." She turns back to the fire. The moment closes. |

---

#### ACT 3 — The Move · Human Village (night)

**Scene 1 — Opening**

*Narrator: The village is quiet. She's still here. So are you. Whatever this has been building toward — it's close now.*

**Kohan:** "You're not afraid of me."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Kohan's Reaction |
|---|---|---|
| Honesty ⭐ | "No. I think I understand you better than you expect." | She goes very still. "...That's either true or the most convincing lie I've heard." But her eyes don't move from yours. |
| Curiosity | "Should I be?" | "Yes." A pause. "Most are." But something in her expression — softens. Just slightly. |
| Strategy | "Fear doesn't help me get what I want." | "And what do you want?" She steps closer. |
| Deflection | "I don't think about it that way." | "You should." She steps back. The distance returns. |

---

**Scene 2 — Villain Entrance**

*Narrator: The rival appears one final time — perhaps sensing what's happening between you.*

**[Villain]:** "This is a mistake. Both of you know it."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Kohan's Reaction |
|---|---|---|
| Honesty ⭐ | "Maybe. I'm making it anyway." | She exhales. Something breaks open in her expression — not quite a smile, not quite surrender. "...Idiot," she says, quietly. Like it means something else. |
| Curiosity | "What makes you so sure?" | Kohan: "Don't." Quiet. Firm. To you, not the villain. Then: "They don't get a vote." |
| Strategy | *(to the villain)* "You've said your piece." | She watches you handle it. Nods, once. "Enough," she tells the villain. They go. |
| Deflection | "They might be right." | Her expression closes. "Then you should listen to them." She steps away. |

---

**Scene 3 — The Move**

*Narrator: Just the two of you now. The fire has burned low. She's watching you like she's trying to memorize something.*

**Kohan:** "Say what you came here to say."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Kohan's Reaction |
|---|---|---|
| Honesty ⭐ | "I think you're unlike anyone I've met. And I don't want to walk away from that." | A long silence. The fire pops. Then she reaches out — takes your hand, just for a moment. "Don't make me regret this." *(Sign of affection — 2 pts)* |
| Curiosity | "I want to know more. I think there's a lot more to know." | "There is." She doesn't look away. "Whether you earn it is a different question." A long beat — then she steps closer. *(1 pt)* |
| Strategy | "I think we could be good for each other. Strategically." | "Strategically." She repeats it. Then, dryly: "At least you're honest about the wrong things." She doesn't leave. *(1 pt)* |
| Deflection | "I don't know. I just didn't want to go." | "That's not enough." She turns away. The fire dies. *(0 pts)* |

---

### CATARINA — The Vampire Princess

**Catarina's personality:** Poised, perceptive, and deeply lonely beneath a flawless exterior. She's been managed and manipulated her whole life. She values people who see past the performance — who treat her like a person, not a position.

---

#### ACT 1 — First Impressions · Vissan Palace

**Scene 1 — Opening**

*Narrator: The palace corridor is marble and shadow. She's standing at a window, looking out at a kingdom that was decided for her long before she was born.*

**Catarina:** *(not turning around)* "You're not supposed to be in this part of the palace."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Catarina's Reaction |
|---|---|---|
| Strategy ⭐ | "I know. I came anyway. I wanted to meet you without an introduction." | She turns. Studies you. "That's either very brave or very rude." A pause. "Possibly both." She doesn't call the guard. |
| Deflection | "I got lost. I'll find my way back." | She tilts her head. "Will you?" A strange smile. "The palace has a way of holding people." |
| Honesty | "I wanted to see you. Without the ceremony." | Something flickers in her eyes. "Without the ceremony," she repeats softly. "How novel." |
| Curiosity | "What do you see, from up there?" | She looks back out the window. "Too much. And never enough." She's quiet a moment. "What made you ask that?" |

---

**Scene 2 — Villain Entrance**

*Narrator: A palace official — the villain — materializes from the corridor. Their presence here is not an accident.*

**[Villain]:** "Your Highness. I wasn't aware you had company."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Catarina's Reaction |
|---|---|---|
| Strategy ⭐ | *(stepping forward, graciously)* "I was just introducing myself. My apologies for the informality." | She watches you take control of the moment. The smallest nod — approval. "Yes. An introduction. Nothing more." |
| Honesty | "I found her. We were talking." | She blinks. Then, quietly amused: "Direct. Dangerously so." |
| Deflection | *(stepping back)* "I'll leave the two of you." | Her expression doesn't change. But something dims. "Of course." |
| Curiosity | "Is it unusual for the Princess to have company?" | The villain stiffens. Catarina: "Yes," she says coolly. "Which is why I value it when it happens." |

---

**Scene 3 — Aftermath**

*Narrator: The official withdraws. The corridor is yours again — for now.*

**Catarina:** "You didn't flinch."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Catarina's Reaction |
|---|---|---|
| Deflection ⭐ | "It wasn't my place to." | She looks at you carefully. "Most people make everything their place." A breath. "Thank you." She reaches out — adjusts the lapel of your coat, a small deliberate gesture. |
| Strategy | "I thought it was better for you to lead." | "Thoughtful." But something retreats in her. "Everyone thinks about what's better for me." |
| Honesty | "I wasn't afraid of them." | "I know." Soft. "That's the thing about you." |
| Curiosity | "What usually happens when someone does?" | "Exile or apology." She smiles, barely. "You avoided both." |

---

#### ACT 2 — Rival Entrance · Vissan Palace (the gardens)

**Scene 1 — Opening**

*Narrator: She's in the palace garden now — alone, or almost. She looks surprised to see you, but not displeased.*

**Catarina:** "You found me again."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Catarina's Reaction |
|---|---|---|
| Honesty ⭐ | "I wanted to. I've been thinking about our conversation." | She's still. "So have I," she says, quietly. She moves aside on the bench — making room. |
| Curiosity | "Is this your usual spot? You seem at home here." | "It's the one place the palace feels smaller." A pause. "Sit. If you want." |
| Strategy | "I thought you might be here. The garden seemed like the most likely escape." | She raises an eyebrow. "You studied my movements?" A cool look. "That's either flattering or alarming." |
| Deflection | "Coincidence, mostly." | "Mm." She doesn't believe you. She also doesn't invite you to sit. |

---

**Scene 2 — Rival Entrance**

*Narrator: The villain arrives into the garden. They speak to Catarina as if you aren't there.*

**[Villain]:** "There are duties awaiting you, Your Highness. People are asking questions."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Catarina's Reaction |
|---|---|---|
| Honesty ⭐ | "I think the Princess is allowed to have an afternoon." | She looks at you — startled. Then something softens. "...Yes," she says. "I believe I am." She doesn't get up. |
| Strategy | *(neutrally)* "She'll return when she's ready, I'm sure." | She follows your lead. "I'll return when I'm ready." Said with more conviction than usual. |
| Deflection | "I should probably leave anyway." | Her composure holds, but her hands fold more tightly in her lap. "Of course." |
| Curiosity | "What questions?" | The villain stiffens. Catarina, quietly: "Don't give them more to work with." A private look at you — not quite a warning, not quite a plea. |

---

**Scene 3 — Aftermath**

*Narrator: The villain leaves. Catarina exhales — the first unguarded breath you've seen from her.*

**Catarina:** "Does it tire you? Being around people like that?"

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Catarina's Reaction |
|---|---|---|
| Strategy ⭐ | "I've learned to move around them. I focus on what I actually care about." | She looks at you. "And what do you care about?" A quieter question than it sounds. |
| Honesty | "Yes. But you seem used to it, and I imagine that's much harder." | She's quiet for a long moment. "You see a lot." Said like it surprises her. |
| Curiosity | "Do you ever just... tell them to leave?" | A real laugh — small and startled. "Not yet." Then: "Maybe soon." |
| Deflection | "I don't mind it." | "You're being kind." She turns back to the garden. The moment recedes. |

---

#### ACT 3 — The Move · Vissan Palace (the balcony, night)

**Scene 1 — Opening**

*Narrator: She's found you — or led you here, it's hard to tell which. The balcony overlooks all of Vissan. She is the most unguarded you've ever seen her.*

**Catarina:** "I don't usually bring people up here."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Catarina's Reaction |
|---|---|---|
| Curiosity ⭐ | "Why me, then?" | She considers it honestly. "I'm not entirely sure. Which is exactly why." She leans on the railing beside you. |
| Honesty | "I'm glad you did." | "So am I." Simply. She doesn't look away. |
| Strategy | "I'll consider it a privilege." | A small smile. "Don't be too formal. It breaks the spell." |
| Deflection | "I won't tell anyone." | Something flattens in her. "That's not why I brought you." |

---

**Scene 2 — Villain Entrance**

*Narrator: A door opens. The villain steps onto the balcony. The interruption is obviously unwelcome — even they seem to sense it.*

**[Villain]:** "I've been looking for you everywhere, Your Highness."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Catarina's Reaction |
|---|---|---|
| Curiosity ⭐ | *(to Catarina, warmly)* "Do you need a moment? I can wait." | She looks at you — something grateful, something decided. "No," she says. To the villain: "We're busy." The door closes. She turns back to you. "Thank you for asking." |
| Honesty | "Can this wait? We were in the middle of something." | She blinks. Then: "Yes. It can." She sounds like she's remembering how to say that. |
| Strategy | *(to the villain)* "The Princess will be with you shortly, I'm sure." | She follows, firmly: "Shortly. Yes." The door closes. |
| Deflection | "I should go. Give you space." | Quietly: "Please don't." She catches herself. Straightens. "If you don't mind staying." |

---

**Scene 3 — The Move**

*Narrator: The night is very still. She's watching the lights of Vissan below — or she was, until she looked at you instead.*

**Catarina:** "Tell me something true."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Catarina's Reaction |
|---|---|---|
| Honesty ⭐ | "I think you've spent your whole life being seen as a title. I see something else." | The silence that follows is different from all the others. She turns to you slowly. Then she takes your hand. Holds it. "Don't let go yet," she says. *(Sign of affection — 2 pts)* |
| Curiosity | "I want to know who you are when no one's performing. I think I've been getting glimpses." | Her expression shifts — something warm opens. "You might be right." She leans slightly toward you. *(1 pt)* |
| Strategy | "I think you're more powerful than anyone in that palace understands." | "Flattery." But she's smiling, just slightly. "Convincing flattery." *(1 pt)* |
| Deflection | "I'm not sure I know any truths tonight." | "That's a shame." She turns back to the lights below. The distance returns. *(0 pts)* |

---

### MAX — The Moon Elf

**Max's personality:** Gentle, ancient, precise. They speak slowly because they mean everything they say. They have seen too much to be easily impressed, but they are moved by sincerity and wounded by carelessness.

---

#### ACT 1 — First Impressions · Moon Elf Forest

**Scene 1 — Opening**

*Narrator: The forest breathes. You're not sure how long they've been watching you — but Max steps from between the trees as if they've decided, finally, that you deserve an introduction.*

**Max:** "You walk quietly. For a visitor."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Max's Reaction |
|---|---|---|
| Honesty ⭐ | "I was trying to. I didn't want to disturb anything." | A long pause. They seem to be weighing this. "Most visitors don't consider what they disturb." They step closer. |
| Curiosity | "Does this forest speak to you? I felt like it was listening." | They tilt their head. "It is. It always is." Something opens. "You felt that?" |
| Strategy | "I've learned that the quieter you are, the more you see." | "That is true." A pause. "Though it is only worth anything if you know what to look for." |
| Deflection | "I wasn't really thinking about it." | "Mm." They are still. "The forest notices." |

---

**Scene 2 — Villain Entrance**

*Narrator: Someone arrives into the clearing — the villain. They carry the energy of a disruption.*

**[Villain]:** "There you are, Max. I've been looking."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Max's Reaction |
|---|---|---|
| Curiosity ⭐ | *(to Max, gently)* "Is this someone you want to see?" | They look at you — something careful and warm. "A good question." To the villain: "Not at this moment, no." |
| Honesty | "We were in the middle of something." | Max, quietly: "We were." The simple agreement carries weight. |
| Deflection | "I'll give you both privacy." | They look at you. "That is not necessary." A beat. "Stay." |
| Strategy | *(to the villain, pleasantly)* "Max was just showing me the forest." | "...Yes," Max says, slowly. They accept it, but look at you with something unreadable after. |

---

**Scene 3 — Aftermath**

*Narrator: The forest resettles. Max is watching you the way light watches a still pond.*

**Max:** "You stayed."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Max's Reaction |
|---|---|---|
| Honesty ⭐ | "I wanted to. There's something here I haven't found anywhere else." | They are very still. Then: "You are the first to say that in a long time." Their hand rests briefly on a tree — and then on your shoulder. Just for a moment. |
| Curiosity | "I keep feeling like I'm only seeing the surface of this place. And of you." | "That feeling," they say, "is correct." Almost a smile. "Come back tomorrow." |
| Deflection | "I didn't have anywhere else to be." | "That is rarely the whole truth." They look away. |
| Strategy | "I thought it might help to make a good impression." | "With whom?" they ask. "Me? Or the forest?" A long pause. "The forest is harder to impress." |

---

#### ACT 2 — Rival Entrance · Moon Elf Forest (deeper in)

**Scene 1 — Opening**

*Narrator: They find you at the edge of a silver pool. You wonder how long they've been deciding to come.*

**Max:** "You returned."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Max's Reaction |
|---|---|---|
| Deflection ⭐ | "The forest made it easy to find my way back." | Something shifts in their expression — appreciative. "Yes," they say. "It does that, sometimes. For some." They sit near the pool. The invitation is implicit. |
| Honesty | "I said I would. I meant it." | "People say many things." A pause. "But here you are." They move to make space. |
| Curiosity | "I kept thinking about what you said. I had more questions." | "Questions," they repeat. A quiet warmth. "Good. Sit." |
| Strategy | "I thought it was worth continuing what we started." | They study you. "What do you think we started?" Not unkind — but precise. |

---

**Scene 2 — Rival Entrance**

*Narrator: The villain enters the forest — clumsy, loud. Max's stillness sharpens.*

**[Villain]:** *(to Max)* "You're wasting your time with this one."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Max's Reaction |
|---|---|---|
| Deflection ⭐ | *(quietly)* "You don't need to defend me." | They look at you. Long. "I know." Then, to the villain: "Leave." Said so quietly it carries the whole forest. |
| Curiosity | "Do you agree with them?" | To the villain: "No." To you — the same word, but different. Softer. |
| Honesty | "I'd rather let Max decide that." | "Yes," Max says. "I would also prefer that." A look at the villain. "You have your answer." |
| Strategy | *(to the villain)* "That seems like Max's decision to make." | They follow without hesitation. "It is." Quiet authority. |

---

**Scene 3 — Aftermath**

*Narrator: The forest exhales. Max is watching the water.*

**Max:** "You handled that with grace."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Max's Reaction |
|---|---|---|
| Honesty ⭐ | "I didn't want to make it harder for you than it needed to be." | The silence that follows is full. Then: "You are considerate in a way that feels uncommon." They reach over — touches the back of your hand. Briefly. Deliberately. |
| Curiosity | "Do things like that happen often?" | "Often enough." A pause. "Less, lately." They glance at you. |
| Deflection | "I wasn't really thinking. I just reacted." | "That," they say, "is often where the truth lives." |
| Strategy | "I thought de-escalation was the better path." | "It was." A pause. "Though I wonder if you felt it, or calculated it." |

---

#### ACT 3 — The Move · Moon Elf Forest (the silver pool, moonrise)

**Scene 1 — Opening**

*Narrator: The moon sits on the water. Max is here. The world outside the forest feels very far away.*

**Max:** "Do you feel it? What this place does to time?"

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Max's Reaction |
|---|---|---|
| Honesty ⭐ | "Yes. It slows down. Or I do. I'm not sure which." | They close their eyes briefly. "Both," they say. "That is the correct answer." They turn to face you fully. |
| Curiosity | "Tell me what it does to you." | "It reminds me what I am." A pause. "And sometimes — what I want." They look at you when they say it. |
| Strategy | "It makes it easier to think clearly." | "Clarity," they say slowly. "Yes. And sometimes — the opposite." A sideways look. |
| Deflection | "I try not to analyze it too much." | "Mm." They return to watching the water. |

---

**Scene 2 — Villain Entrance**

*Narrator: The villain appears at the tree line. They say nothing yet — they are simply present, like a problem that hasn't spoken yet.*

**[Villain]:** "This isn't your world. You don't belong here."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Max's Reaction |
|---|---|---|
| Honesty ⭐ | "Maybe not. But I'm here, and I'd like to stay." | Max stands. "Then stay." To the villain: "They are here because I want them here." Said once. That is all. |
| Curiosity | *(to Max)* "Do you agree with them?" | "No," they say. Simply. Then, to the villain: "You have your answer." |
| Strategy | "I'm not trying to belong. I'm trying to understand." | Max: "There is a difference." To you: "A meaningful one." |
| Deflection | "They might not be wrong." | Max goes very still. "They are wrong," they say quietly. "Don't agree with people who diminish you." |

---

**Scene 3 — The Move**

*Narrator: The villain is gone. The moon is full. Max is looking at you the way the forest looks at everything — like you've always been here.*

**Max:** "I have not let many people into this place."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Max's Reaction |
|---|---|---|
| Honesty ⭐ | "I know. I don't take that lightly." | "I know you don't." They move to you — slow, deliberate. They take your face in their hands. Look at you for a long time. Then press their forehead to yours. "Stay a little longer." *(Sign of affection — 2 pts)* |
| Curiosity | "Can I ask why me? Out of everyone who might have come through?" | "Because you listened," they say. "And you asked." They step closer. "Not many do both." *(1 pt)* |
| Deflection | "I haven't done anything special." | "You have," they say. "Without trying to. That is the thing about it." A small, tired warmth. *(1 pt)* |
| Strategy | "I've been trying to be worthy of it." | "Trying." They are quiet. "I know. And I am deciding if it is enough." They do not step closer. *(0 pts)* |

---

### ANDAM — The Vampire General

**Andam's personality:** Controlled, precise, privately tender. He is used to command and allergic to softness — but beneath the armor is someone who has never been allowed to want something for himself. He responds to strength, honesty, and people who don't need him to be anything other than what he is.

---

#### ACT 1 — First Impressions · Vissan Palace

**Scene 1 — Opening**

*Narrator: The throne room is empty save for him. He doesn't look up from the maps.*

**Andam:** "This room is restricted."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Andam's Reaction |
|---|---|---|
| Deflection ⭐ | "I wasn't aware. I'll leave." | He finally looks up. Studies you. "You don't seem lost." A pause. "Stay. For a moment." |
| Strategy | "I know. I came looking for you specifically." | His jaw tightens — but he doesn't dismiss you. "Then say what you came to say." |
| Honesty | "I wanted to see the room. And I wanted to see who used it." | A long look. "That's direct." He sets down the map. |
| Curiosity | "What are the maps of?" | He is quiet for a beat. "Every place I've had to defend." Something passes across his face. "Why?" |

---

**Scene 2 — Villain Entrance**

*Narrator: The villain enters — they carry the air of someone who thinks they have authority here.*

**[Villain]:** "General. You're needed. And this person shouldn't be here."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Andam's Reaction |
|---|---|---|
| Deflection ⭐ | *(stepping back)* "I'll get out of your way." | He looks at you — then the villain. "They're with me." Flat. Decisive. The villain goes. |
| Strategy | *(neutrally)* "I'll wait outside, if that's easier." | He shakes his head once. "No." To the villain: "Give me a moment." |
| Honesty | "I was invited. Effectively." | He almost smiles — it doesn't reach his face, but it reaches his eyes. "They were." |
| Curiosity | "What does 'needed' mean in a place like this?" | "It means someone wants something from me." He says it to you, not the villain. |

---

**Scene 3 — Aftermath**

*Narrator: The room is quiet again. He rolls the map back up. He hasn't asked you to leave.*

**Andam:** "Most people would have backed down."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Andam's Reaction |
|---|---|---|
| Deflection ⭐ | "I wasn't sure what to do. I followed your lead." | He looks at you — something shifts. "That's more self-aware than most." A pause. "Come back tomorrow, if you want." |
| Honesty | "I wasn't going to be dismissed for something I hadn't done wrong." | "Good." Said simply. Like a verdict. |
| Strategy | "I didn't think retreating would serve either of us." | "No," he says. "It wouldn't have." He's looking at you differently now. |
| Curiosity | "What usually happens to people who do?" | "They get what they accept." Flat. But he's watching you carefully. |

---

#### ACT 2 — Rival Entrance · Vissan Palace (the corridor)

**Scene 1 — Opening**

*Narrator: He stops when he sees you. He was not expecting you, but he doesn't look displeased.*

**Andam:** "You came back."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Andam's Reaction |
|---|---|---|
| Curiosity ⭐ | "I kept thinking about what you said. About the maps. About what you've had to defend." | He's still. Then: "Did you." Not a question. He glances away — then back. "Walk with me." |
| Honesty | "I said I might. I meant it." | "People say many things." But he falls into step beside you. |
| Strategy | "I thought it was worth seeing you again." | "Worth it." He turns the words over. "We'll see." But he doesn't leave. |
| Deflection | "I was in the area." | "You were not." Dry. "But fine." |

---

**Scene 2 — Rival Entrance**

*Narrator: The villain intercepts — placing themselves between you and Andam.*

**[Villain]:** *(to you)* "You're getting comfortable in places you don't belong."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Andam's Reaction |
|---|---|---|
| Curiosity ⭐ | *(calmly)* "Where do you think I belong?" | He watches you hold the moment. Then, to the villain: "That's enough." Something behind his eyes — assessment passed. |
| Honesty | "I belong where I'm welcomed. Andam, are you welcoming me?" | A pause. Then, to the villain: "They're with me." Final. |
| Strategy | *(to Andam)* "Is this person speaking for you?" | He looks at the villain. "No." Then to you: "Come." |
| Deflection | "They might have a point." | He frowns. Not at the villain — at you. "Don't concede ground you didn't lose." |

---

**Scene 3 — Aftermath**

*Narrator: You're alone in the corridor. He's watching you with the same precision he gives the maps.*

**Andam:** "You don't rattle easily."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Andam's Reaction |
|---|---|---|
| Honesty ⭐ | "I've had to learn when something's worth rattling over. That wasn't." | A long silence. Then: "That's a useful skill." He glances at your hand — then away. The almost-touch is deliberate. |
| Curiosity | "Is that a quality you look for?" | "It's a quality I respect." A pause. "Yes." |
| Strategy | "It wasn't in my interest to." | "Calculated composure," he says. "Effective. But I wonder what the unfiltered version looks like." |
| Deflection | "I wasn't paying that much attention." | "You were." He doesn't elaborate. The moment closes. |

---

#### ACT 3 — The Move · Vissan Palace (the outer wall, night)

**Scene 1 — Opening**

*Narrator: He found you, or you found each other — the wall overlooking Vissan at night, the city laid out like a map below.*

**Andam:** "I don't usually come here with anyone."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Andam's Reaction |
|---|---|---|
| Honesty ⭐ | "Why now? Why me?" | He looks out at the city. A long pause. "I'm not entirely certain. That's unusual." He turns. "I'm still deciding if it bothers me." |
| Curiosity | "What do you see when you look at it from here?" | "Responsibility." A beat. "And, tonight — something else." He doesn't name it. |
| Strategy | "A general who needs a high vantage point. Makes sense." | "Don't reduce it." Not harsh — direct. "That's not what this is." |
| Deflection | "I won't ask questions, then." | "You can ask." Quietly. "I may actually answer." |

---

**Scene 2 — Villain Entrance**

*Narrator: Footsteps on the wall behind you. The villain. Of course.*

**[Villain]:** "You've been distracted lately, General. It's noticeable."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Andam's Reaction |
|---|---|---|
| Honesty ⭐ | "He's allowed to be." | He looks at you — something startled, then settled. Then, to the villain: "You heard them." The villain goes. He's quiet a moment. "Thank you." Said like it costs something. |
| Curiosity | *(to Andam)* "Is that a problem for you? Being noticed?" | He considers it. "It's unusual." To the villain: "We're done." |
| Strategy | *(to the villain)* "The General's focus is his own concern." | He takes that, uses it. "Yes. It is." The villain retreats. |
| Deflection | "I'll head back. Give you privacy." | "Stay." Said quietly. Quickly. Like it surprised him too. |

---

**Scene 3 — The Move**

*Narrator: The villain is gone. The city hums below. He is the most still you have ever seen him — not the stillness of control. Something else.*

**Andam:** "Say something honest."

*HOW WOULD YOU ANSWER?*

| Trait | Choice Text | Andam's Reaction |
|---|---|---|
| Honesty ⭐ | "I think you carry a lot alone. I don't think you have to. Not tonight." | The silence that follows is different from his other silences. Then he reaches over — takes your hand. Holds it firmly. Doesn't let go. "One night," he says. "We'll see about the rest." *(Sign of affection — 2 pts)* |
| Curiosity | "I keep wondering what you want. For yourself. Not the city." | He inhales. "I'm not sure I know the answer." A pause. "But I find I want to." He steps closer. *(1 pt)* |
| Strategy | "I think you'd be a formidable person to be close to." | "Formidable." Flat. Then, dryly: "That's one word for it." But he doesn't move away. *(1 pt)* |
| Deflection | "I'm not sure I have anything honest left tonight." | "Then we've run out of time." He looks back at the city. The wall between you returns. *(0 pts)* |

---

## Win/Lose Ending Screens

### Final Score Tiers (after Act 3 — cumulative 0–18)

**0–4 pts — Loose**

> Title: *"Something Passed Between You"*
> Body: *"Not everything that starts becomes a story. But you were here, and they noticed. That matters — even if neither of you can say exactly how."*
> CTA: `TRY AGAIN`  |  `CHOOSE DIFFERENTLY`

**5–9 pts — Friend Zone**

> Title: *"Close, But Not Quite"*
> Body: *"There was something real between you — a thread, a warmth, a moment that almost became more. Maybe the timing was wrong. Maybe a different approach would change everything. There's only one way to find out."*
> CTA: `TRY AGAIN`  |  `CHOOSE DIFFERENTLY`

**10–18 pts — Sign of Affection** *(Win)*

> Title: *"Theirs"*  *(or character-specific variant — see below)*
> Body: character-specific (see below)
> CTA: `PLAY AGAIN`  |  `PURSUE ANOTHER`

**Character Win Endings:**

*Kohan:* "She doesn't say what she means, usually. But she took your hand — and held it. In Vissan, that is everything."

*Catarina:* "She has spent her whole life performing. What she gave you tonight was not a performance. Remember that."

*Max:* "Time moves differently in the forest. They asked you to stay a little longer. For them, that is a declaration."

*Andam:* "He has defended this city for longer than he can remember. Tonight, for the first time, he let someone stand beside him — rather than behind him."

---

## Spook Mechanic

If the player makes a bold move while affection points in the current act are below 2 (fewer than 2 points earned so far this act), the love interest **pulls back (Startled)**. The player gets **one recovery attempt**:
- Successful repair → affection partially restored, game continues to next scene
- Failed repair → act ends early, 0 points awarded for remaining exchanges

`spookUsed` flag tracks whether recovery chance has been used this act. Resets each act.

---

## Villain System

- Villain is **randomly selected** from the 2 remaining characters (not player, not interest)
- Villain appears in **Scene 2** of every act
- Villain has unique dialogue lines per combination (stored in `ACTS[act][scene].villain.lines[villainKey]`)
- Player response to villain influences affection meter mood (not direct points) — context cue only
- Same random villain persists across all 3 scenes of an act; re-randomised each act

---

## Continue Button — Rules

The `[CONTINUE →]` button is the **only** way to advance between scenes and between acts. Nothing ever auto-advances.

| Moment | Button label | Leads to |
|---|---|---|
| After Scene 1 resolves | `CONTINUE →` | Scene 2 opens |
| After Scene 2 resolves | `CONTINUE →` | Scene 3 opens |
| After Scene 3 resolves | `CONTINUE →` | Act Result Screen |
| After Act Result Screen | `CONTINUE →` | Next Act (or Final Ending) |

A scene is **resolved** when:
1. Player has tapped a choice
2. All choice buttons are disabled
3. Love interest's reaction line has fully rendered
4. Affection meter has updated

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

## State Object

```js
const STATE = {
  player:     null,   // character key
  interest:   null,   // character key
  villain:    null,   // character key (random, set per act)
  act:        1,      // 1–3
  scene:      1,      // 1–3
  exchange:   1,      // 1–3
  actScore:   0,      // 0–6 (current act)
  totalScore: 0,      // 0–18 (cumulative)
  spookUsed:  false,
  bioContext: null,   // 'avatar' | 'interest'
};
```

---

## GAME_DATA Structure

```js
const GAME_DATA = {
  characters: { kohan: {...}, andam: {...}, catarina: {...}, max: {...} },
  acts: {
    1: {
      scenes: {
        1: { label, open, exchanges: [ { who, text, choices: [{tag, trait, text, reply, mood, points}] } ] },
        2: { villain scene structure },
        3: { resolution scene structure }
      }
    },
    2: { ... },
    3: { ... }
  },
  traitPoints: {
    // points per trait per character per act — see Scoring System tables
    1: { kohan: { Curiosity: 2, Honesty: 1, Deflection: 1, Strategy: 0 }, ... },
    2: { ... },
    3: { ... }
  }
};
```

---

## Starting Locations

| Love Interest | Location | Background image key |
|---|---|---|
| Kohan | Human Village | `bg_village` |
| Max | Moon Elf Forest | `bg_forest` |
| Catarina | Vissan Palace | `bg_castle` |
| Andam | Vissan Palace | `bg_castle` |

---

## Asset System

All images stored as base64 strings in `const ASSETS = {}`:

```js
const ASSETS = {
  kohan:      'data:image/png;base64,...',
  andam:      'data:image/png;base64,...',
  catarina:   'data:image/png;base64,...',
  max:        'data:image/png;base64,...',
  bg_village: 'data:image/png;base64,...',
  bg_forest:  'data:image/png;base64,...',
  bg_castle:  'data:image/png;base64,...',
  bg_world:   'data:image/png;base64,...',
};

function getCharImg(key, act) {
  return ASSETS[key + '_a' + act] || ASSETS[key];
}
```

---

## Navigation Rules

- `goTo(screenId)` — hides all screens, shows target, resets `scrollTop = 0`
- Back navigation never loses state
- Bio screen stores `bioContext` ('avatar' or 'interest') to know what CTA to show
- Bio nav arrows wrap around; skip avatar character in interest context
- **Never auto-navigate** from encounter to result screen — always wait for player to tap Continue
- `TRY AGAIN` from ending → `goTo('s-avatar')` with previous selections still set

---

## Code Architecture

Single HTML file. Organised:

```
1. <head>  — meta, Google Fonts link, <style> block
2. <body>  — all screen divs (display:none except active)
3. <script>
   ├── ASSETS object (base64 images)
   ├── GAME_DATA object (all dialogue, scenes, acts)
   ├── STATE object  (mutable game state)
   ├── UI helpers    (goTo, dlg, setChoices, showContinue, meter, pips)
   ├── Screen builders (buildInterestCards, buildBio, buildAvatarGrid)
   └── Game flow     (startAct, startScene, startExchange, handleChoice, endAct)
```

---

## What NOT to Build in Round 1

- No Claude API / free-text input (Round 2)
- No multi-love-interest parallel tracking (Round 2)
- No landscape layout
- No sound / music
- No save state / localStorage
- No animation between screens (simple opacity fade)
- No backend

---

## File Output

Single file: `affections_of_vissan.html`

Must work by double-clicking in Safari on iPad/iPhone. No internet required after load. No server required.

Target file size: under 8MB.

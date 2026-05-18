# ~ cerabellum ~
![image of software](https://file.garden/aGHX-XiW5xIQj3Jo/image_2026-05-18_182403082.png)

> *named after my beautiful wife c.c. from code geass.. does what lucien does but for code. (you would get this reference if you play blood†stained symphony wink wink.*

production tooling for **blood†stained symphony** — a code geass vampire au visual novel by lobster trilogy.

---

## what it does

cerabellum is a ren'py development tool built specifically for blood†stained symphony. it handles the repetitive technical work of visual novel production so you can focus on the writing and the art. This plugin is directed towards writers rather than technical programmers.

**cera script** — a plain-text scripting notation (`.ceras`) that converts to complete ren'py syntax. write your scenes in a readable human format. cerabellum handles the rest.

**states** — reads your `characters.yaml` config and generates ren'py `layeredimage` blocks and character defines automatically. add a state to the yaml, regenerate, done.

**visualise** — checks which sprite asset files actually exist on disk and which are still missing. your art production checklist, always up to date.

---

## the notation

cera script uses `\\` as its instruction prefix. everything else is content.

```
\\ ~ act 1 · standard deviation ~
\\ label: act_01_start
\\ scene: classroom_afternoon
\\ music: school_casual
\\ nvl

The warm afternoon light spread itself through the classroom.
But what is a line without direction?

\\ adv
lelouch:: school_bored center
l "Yes?"

\\ cg: cg02_act01_forest
\\ py: unlock_cg("cg02_act01_forest")
\\ break
\\ jump: act_01_hospital
```

full notation reference in `CERA_SCRIPT_REFERENCE.txt`.

---

## installation

requires python 3.10+ and pyyaml.

```bash
git clone https://github.com/Lobster-Trilogy/cerabellum
cd cerabellum
pip install -r requirements.txt
python main.py
```

---

## project structure

```
cerabellum/
├── main.py                       gui — tkinter, c.c.'s colour scheme
├── config.py                     yaml loading · State · Character · Config
├── encapsulator.py               generates ren'py layeredimage blocks
├── formatter.py                  converts cera script to ren'py syntax
├── visualiser.py                 checks sprite asset status
├── data/
│   ├── characters.yaml           character config — states, expressions, eyes
│   └── acts/                     your .ceras script files live here
├── output/                       generated .rpy files land here
├── requirements.txt
└── CERA_SCRIPT_REFERENCE.txt     complete notation guide
```

---

## characters.yaml

characters are defined in yaml with their sprite layers, states, and flags.

```yaml
characters:

  lelouch:
    display_name: "Lelouch Lamperouge"
    shorthand: "l"
    colour: "#8B0000"
    flower: "spider_lily"
    side_image: true              # side image characters hide automatically ♡

    defaults:
      position: center
      transition: t_default
      base: school_uniform
      eyes: contacts

    bases:
      school_uniform: "lelouch/base_school"
      mansion_casual: "lelouch/base_mansion"

    expressions:
      neutral:      "lelouch/expr_neutral"
      sharp:        "lelouch/expr_sharp"
      soft:         "lelouch/expr_soft"

    eyes:
      contacts:     "lelouch/eyes_contacts"
      vampire:      "lelouch/eyes_vampire"

    states:
      school_neutral:
        base: school_uniform
        expression: neutral
        eyes: contacts
      mansion_soft:
        base: mansion_casual
        expression: soft
        eyes: vampire
        note: "c.c. and nunnally specific ♡"
```

---

## side image system

characters with `side_image: true` in their config use ren'py's side image system — their portrait appears automatically when they speak and disappears when someone else does. no explicit `\\ hide:` calls needed.

```
lelouch:: school_bored center
l "Yes?"

te "Can you answer the question?"       ← lelouch's portrait hides automatically

lelouch:: school_bored_ec center
l "x equals one.."                      ← reappears when he speaks again
```

to temporarily show a side image character as a full sprite:

```
\\ py: renpy.hide_side_image()
cc:: sovereign_neutral left t_weighted

c "The line has direction."

\\ hide: cc
\\ py: renpy.show_side_image()
```

---

## complete notation reference

| notation | output |
|---|---|
| `\\ nvl` | switch to NVL mode |
| `\\ adv` | switch to ADV mode |
| `\\ scene: name` | background change |
| `\\ music: name` | music change with fadein |
| `\\ sfx: name` | sound effect |
| `\\ cg: name` | show CG image |
| `\\ hide: name` | hide sprite or CG |
| `\\ clear` | hide all sprites |
| `\\ break` | fade to black |
| `\\ label: name` | define ren'py label |
| `\\ jump: name` | jump to label |
| `\\ call: name` | call label (returns after) |
| `\\ py: command` | raw ren'py / python passthrough |
| `\\ ~ note ~` | human comment — ignored by formatter |
| `character:: state` | show sprite at last known position |
| `character:: state left` | show sprite at position |
| `character:: state left t_weighted` | show sprite with transition |
| `x "dialogue"` | attributed dialogue |
| `"unattributed"` | unattributed speech |
| plain text | NVL narrator line |

---

## roadmap

**v1.0** — current. cera script compiler · encapsulator · visualiser · gui.

**v1.1** — in-app cera script editor with syntax highlighting. write directly in cerabellum without a separate text editor.

**v2.0** — visual compose mode. build layered image states graphically, preview sprite combinations, write directly to yaml. requires pillow.

---

## built by

**lobster trilogy**
lead: [Mari](https://x.com/crinternet_)
composer: [Rei](https://x.com/blockie_mc)
additional writing: [Lorik](https://x.com/lorikubeast)

blood†stained symphony is a code geass fan work.
code geass © sunrise. no commercial use.

---

*~ What's a line without direction? ~*

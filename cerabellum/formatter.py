import os
import re


def classify_line(line):
    stripped = line.strip()

    if stripped == "":
        return "blank"

    if stripped.startswith("\\\\ note:") or stripped.startswith("\\\\ ~"):
        return "comment"
    if stripped.startswith("#"):
        return "comment"

    if stripped == "\\\\ nvl":
        return "nvl"

    if stripped.startswith("\\\\ nvl hide"):
        return "nvl_hide"

    if stripped.startswith("\\\\ nvl show"):
        return "nvl_show"
    if stripped == "\\\\ adv":
        return "adv"

    if stripped.startswith("\\\\ scene:"):
        return "scene"
    if stripped.startswith("\\\\ music:"):
        return "music"
    if stripped.startswith("\\\\ sfx:"):
        return "sfx"
    if stripped.startswith("\\\\ cg:"):
        return "cg"
    if stripped.startswith("\\\\ hide:"):
        return "hide"
    if stripped == "\\\\ clear":
        return "clear"
    if stripped == "\\\\ break":
        return "break"
    if stripped.startswith("\\\\ label:"):
        return "label"
    if stripped.startswith("\\\\ jump:"):
        return "jump"
    if stripped.startswith("\\\\ call:"):
        return "call"
        
    if stripped.startswith("\\\\ py:"):
        return "py"
    if stripped.startswith("\\\\ screen:"):
        return "screen"

    if stripped.startswith("\\\\ hidescreen:"):
        return "hidescreen"

    if "::" in stripped:
        return "sprite"

    # Attributed dialogue — shorthand prefix + quoted text
    # covers l, s, te, sh, ni, etc.
    if re.match(r'^[a-z_]{1,6}\s+"', stripped):
        return "dialogue"

    # Unattributed speech — line starts with a quote
    # distinct from narrator prose — renders as spoken text
    if stripped.startswith('"'):
        return "unattributed"

    # Everything else is narrator prose
    return "narrator"


def convert_line(line, line_type, state, config=None):
    stripped = line.strip()

    if line_type == "blank":
        return ""

    if line_type == "comment":
        return ""

    if line_type == "nvl":
        state["mode"] = "nvl"
        return "nvl clear\nwindow hide"
    
    if line_type == "nvl_hide":
        # check for optional transition parameter
        parts = stripped.replace("\\\\ nvl hide", "").strip()
        if parts:
            return f"nvl hide {parts}"
        return "nvl hide"

    if line_type == "nvl_show":
        parts = stripped.replace("\\\\ nvl show", "").strip()
        if parts:
            return f"nvl show {parts}"
        return "nvl show"

    if line_type == "adv":
        state["mode"] = "adv"
        return "window show"

    if line_type == "scene":
        name = stripped.replace("\\\\ scene:", "").strip()
        return f"scene {name} with t_default"

    if line_type == "music":
        name = stripped.replace("\\\\ music:", "").strip()
        return f"$ renpy.music.play('audio/music/{name}.ogg', fadein=1.0)"

    if line_type == "sfx":
        name = stripped.replace("\\\\ sfx:", "").strip()
        return f"$ renpy.sound.play('audio/sfx/{name}.ogg')"

    if line_type == "cg":
        name = stripped.replace("\\\\ cg:", "").strip()
        return f"show {name}"

    if line_type == "hide":
        name = stripped.replace("\\\\ hide:", "").strip()
        if config is not None and config.is_side_image(name):
            return ""
        return f"hide {name}"

    if line_type == "clear":
        return "hide screen sprites"

    if line_type == "break":
        return "scene black with Dissolve(1.0)\npause 0.5"

    if line_type == "label":
        name = stripped.replace("\\\\ label:", "").strip()
        return f"label {name}:"

    if line_type == "jump":
        name = stripped.replace("\\\\ jump:", "").strip()
        return f"jump {name}"

    if line_type == "call":
        name = stripped.replace("\\\\ call:", "").strip()
        return f"call {name}"
    
    if line_type == "screen":
        name = stripped.replace("\\\\ screen:", "").strip()
        return f"show screen {name}"

    if line_type == "hidescreen":
        name = stripped.replace("\\\\ hidescreen:", "").strip()
        return f"hide screen {name}"
    
    
    
    
    if line_type == "py":
        command = stripped.replace("\\\\ py:", "").strip()
        return f"$ {command}"

    if line_type == "sprite":
        parts = stripped.split("::")
        char_id = parts[0].strip()
        rest = parts[1].strip().split()
        state_name = rest[0]

        # no position specified — state update only
        # used for side image characters
        if len(rest) == 1:
            return f"show {char_id} {state_name}"

        # position specified — full sprite on background
        position = rest[1]
        state["positions"][char_id] = position
        transition = rest[2] if len(rest) > 2 and rest[2].startswith("t_") else "t_default"
        return f"show {char_id} {state_name} at {position} with {transition}"

    if line_type == "dialogue":
        return stripped

    if line_type == "unattributed":
        # Pass through unchanged in both modes.
        # In ADV mode renders via adv_narrator character defined in game.
        # In NVL mode renders as unattributed speech in the NVL window.
        return f'adv_narrator {stripped}'

    if line_type == "narrator":
        # NVL: handled by the buffer in format_script — this branch
        # is only reached if called directly outside format_script.
        # ADV: short stage direction, one line at a time.
        return f'narrator "{stripped}"'

    return ""


def format_script(input_path, output_path, config=None):
    """
    Converts a .ceras or .md Cera Script file to .rpy Ren'Py output.

    Every narrator line is its own narrator call — line breaks in the
    source file directly control pacing. The writer decides where to
    break by where they put line breaks.

    Unattributed speech passes through unchanged in both modes.
    """
    state = {
        "mode": "nvl",
        "positions": {}
    }

    output_lines = []
    output_lines.append("## ~ generated by cerabellum ~ do not edit manually please <3")
    output_lines.append("")

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            line_type = classify_line(line)
            converted = convert_line(line, line_type, state, config)
            if converted:
                output_lines.append(converted)

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print(f"~ cerabellum ~ formatted: {output_path}")


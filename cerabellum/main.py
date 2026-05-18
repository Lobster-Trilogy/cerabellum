import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import re 

# ~ c.c. palette ~
BG      = "#FBFFFD"
PANEL   = "#EDE8DC"
GREEN   = "#E2F0B5"
PINK    = "#D4A0A0"
TEXT    = "#2A2A1E"
DIM     = "#8A8A7A"

window = tk.Tk()
window.title("~ cerabellum ~")
window.geometry("1024x768")
window.configure(bg=BG)

# ── header ────────────────────────────────────
header = tk.Frame(window, bg=BG)
header.pack(fill="x", padx=20, pady=(20, 10))

window.iconbitmap("favicon.ico") 

title = tk.Label(
    header,
    text="~ cerabellum ~",
    bg=BG,
    fg=PINK,
    font=("Georgia", 18, "bold")
)
title.pack(side="left")

subtitle = tk.Label(
    header,
    text="~ cera script · states · visualise ~",
    bg=BG,
    fg=DIM,
    font=("Georgia", 10)
)
subtitle.pack(side="left", padx=(8, 0))

divider = tk.Frame(window, bg="#D4A0A0", height=2)
divider.pack(fill="x", padx=20, pady=(0, 16))

# ── mode row ──────────────────────────────────
mode_row = tk.Frame(window, bg=BG)
mode_row.pack(fill="x", padx=20, pady=(0, 12))

tk.Label(
    mode_row,
    text="mode",
    bg=BG,
    fg=DIM,
    font=("Georgia", 10)
).pack(side="left", padx=(0, 8))

mode_var = tk.StringVar(value="cera script")

mode_dropdown = ttk.Combobox(
    mode_row,
    textvariable=mode_var,
    values=["cera script", "states", "visualise"],
    state="readonly",
    width=20,
    font=("Georgia", 10)
)
mode_dropdown.pack(side="left")

# ── browse functions ───────────────────────────
input_var  = tk.StringVar()
output_var = tk.StringVar()
yaml_var   = tk.StringVar()
images_var = tk.StringVar()

def browse_input():
    path = filedialog.askopenfilename(
        filetypes=[
            ("Cera Script", "*.ceras"),
            ("Markdown", "*.md"),
            ("All files", "*.*")
        ]
    )
    if path:
        input_var.set(path)

def browse_output():
    path = filedialog.asksaveasfilename(
        defaultextension=".rpy",
        filetypes=[("Ren'Py Script", "*.rpy"), ("All files", "*.*")]
    )
    if path:
        output_var.set(path)

def browse_yaml():
    path = filedialog.askopenfilename(
        filetypes=[("YAML", "*.yaml *.yml"), ("All files", "*.*")]
    )
    if path:
        yaml_var.set(path)

def browse_images():
    path = filedialog.askdirectory()
    if path:
        images_var.set(path)

# ── cera script panel ─────────────────────────
cera_panel = tk.Frame(window, bg=BG)

input_row = tk.Frame(cera_panel, bg=BG)
input_row.pack(fill="x", pady=(0, 8))

tk.Label(
    input_row, text="input", bg=BG, fg=DIM,
    font=("Georgia", 10), width=8, anchor="w"
).pack(side="left")

tk.Entry(
    input_row, textvariable=input_var,
    bg=PANEL, fg=TEXT, font=("Georgia", 10),
    relief="flat", width=55
).pack(side="left", padx=(0, 8))

tk.Button(
    input_row, text="browse", bg=PANEL, fg=PINK,
    font=("Georgia", 10), relief="flat",
    command=browse_input
).pack(side="left")

output_row = tk.Frame(cera_panel, bg=BG)
output_row.pack(fill="x", pady=(0, 8))

tk.Label(
    output_row, text="output", bg=BG, fg=DIM,
    font=("Georgia", 10), width=8, anchor="w"
).pack(side="left")

tk.Entry(
    output_row, textvariable=output_var,
    bg=PANEL, fg=TEXT, font=("Georgia", 10),
    relief="flat", width=55
).pack(side="left", padx=(0, 8))

tk.Button(
    output_row, text="browse", bg=PANEL, fg=PINK,
    font=("Georgia", 10), relief="flat",
    command=browse_output
).pack(side="left")

# ── states panel ──────────────────────────────
states_panel = tk.Frame(window, bg=BG)

states_yaml_row = tk.Frame(states_panel, bg=BG)
states_yaml_row.pack(fill="x", pady=(0, 8))

tk.Label(
    states_yaml_row, text="config", bg=BG, fg=DIM,
    font=("Georgia", 10), width=8, anchor="w"
).pack(side="left")

tk.Entry(
    states_yaml_row, textvariable=yaml_var,
    bg=PANEL, fg=TEXT, font=("Georgia", 10),
    relief="flat", width=55
).pack(side="left", padx=(0, 8))

tk.Button(
    states_yaml_row, text="browse", bg=PANEL, fg=PINK,
    font=("Georgia", 10), relief="flat",
    command=browse_yaml
).pack(side="left")

states_out_row = tk.Frame(states_panel, bg=BG)
states_out_row.pack(fill="x", pady=(0, 8))

tk.Label(
    states_out_row, text="output", bg=BG, fg=DIM,
    font=("Georgia", 10), width=8, anchor="w"
).pack(side="left")

tk.Entry(
    states_out_row, textvariable=output_var,
    bg=PANEL, fg=TEXT, font=("Georgia", 10),
    relief="flat", width=55
).pack(side="left", padx=(0, 8))

tk.Button(
    states_out_row, text="browse", bg=PANEL, fg=PINK,
    font=("Georgia", 10), relief="flat",
    command=browse_output
).pack(side="left")

# ── visualise panel ───────────────────────────
visualise_panel = tk.Frame(window, bg=BG)

vis_yaml_row = tk.Frame(visualise_panel, bg=BG)
vis_yaml_row.pack(fill="x", pady=(0, 8))

tk.Label(
    vis_yaml_row, text="config", bg=BG, fg=DIM,
    font=("Georgia", 10), width=8, anchor="w"
).pack(side="left")

tk.Entry(
    vis_yaml_row, textvariable=yaml_var,
    bg=PANEL, fg=TEXT, font=("Georgia", 10),
    relief="flat", width=55
).pack(side="left", padx=(0, 8))

tk.Button(
    vis_yaml_row, text="browse", bg=PANEL, fg=PINK,
    font=("Georgia", 10), relief="flat",
    command=browse_yaml
).pack(side="left")

vis_images_row = tk.Frame(visualise_panel, bg=BG)
vis_images_row.pack(fill="x", pady=(0, 8))

tk.Label(
    vis_images_row, text="images", bg=BG, fg=DIM,
    font=("Georgia", 10), width=8, anchor="w"
).pack(side="left")

tk.Entry(
    vis_images_row, textvariable=images_var,
    bg=PANEL, fg=TEXT, font=("Georgia", 10),
    relief="flat", width=55
).pack(side="left", padx=(0, 8))

tk.Button(
    vis_images_row, text="browse", bg=PANEL, fg=PINK,
    font=("Georgia", 10), relief="flat",
    command=browse_images
).pack(side="left")

# ── mode switching ────────────────────────────
def switch_mode(event=None):
    mode = mode_var.get()
    cera_panel.pack_forget()
    states_panel.pack_forget()
    visualise_panel.pack_forget()

    if mode == "cera script":
        cera_panel.pack(fill="x", padx=20, pady=(0, 8))
    elif mode == "states":
        states_panel.pack(fill="x", padx=20, pady=(0, 8))
    elif mode == "visualise":
        visualise_panel.pack(fill="x", padx=20, pady=(0, 8))

mode_dropdown.bind("<<ComboboxSelected>>", switch_mode)
switch_mode()  # set initial state

# ── preview panel ─────────────────────────────
preview_frame = tk.Frame(window, bg=PANEL, bd=1, relief="flat")
preview_frame.pack(fill="both", expand=True, padx=20, pady=(8, 8))

preview_text = tk.Text(
    preview_frame,
    bg=PANEL,
    fg=TEXT,
    font=("Courier", 9),
    relief="flat",
    state="disabled",
    wrap="none",
    padx=12,
    pady=12
)
preview_text.pack(fill="both", expand=True)



def highlight():
    # keywords — show, scene, nvl, adv, hide, narrator
    # colour: sage green
    preview_text.tag_config("keyword", foreground="#7A9E7E")

    # strings — anything in "quotes"  
    # colour: dusty pink
    preview_text.tag_config("string", foreground="#C47A7A")

    # comments — lines starting with ##
    # colour: dim
    preview_text.tag_config("comment", foreground="#8A8A7A")

    # commands — lines starting with $
    # colour: soft gold
    preview_text.tag_config("command", foreground="#B8960C")

    # cg triggers — show cg lines
    # colour: soft blue
    preview_text.tag_config("cg", foreground="#7A9E9E")
    
    content = preview_text.get("1.0", "end")
    
    patterns = {
        "comment": r"##[^\n]*",
        "command": r"^\$[^\n]*",
        "keyword": r"\b(show|scene|hide|nvl|narrator|window|play|pause)\b",
        "string":  r'"[^"]*"',
        "cg":      r"\bcg_\w+",
    }
    
    for tag, pattern in patterns.items():
        for match in re.finditer(pattern, content, re.MULTILINE):
            start = f"1.0 + {match.start()} chars"
            end = f"1.0 + {match.end()} chars"
            preview_text.tag_add(tag, start, end)
            
    preview_text.config(state="disabled")
# ── generate logic ────────────────────────────
def generate():
    mode = mode_var.get()

    if mode == "cera script":
        input_path  = input_var.get()
        output_path = output_var.get()

        if not input_path or not output_path:
            messagebox.showwarning(
                "~ cerabellum ~",
                "please set an input and output path first ♡"
            )
            return

        try:
            from formatter import format_script
            format_script(input_path, output_path)

            with open(output_path, "r", encoding="utf-8") as f:
                content = f.read()

            preview_text.config(state="normal")
            preview_text.delete("1.0", "end")
            preview_text.insert("1.0", content)
            preview_text.config(state="disabled")
            highlight()
            messagebox.showinfo("~ cerabellum ~", "~ generated successfully ♡ ~")

        except Exception as e:
            messagebox.showerror("~ cerabellum ~", f"something went wrong:\n{e}")

    elif mode == "states":
        yaml_path   = yaml_var.get()
        output_path = output_var.get()

        if not yaml_path or not output_path:
            messagebox.showwarning(
                "~ cerabellum ~",
                "please set a config and output path first ♡"
            )
            return

        try:
            from config import Config
            from encapsulator import encapsulate

            cfg = Config(yaml_path)
            all_output = []

            for char_id, character in cfg.characters.items():
                all_output.append(encapsulate(character))
                all_output.append("")

            content = "\n".join(all_output)

            with open(output_path, "w", encoding="utf-8") as f:
                f.write(content)

            preview_text.config(state="normal")
            preview_text.delete("1.0", "end")
            preview_text.insert("1.0", content)
            preview_text.config(state="disabled")
            highlight()
            messagebox.showinfo("~ cerabellum ~", "~ states generated ♡ ~")

        except Exception as e:
            messagebox.showerror("~ cerabellum ~", f"something went wrong:\n{e}")

    elif mode == "visualise":
        yaml_path   = yaml_var.get()
        images_root = images_var.get() or "images"

        if not yaml_path:
            messagebox.showwarning(
                "~ cerabellum ~",
                "please set a config path first ♡"
            )
            return

        try:
            from config import Config
            from visualiser import visualise

            cfg = Config(yaml_path)
            all_output = []

            for char_id, character in cfg.characters.items():
                all_output.append(visualise(character, images_root))
                all_output.append("")

            content = "\n".join(all_output)

            preview_text.config(state="normal")
            preview_text.delete("1.0", "end")
            preview_text.insert("1.0", content)
            preview_text.config(state="disabled")

        except Exception as e:
            messagebox.showerror("~ cerabellum ~", f"something went wrong:\n{e}")

def copy_output():
    content = preview_text.get("1.0", "end")
    window.clipboard_clear()
    window.clipboard_append(content)
    highlight()
    messagebox.showinfo("~ cerabellum ~", "~ copied to clipboard ♡ ~")

# ── action buttons ────────────────────────────
btn_row = tk.Frame(window, bg=BG)
btn_row.pack(fill="x", padx=20, pady=(0, 20))

tk.Button(
    btn_row,
    text="~ generate ~",
    bg=GREEN,
    fg=TEXT,
    font=("Georgia", 11),
    relief="flat",
    padx=16,
    pady=6,
    command=generate
).pack(side="left")

tk.Button(
    btn_row,
    text="copy",
    bg=PANEL,
    fg=PINK,
    font=("Georgia", 10),
    relief="flat",
    padx=12,
    pady=6,
    command=copy_output
).pack(side="right", padx=(8, 0))

tk.Button(
    btn_row,
    text="save",
    bg=PANEL,
    fg=PINK,
    font=("Georgia", 10),
    relief="flat",
    padx=12,
    pady=6,
    command=browse_output
).pack(side="right")

# ── footer ────────────────────────────────────
tk.Label(
    window,
    text="~ cerabellum · lobster trilogy ~",
    bg=BG,
    fg=DIM,
    font=("Georgia", 8)
).pack(pady=(0, 8))

# mainloop ALWAYS last ─────────────────────────
window.mainloop()
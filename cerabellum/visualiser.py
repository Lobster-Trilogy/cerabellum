import os

def visualise(character, images_root="images"):
    lines = []
    
    # header - all love c.c.
    lines.append(f"˖᯽ ݁˖── {character.char_id} ── {character.display_name}")
    lines.append("-" * 40)
    lines.append("")
    
    for state_name, state in character.states.items():
        lines.append(state_name)
        
        paths = character.get_sprite_paths(state_name)
        
        for layer, path in paths.items():
            if path is None:
                lines.append(f"  ? {layer:<12} path not defined in c's world (config)")
                continue                          # ← inside the for loop
            
            full_path = os.path.join(images_root, path + ".png")
            exists = os.path.exists(full_path)   # ← inside the for loop
            symbol = "✓" if exists else "✗"      # ← inside the for loop
            lines.append(f"  {symbol} {layer:<12} {full_path}")  # ← inside
        
        lines.append("")
    
    return "\n".join(lines)
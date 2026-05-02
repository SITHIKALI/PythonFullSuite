# Duplicate & Scam File Remover with GUI in Python (with Auto-Delete Option)

import os
import hashlib
import re
import shutil
from collections import defaultdict
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk

# Theme configuration
THEMES = {
    'light': {
        'bg': '#ffffff',
        'fg': '#000000',
        'select_bg': '#0078d4',
        'select_fg': '#ffffff',
        'button_bg': '#f0f0f0',
        'button_fg': '#000000',
        'entry_bg': '#ffffff',
        'entry_fg': '#000000',
        'text_bg': '#ffffff',
        'text_fg': '#000000',
        'frame_bg': '#f0f0f0'
    },
    'dark': {
        'bg': '#2d2d2d',
        'fg': '#ffffff',
        'select_bg': '#404040',
        'select_fg': '#ffffff',
        'button_bg': '#404040',
        'button_fg': '#ffffff',
        'entry_bg': '#404040',
        'entry_fg': '#ffffff',
        'text_bg': '#1e1e1e',
        'text_fg': '#ffffff',
        'frame_bg': '#2d2d2d'
    }
}

# Global theme variable
current_theme = 'light'

def apply_theme(widget, theme_name):
    """Apply theme colors to a widget and its children"""
    theme = THEMES[theme_name]
    
    # Apply theme to the widget itself
    try:
        if isinstance(widget, tk.Tk) or isinstance(widget, tk.Toplevel):
            widget.configure(bg=theme['bg'])
        elif isinstance(widget, tk.Frame):
            widget.configure(bg=theme['frame_bg'])
        elif isinstance(widget, tk.Button):
            widget.configure(bg=theme['button_bg'], fg=theme['button_fg'], 
                           activebackground=theme['select_bg'], activeforeground=theme['select_fg'])
        elif isinstance(widget, tk.Entry):
            widget.configure(bg=theme['entry_bg'], fg=theme['entry_fg'], 
                           insertbackground=theme['entry_fg'])
        elif isinstance(widget, tk.Checkbutton):
            widget.configure(bg=theme['frame_bg'], fg=theme['fg'], 
                           activebackground=theme['frame_bg'], activeforeground=theme['fg'],
                           selectcolor=theme['entry_bg'])
        elif isinstance(widget, scrolledtext.ScrolledText):
            widget.configure(bg=theme['text_bg'], fg=theme['text_fg'], 
                           insertbackground=theme['text_fg'])
    except tk.TclError:
        pass  # Some widgets may not support all options
    
    # Apply theme to all children
    for child in widget.winfo_children():
        apply_theme(child, theme_name)

def toggle_theme():
    """Toggle between light and dark theme"""
    global current_theme
    current_theme = 'dark' if current_theme == 'light' else 'light'
    apply_theme(root, current_theme)
    
    # Update theme button text
    theme_button.configure(text=f"Switch to {'Light' if current_theme == 'dark' else 'Dark'} Mode")

# Step 1: Generate MD5 hash of a file to detect duplicates
def get_file_hash(file_path):
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as file:
            buf = file.read()
            hasher.update(buf)
        return hasher.hexdigest()
    except Exception as e:
        return None

# Step 2: Identify duplicate files and exact name matches
def find_duplicates(target_dir):
    hash_map = defaultdict(list)
    name_map = defaultdict(list)
    for root, _, files in os.walk(target_dir):
        for name in files:
            file_path = os.path.join(root, name)
            file_hash = get_file_hash(file_path)
            if file_hash:
                hash_map[file_hash].append(file_path)
            name_map[name].append(file_path)

    duplicates = {h: paths for h, paths in hash_map.items() if len(paths) > 1}
    exact_name_duplicates = {n: paths for n, paths in name_map.items() if len(paths) > 1}
    return duplicates, exact_name_duplicates

# Step 3: Detect scam or phishing files by name/content pattern
def is_scam_file(file_path):
    scam_keywords = ["free_money", "passwords", "bitcoin", "porn", "hacked", "win_prize"]
    try:
        with open(file_path, 'r', errors='ignore') as file:
            content = file.read().lower()
            for keyword in scam_keywords:
                if keyword in content:
                    return True
    except Exception:
        pass

    filename = os.path.basename(file_path).lower()
    for keyword in scam_keywords:
        if keyword in filename:
            return True

    return False

# Step 4: Scan and classify with auto-delete/move option
def scan_directory(target_dir, auto_action=False):
    duplicates, exact_name_duplicates = find_duplicates(target_dir)
    scam_files = []

    if auto_action:
        removed_dir = os.path.join(target_dir, "removed")
        os.makedirs(removed_dir, exist_ok=True)

    for root, _, files in os.walk(target_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if is_scam_file(file_path):
                scam_files.append(file_path)
                if auto_action:
                    try:
                        shutil.move(file_path, os.path.join(removed_dir, file))
                    except Exception:
                        pass

    if auto_action:
        for file_list in duplicates.values():
            for dup_file in file_list[1:]:  # keep one original
                try:
                    shutil.move(dup_file, os.path.join(removed_dir, os.path.basename(dup_file)))
                except Exception:
                    pass

        for file_list in exact_name_duplicates.values():
            for dup_file in file_list[1:]:  # keep one file with the same name
                try:
                    shutil.move(dup_file, os.path.join(removed_dir, os.path.basename(dup_file)))
                except Exception:
                    pass

    return duplicates, scam_files, exact_name_duplicates

# Step 5: GUI setup
def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_var.set(folder)

def run_scan():
    target_dir = folder_var.get()
    if not os.path.exists(target_dir):
        messagebox.showerror("Error", "Directory does not exist.")
        return

    auto_action = auto_action_var.get()

    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, f"Scanning: {target_dir}\n\n")

    duplicates, scam_files, name_duplicates = scan_directory(target_dir, auto_action=auto_action)

    if duplicates:
        output_text.insert(tk.END, "[Duplicate Files Detected by Content]:\n")
        for file_list in duplicates.values():
            output_text.insert(tk.END, "\n".join(file_list) + "\n---\n")
    else:
        output_text.insert(tk.END, "[INFO] No duplicate files found by content.\n")

    if name_duplicates:
        output_text.insert(tk.END, "\n[Duplicate Files Detected by Filename]:\n")
        for file_list in name_duplicates.values():
            output_text.insert(tk.END, "\n".join(file_list) + "\n---\n")
    else:
        output_text.insert(tk.END, "\n[INFO] No duplicate filenames found.\n")

    if scam_files:
        output_text.insert(tk.END, "\n[Potential Scam Files Detected]:\n")
        output_text.insert(tk.END, "\n".join(scam_files))
    else:
        output_text.insert(tk.END, "\n[INFO] No scam files found.")

# Step 6: Launch GUI
def main():
    global root, theme_button, entry, browse_btn, auto_delete_checkbox, scan_btn, output_text
    global folder_var, auto_action_var
    
    root = tk.Tk()
    root.title("Duplicate & Scam File Remover")
    root.geometry("700x600")

    folder_var = tk.StringVar()
    auto_action_var = tk.BooleanVar()

    # Create main frame
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Theme switcher button
    theme_frame = tk.Frame(main_frame)
    theme_frame.pack(fill=tk.X, pady=(0, 10))

    theme_button = tk.Button(theme_frame, text="Switch to Dark Mode", command=toggle_theme)
    theme_button.pack(side=tk.RIGHT)

    # Folder selection frame
    folder_frame = tk.Frame(main_frame)
    folder_frame.pack(fill=tk.X, pady=(0, 10))

    entry = tk.Entry(folder_frame, textvariable=folder_var, width=60)
    entry.pack(side=tk.LEFT, padx=(0, 5), fill=tk.X, expand=True)

    browse_btn = tk.Button(folder_frame, text="Browse", command=browse_folder)
    browse_btn.pack(side=tk.RIGHT)

    # Options frame
    options_frame = tk.Frame(main_frame)
    options_frame.pack(fill=tk.X, pady=(0, 10))

    auto_delete_checkbox = tk.Checkbutton(options_frame, text="Auto-Delete/Move Files", variable=auto_action_var)
    auto_delete_checkbox.pack(side=tk.LEFT)

    # Scan button
    scan_btn = tk.Button(main_frame, text="Scan Now", command=run_scan)
    scan_btn.pack(pady=(0, 10))

    # Output text area
    output_text = scrolledtext.ScrolledText(main_frame, width=80, height=20)
    output_text.pack(fill=tk.BOTH, expand=True)

    # Apply initial theme
    apply_theme(root, current_theme)

    root.mainloop()

if __name__ == "__main__":
    main()

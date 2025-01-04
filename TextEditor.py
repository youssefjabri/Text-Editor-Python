import tkinter as Tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    global current_file_saved, filepath
    filepath = askopenfilename(
        filetypes=[("Text File", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text_edit.delete(1.0, Tk.END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        text_edit.insert(Tk.END, text)
    window.title(f"Text Editor - {filepath}")
    current_file_saved = True

def save_file(event=None):
    global current_file_saved, filepath
    if not filepath:
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text File", "*.txt"), ("All Files", "*.*")]
        )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_edit.get(1.0, Tk.END).strip()
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")
    current_file_saved = True

def on_text_change(event=None):
    global current_file_saved
    if text_edit.edit_modified():
        if current_file_saved:
            window.title(f"Text Editor - {filepath or 'Untitled*'}")
        current_file_saved = False
    text_edit.edit_modified(False) 

def on_closing():
    if not current_file_saved:
        response = messagebox.askyesnocancel(
            "Unsaved Changes",
            "You have unsaved changes. Do you want to save them before closing?"
        )
        if response is None:
            return
        elif response:
            save_file()
    window.destroy()

current_file_saved = True
filepath = None

window = Tk.Tk()
window.title("Text Editor")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)

text_edit = Tk.Text(window)
fr_buttons = Tk.Frame(window, relief=Tk.RAISED, bd=1)
btn_open = Tk.Button(fr_buttons, text="Open...", command=open_file)
btn_save = Tk.Button(fr_buttons, text="Save...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=2, pady=2)
btn_save.grid(row=1, column=0, sticky="ew", padx=2)

fr_buttons.grid(row=0, column=0, sticky="ns")
text_edit.grid(row=0, column=1, sticky="nsew")

text_edit.bind("<<Modified>>", on_text_change)
text_edit.bind("<Control-s>", save_file)
window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()

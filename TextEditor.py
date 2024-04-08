import tkinter as Tk
from tkinter.filedialog import askopenfilename , asksaveasfilename

def open_file():
    """Open a file for editing"""
    filepath = askopenfilename(
        filetypes=[("Text File" , "*.txt"),("All Files", "*.*")]
    )
    if not filepath:
        return
    text_edit.delete(1.0, Tk.END)
    with open(filepath , 'r') as input_file:
        text = input_file.read()
        text_edit.insert(Tk.END, text)
    window.title(f"Text Editor - {filepath}")

def save_file():
    """Save The Current file"""
    filepath =  asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text File" , "*.txt"),("All Files", "*.*")]
    )
    if not filepath: 
        return
    with open(filepath , "w") as output_file :
        text = text_edit.get(1.0, Tk.END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")
        
window = Tk.Tk()
window.title("Text Editor")
window.rowconfigure(0 , minsize=500 , weight=1)
window.columnconfigure(1 , minsize=500 , weight=1)

text_edit =  Tk.Text(window)
fr_buttons = Tk.Frame(window , relief=Tk.RAISED , bd=1)
btn_open = Tk.Button(fr_buttons , text="Open..." , command=open_file )
btn_save = Tk.Button(fr_buttons , text="Save..." , command=save_file )

btn_open.grid(row=0 , column=0, sticky="ew" ,padx=2 , pady=2)
btn_save.grid(row=1 , column=0, sticky="ew" ,padx=2)

fr_buttons.grid(row=0, column=0 , sticky="ns")
text_edit.grid(row=0 , column=1, sticky="nsew")

window.mainloop()
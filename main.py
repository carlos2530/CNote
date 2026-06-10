import tkinter as tk
from tkinter import filedialog, messagebox

#Functions
#To save the file
def save_file():
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file:
        try:
            content = text_area.get("1.0", tk.END)
            with open(file, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Success", "File saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

#Load file
def load_file():
    file = filedialog.askopenfilename(
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file:
        try:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", content)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the file: {e}")

def give_negrita():
    try:
        inicio = text_area.index("sel.first")
        fin = text_area.index("sel.last")
        text_area.tag_config("negrita", font=("Arial", 12, "bold"))
        tags_actuales = text_area.tag_names(inicio)

        if "negrita" in tags_actuales:
            text_area.tag_remove("negrita", inicio, fin)
        else:
            text_area.tag_add("negrita", inicio, fin)
    except tk.TclError:
        pass # No hay texto seleccionado, no hacer nada

def insert_check():
    estado = tk.BooleanVar()
    check = tk.Checkbutton(text_area, variable=estado)
    text_area.window_create(tk.INSERT, window=check)
    text_area.insert(tk.INSERT, " ")  # Agregar un espacio después del checkbox para separar

#Window settings
window = tk.Tk()
window.title("CNote")
window.geometry("480x640")

#Menu settings
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=menu_file)
menu_file.add_command(label="Open", command=load_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=window.quit)

#Toolbar settings
tool_bar = tk.Frame(window, bg="#f0f0f0")
tool_bar.pack(fill="x", padx=10, pady=5)

button_negrita = tk.Button(tool_bar, text="B", font=("Arial", 12, "bold"), command=give_negrita)
button_negrita.pack(side="left", padx=5)

button_check = tk.Button(tool_bar, text="Insert Check", command=insert_check, font=("Arial", 10))
button_check.pack(side="left", padx=5)

#Text area
text_area = tk.Text(window, font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

#bucle
window.mainloop()
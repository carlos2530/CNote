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
            messagebox.showinfo("Success", "File loaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the file: {e}")

#Window settings
window = tk.Tk()
window.title("CNote")
window.geometry("400x300")

#Menu settings
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

menu_file = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=menu_file)

menu_file.add_command(label="Open", command=load_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=window.quit)

#Text area
text_area = tk.Text(window, font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

#bucle
window.mainloop()
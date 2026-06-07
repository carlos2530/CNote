import tkinter as tk

#window creation
window = tk.Tk()
window.title("CNote")
#height and width of the window
window.geometry("400x300")

#Text area
text_area = tk.Text(window, font=("Arial", 12))
text_area.pack(expand=True, fill="both", padx=10, pady=10)

#bucle
window.mainloop()
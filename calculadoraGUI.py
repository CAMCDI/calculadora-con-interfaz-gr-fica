import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Operación no válida")
    else:
        entry_var.set(entry_var.get() + button_text)

# Crear la ventana
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x400")
root.resizable(False, False)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify="right", bd=10)
entry.pack(fill="both")

buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")
    for button_text in row:
        btn = tk.Button(row_frame, text=button_text, font=("Arial", 18), command=lambda text=button_text: on_click(text))
        btn.pack(side="left", expand=True, fill="both")

root.mainloop()

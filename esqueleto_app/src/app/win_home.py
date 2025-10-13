import tkinter as tk
from src.core.classes import User

from .win_progress import open_win_progress
from .win_talleres import open_win_talleres
from .

from tkinter import ttk, messagebox

def open_win_home(user:User):
    root = tk.Tk()
    root.title("Home / Bienvenida")
    root.geometry("360x220")
    frm = ttk.Frame(root, padding=16)
    frm.pack(fill="both", expand=True)
    ttk.Label(frm, text=f"Hola, {user.name}", font=("Segoe UI", 11, "bold")).pack(pady=(0, 8))
    ttk.Button(frm, text="Metas",
               command=lambda: open).pack()
    ttk.Button(frm, text="Progreso",
               command=lambda: open_win_progress(root, user)).pack()
    ttk.Button(frm, text="Talleres",
               command=lambda: open_win_talleres()).pack()
    ttk.Button(frm, text="Tips",
               command=lambda: messagebox.showinfo("Info", "¡Equipo listo!")).pack()
    ttk.Button(frm, text="Cerrar", command=root.destroy).pack()
    root.mainloop()

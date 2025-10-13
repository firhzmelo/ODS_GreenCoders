import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

def open_win_home(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Home / Bienvenida")
    win.geometry("400x300")
    frm = ttk.Frame(win, padding=16)
    frm.pack(fill="both", expand=True)

    ttk.Label(frm, text="Talleres", font=("Segoe UI", 11, "bold")).pack(pady=(0, 8))
    ttk.Button(frm, text="Tutorial huerto vertical",
           command=lambda:webbrowser.open("https://www.youtube.com/watch?v=IEX7D8wxkm4")).pack()
    ttk.Button(frm, text="Taller de composta",
           command=lambda:webbrowser.open("https://educacion.mma.gob.cl/educacion-ambiental-en-tu-casa/compostaje/")).pack()
    ttk.Button(frm, text="Tutorial papel reciclado",
           command=lambda:webbrowser.open("https://youtu.be/kjkry2AkcPQ?si=dt_3K-GP22iAtmzg")).pack()
    ttk.Button(frm, text="Talleres precenciales en León, Guanajuato",
           command=lambda:webbrowser.open("https://www.leon.gob.mx/medioambiente/articulo.php?a=312")).pack()
    ttk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=8)

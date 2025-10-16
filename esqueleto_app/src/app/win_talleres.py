import ttkbootstrap as ttk
import webbrowser
import tkinter as tk

tamLetra = 10
tipLetra = "Verdana"
tipTitulo = "Century Gothic"

def open_win_talleres(parent: ttk.Window):
    global win
    win = ttk.Toplevel(parent)

    win.title("Home / Bienvenida")
    win.geometry("500x900")

    s=ttk.Style()
    s.configure("TButton", font=("Verdana",10, "bold"), anchor=tk.CENTER)
    s.configure("Titulo.TLabel", font=(tipLetra, 20, "bold"))
    s.configure("TLabel", font=(tipLetra, tamLetra))
    global frm

    frm = ttk.Frame(win, padding=16)
    frm.pack(fill="both", expand=True)
    ttk.Label(frm, text="Talleres", style="Titulo.TLabel").pack(pady=(150, 8))
    ttk.Button(frm, text="Tutorial huerto vertical",
            command=lambda:webbrowser.open("https://www.youtube.com/watch?v=IEX7D8wxkm4"), width=100).pack(pady=20)
    ttk.Button(frm, text="Taller de composta",
            command=lambda:webbrowser.open("https://educacion.mma.gob.cl/educacion-ambiental-en-tu-casa/compostaje/"), width=100).pack(pady=20)
    ttk.Button(frm, text="Tutorial papel reciclado",
            command=lambda:webbrowser.open("https://youtu.be/kjkry2AkcPQ?si=dt_3K-GP22iAtmzg"), width=100).pack(pady=20)
    ttk.Button(frm, text="Talleres precenciales en León",
            command=lambda:webbrowser.open("https://www.leon.gob.mx/medioambiente/articulo.php?a=312"), width=100).pack(pady=20)
    ttk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=8)

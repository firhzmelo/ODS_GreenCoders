import ttkbootstrap as tk
import webbrowser

tamLetra = 13
tipLetra = "Verdana"
tipTitulo = "Century Gothic"

def open_win_tips(parent: tk.Window):
    win = tk.Toplevel(parent)
    win.title("Home / Bienvenida")
    win.geometry("500x900")

    s=tk.Style()
    s.configure("TButton", font=("Verdana",10, "bold"), anchor=tk.CENTER)
    s.configure("Titulo.TLabel", font=(tipLetra, 20, "bold"))
    s.configure("TLabel", font=(tipLetra, tamLetra), padding=15)

    frm = tk.Frame(win, padding=16)
    frm.pack(fill="both", expand=True)

    tk.Label(frm, text="Tips", style="Titulo.TLabel").pack(pady=(150, 8))
    tk.Label(frm, text="- Reduce, reutiliza y recicla", wraplength=400, bootstyle="inverse-light").pack(anchor='w', fill="x")
              
    tk.Label(frm, text="- Ahorra energía (apaga las luces que no estas utilizando y aprovecha la luz natural)", bootstyle="inverse-light", wraplength=400).pack(anchor='w', fill="x")
               
    tk.Label(frm, text="- Cuida el agua", wraplength=400)
               
    tk.Label(frm, text="- Camina, usa bicicleta o comparte coche para disminuir emisiones", bootstyle="inverse-light", wraplength=400).pack(anchor='w', fill="x")
               
    tk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=8, anchor='ce')

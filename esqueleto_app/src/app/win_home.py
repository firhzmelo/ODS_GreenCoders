import ttkbootstrap as ttk
from core.classes import User
from PIL import Image, ImageTk

from win_progress import open_win_progress
from win_talleres import open_win_talleres
from win_tips import open_win_tips
from win_metas import open_win_metas
from core.classes import Task
from win_api import open_win_api

tamLetra = 10
tipLetra = "Verdana"
tipTitulo = "Century Gothic"

def metas(frm:ttk.Frame, user:User):
    # frm.pack_forget()
    open_win_metas(root, user=user)


def open_win_home(LogIn, user:User):
    global root 
    root = LogIn
    root.title("Home / Bienvenida")
    root.geometry("500x900")

    s=ttk.Style()
    s.configure("TButton", font=("Verdana",10, "bold"))
    s.configure("Titulo.TLabel", font=(tipLetra, 20, "bold"))
    s.configure("TLabel", font=(tipLetra, tamLetra))

    frm = ttk.Frame(root, padding=16)
    frm.pack(fill="both", expand=True)

    user.tasks.append(Task(
        name='Ducha Express',
        desc='Dúchate en el tiempo que dura una canción (máximo 5 minutos).'
    ))
    user.tasks.append(Task(
        name='Cero Papel en tu Cartera',
        desc='Hoy no aceptes ningún recibo impreso. Pídelo por correo o simplemente recházalo. '
    ))
    user.tasks.append(Task(
        name='Movilidad Activa',
        desc='Realiza un trayecto corto caminando o en bicicleta en lugar de usar el auto.'
    ))

    imagen = Image.open("Logo_App.png")
    imagen = imagen.resize((300,118))

    img_tk = ImageTk.PhotoImage(imagen)

    ttk.Label(frm, image=img_tk).pack()

    ttk.Label(frm, text=f"Hola, {user.name}", style="Titulo.TLabel").pack(pady=(10, 50))
    ttk.Button(frm, text="Metas",
               command=lambda: metas(frm, user), width=100).pack(pady=15)
    ttk.Button(frm, text="Progreso",
               command=lambda: open_win_progress(root, user=user), width=100).pack(pady=15)
    ttk.Button(frm, text="Talleres",
               command=lambda: open_win_talleres(root), width=100).pack(pady=15)
    ttk.Button(frm, text="Tips",
               command=lambda: open_win_tips(root), width=100).pack(pady=15)
    ttk.Button(frm, text="Calidad del aire",
               command=lambda: open_win_api(root), width=100).pack(pady=15)
    ttk.Button(frm, text="Cerrar", command=root.destroy).pack(pady=15)
    root.mainloop()

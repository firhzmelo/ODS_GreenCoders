import tkinter as tk
from tkinter import ttk
from .CreateAccount import crea_cuenta
from src.core.leer_usuario import leer_usuario
from .win_home import open_win_home
from src.core.classes import User

def dirige(user:User):
    LogIn.destroy()
    open_win_home(user)

def emergente(titulo, mensaje, dirigir, user:User = None):
    win.title(titulo)
    win.geometry("300x150")

    frame = ttk.Frame(win, padding=12)
    frame.pack(fill="both", expand=True)

    tk.Label(frame, text=mensaje).pack()
    if dirigir:
        tk.Button(frame, text="Ok", command=dirige(user)).pack()
    else:
        tk.Button(frame, text="Ok", command= lambda: win.destroy()).pack()

def check(parent ,usuario, clave):
    user = leer_usuario(usuario)
    global win
    win = tk.Toplevel(parent)

    if user == -1:
        emergente("Usuario Incorrecto", "El usuario no existe o es incorrecto,\nintente de nuevo o cree una cuenta", 0)
    elif user.password != clave:
        emergente("Contraseña Incorrecta", "Contraseña incorrecta\nintente de nuevo", 0)
    else:
        emergente("Inicio correcto", "Log In correcto,\ndirigir a inicio", 1, user)
    


def logIn():
    global LogIn
    LogIn = tk.Tk()
    LogIn.geometry("300x250")
    LogIn.title("LogIn")

    frame = ttk.Frame(LogIn, padding=16)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="LogIn", font=("Segoe UI",16, "bold")).pack(pady = 10)

    usuario = tk.StringVar()
    clave = tk.StringVar()

    ttk.Label(frame, text="Usuario").pack(fill = 'x')
    ttk.Entry(frame, textvariable=usuario).pack(pady = 5, fill = 'x')
    ttk.Label(frame, text="Contraseña").pack(fill='x')
    ttk.Entry(frame, textvariable=clave, show='*').pack( pady= 5, fill ='x')

    ttk.Button(frame, text="Ingresar", command=lambda: check(LogIn, usuario.get(), clave.get())).pack()
    ttk.Button(frame, text="Crear cuenta", command=lambda: crea_cuenta(LogIn)).pack()

    LogIn.mainloop()

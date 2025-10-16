import ttkbootstrap as ttk
from CreateAccount import crea_cuenta
from core.leer_usuario import leer_usuario
from win_home import open_win_home
from core.classes import User

tamLetra = 10
tipLetra = "Verdana"
tipTitulo = "Century Gothic"


def dirige(user:User):
    win.destroy()
    frame.pack_forget()
    open_win_home(LogIn, user)

def emergente(titulo, mensaje, dirigir, user:User = None):
    win.title(titulo)
    win.geometry("300x300")

    frame = ttk.Frame(win, padding=12)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text=mensaje, font=(tipLetra, tamLetra, "bold")).pack()
    if dirigir:
        ttk.Button(frame, text="Ok", command=lambda u=user: dirige(u)).pack()
    else:
        ttk.Button(frame, text="Ok", command= lambda: win.destroy()).pack()

def check(parent ,usuario, clave):
    user = leer_usuario(usuario)
    global win
    global win 
    win = ttk.Toplevel(parent)

    if user == -1:
        emergente("Usuario Incorrecto", "El usuario no existe o es incorrecto,\nintente de nuevo o cree una cuenta", 0)
    elif user.password != clave:
        emergente("Contraseña Incorrecta", "Contraseña incorrecta\nintente de nuevo", 0)
    else:
        emergente("Inicio correcto", "Log In correcto,\ndirigir a inicio", 1, user)
    


def logIn():
    global LogIn
    LogIn = ttk.Window(themename="minty")

    s=ttk.Style()
    s.configure("TButton", font=("Verdana",10, "bold"))


    LogIn.geometry("500x900")
    LogIn.title("LogIn")
    global frame
    frame = ttk.Frame(LogIn, padding=16)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="LogIn", font=("Century Gothic",30, "bold")).pack(pady = (150, 10))

    usuario = ttk.StringVar()
    clave = ttk.StringVar()

    ttk.Label(frame, text="Usuario", font=("Verdana",tamLetra)).pack(fill = 'x', pady=15, padx=15)
    ttk.Entry(frame, textvariable=usuario).pack(pady = 5, fill = 'x', padx=15)
    ttk.Label(frame, text="Contraseña",font=("Verdana",tamLetra)).pack(fill='x', pady=15, padx=15)
    ttk.Entry(frame, textvariable=clave, show='*').pack( pady= 15, fill ='x', padx=15)

    ttk.Button(frame, text="Ingresar", width=50,command=lambda: check(LogIn, usuario.get(), clave.get())).pack( padx=10, pady=20)
    ttk.Button(frame, text="Crear cuenta", width=50, command=lambda: crea_cuenta(LogIn)).pack( padx = 10, pady=20)

    LogIn.mainloop()

import ttkbootstrap as ttk
from core.leer_usuario import leer_usuario
from core.classes import User

tamLetra = 10
tipLetra = "Verdana"
tipTitulo = "Century Gothic"

def emergente(titulo, mensaje, elim):
    global win
    win = ttk.Toplevel(root)
    win.title(titulo)
    win.geometry("400x400")

    ttk.Label(win, text=mensaje, bootstyle="warning").pack()
    if elim:
        ttk.Button(win, text="Ok", command=lambda: win.destroy()).pack(pady=20)
    else:
        ttk.Button(win, text="Ok", command=lambda: win.destroy()).pack(pady=20)

def has_cuenta(usuario, nombre, clave, clave2):
    import os

    if usuario.strip() == "" or nombre.strip() == "" or clave == "" or clave2 == "":
        emergente("Datos vacios","Hay campos vacios,\nrellena e intenta de nuevo", 0)
    elif clave != clave2:
        emergente("Contraseña no coincide","La contraseña no coincide,\n intente de nuevo", 0)
    elif leer_usuario(usuario) != -1:
        emergente("Usuario repetido","El usuario ya existe", 0)
    else:
        archivo = open(usuario, "w")
        archivo.write(usuario + '\n')
        archivo.write(nombre + '\n')
        archivo.write(clave)
        archivo.close()
        emergente("Registro exitoso", "El registro se conlcuyo\n de forma exitosa", 1)
        

def crea_cuenta(logIn):
    global root
    root = ttk.Toplevel(logIn)
    root.title("Crea tu cuenta")
    root.geometry("500x900")

    s=ttk.Style()
    s.configure("TButton", font=("Verdana",10, "bold"))

    frame = ttk.Frame(root, padding=16)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Crea una cuenta", font=(tipTitulo,20, "bold")).pack(pady = 10)

    usuario = ttk.StringVar()
    nombre = ttk.StringVar()
    clave = ttk.StringVar()
    clave2 = ttk.StringVar()

    ttk.Label(frame, text="Usuario", font=("Verdana", tamLetra)).pack(fill='x', pady=10)
    ttk.Entry(frame, textvariable=usuario).pack(fill='x', pady=10)
    ttk.Label(frame, text="Nombre",font=(tipLetra, tamLetra)).pack(fill='x', pady=10)
    ttk.Entry(frame, textvariable=nombre).pack(fill="x", pady=10)
    ttk.Label(frame, text="Contraseña",font=(tipLetra, tamLetra)).pack(fill='x', pady=10)
    ttk.Entry(frame, textvariable=clave, show='*').pack(fill='x', pady=10)
    ttk.Label(frame, text="Repite Contraseña",font=(tipLetra, tamLetra)).pack(fill='x', pady=10)
    ttk.Entry(frame, textvariable=clave2, show='*').pack(fill='x', pady=10)

    ttk.Button(frame, text="Crear", command=lambda: has_cuenta(usuario.get(), nombre.get(), clave.get(), clave2.get())).pack(pady=15)
    root.mainloop()

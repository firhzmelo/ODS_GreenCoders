import ttkbootstrap as ttk
from datetime import date
from core.classes import User
from core.classes import Task

tamLetra = 10
tipLetra = "Verdana"
tipTitulo = "Century Gothic"

def open_win_metas(parent: ttk.Window, user: User):
    win = ttk.Toplevel(parent)
    win.title("Metas")
    win.geometry("500x900")

    s=ttk.Style()
    s.configure("TButton", font=("Verdana",10, "bold"), anchor=ttk.CENTER)
    s.configure("Titulo.TLabel", font=(tipLetra, 15, "bold"))
    s.configure("TLabel", font=(tipLetra, tamLetra))

    frm = ttk.Frame(win, padding=15)
    frm.pack(expand=True, fill='both', pady=(40, 0))

    dia = date.today().strftime("%A")

    dias_semana = {
        "Monday": "Lun",
        "Tuesday": "Mar",
        "Wednesday": "Mie",
        "Thursday": "Jue",
        "Friday": "Vie",
        "Saturday": "Sab",
        "Sunday": "Dom"
    }

    def marcar_completada(task:Task):
        task.done = True
        task.day_done = dias_semana[dia]
        user.tasks_done.append(task)
        reconstruir_metas()

    def reconstruir_metas():
        for widget in frm.winfo_children():
            widget.destroy()
        
        for task in user.tasks:
            name = ttk.StringVar(value=task.name)
            label = ttk.Label(frm, text=name.get(), wraplength=260, style="Titulo.TLabel", justify='left')
            label.pack(side="top", pady=(20, 5), padx=10, anchor='w')
            desc = ttk.StringVar(value=task.desc)
            button = ttk.Label(frm, text=desc.get(), wraplength=400, justify='left', bootstyle="inverse-light")
            button.pack(padx=10, anchor='w')
            if task.done == False:
                ttk.Button(frm, text="Completar", command=lambda t=task: marcar_completada(t)).pack(anchor="e", padx=10, pady=7)
            else:
                ttk.Label(frm, text='Completada', bootstyle="success").pack(anchor='e', padx=10)
        
        ttk.Button(frm, text="Cerrar", command=win.destroy).pack(side='bottom', pady=10)
    reconstruir_metas()
import ttkbootstrap as tk
from core.classes import User
from core.classes import Task
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

tamLetra = 10
tipLetra = "Verdana"
tipTitulo = "Century Gothic"

def open_win_progress(parent: tk.Window, user: User):
    win = tk.Toplevel(parent)
    win.title("Tu Progreso")
    win.geometry("500x900")

    s=tk.Style()
    s.configure("TButton", font=("Verdana",10, "bold"), anchor=tk.CENTER)
    s.configure("Titulo.TLabel", font=(tipLetra, 20, "bold"))
    s.configure("TLabel", font=(tipLetra, tamLetra))

    frm = tk.Frame(win, padding=5)
    frm.pack(fill="both", expand=True)
    tk.Label(frm, text='Tareas Realizadas', justify='center', style="Titulo.TLabel").pack(anchor='center', pady=15)

    no_tareas = tk.StringVar(value=str(len(user.tasks_done))) # cambiar value por len(user.tasks_done
    tk.Label(frm, text=no_tareas.get(), justify='center', font=('Arial', 15)).pack(anchor="center")

    # Create a Matplotlib figure
    fig = Figure(figsize=(6, 5), dpi=75)
    ax = fig.add_subplot(111)
    # Get tasks
    tasks_done = user.tasks_done
    tasks_per_say = {"Lun": 0,
                     "Mar": 0, 
                     "Mie": 0, 
                     "Jue": 0, 
                     "Vie": 0, 
                     "Sab": 0, 
                     "Dom": 0
                    }
    # ax.tick_params(axis="x", rotation=45)
    for task in tasks_done:
        tasks_per_say[task.day_done] += 1


    # ax.plot(tasks_per_say.keys(), [2, 1, 3, 0, 4, 2, 2], marker="o")
    ax.bar(tasks_per_say.keys(), tasks_per_say.values(), color="#89bdce")
    ax.set_ylabel("No. de Tareas")
    ax.set_yticks([i for i in range(1, 6)])
    ax.tick_params(axis="x", rotation=45)
    # Embed the figure into Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frm)  # A tk.DrawingArea
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill='y')

    
    
    

    tk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=8, anchor="ce")

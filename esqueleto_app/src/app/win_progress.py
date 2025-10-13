import tkinter as tk
from tkinter import ttk
from src.core.classes import User
from src.core.classes import Task
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def open_win_progress(parent: tk.Tk, user: User):
    win = tk.Toplevel(parent)
    win.title("Tu Progreso")
    win.geometry("600x550")

    frm = ttk.Frame(win, padding=5)
    frm.pack(fill="both", expand=True)

    # Create a Matplotlib figure
    fig = Figure(figsize=(6, 5), dpi=75)
    ax = fig.add_subplot(111)
    # Get tasks
    tasks_done = user.tasks_done
    tasks_per_say = {"Lunes": 0,
                     "Martes": 0, 
                     "Miércoles": 0, 
                     "Jueves": 0, 
                     "Viernes": 0, 
                     "Sábado": 0, 
                     "Domingo": 0
                    }
    # ax.tick_params(axis="x", rotation=45)
    for task in tasks_done:
        tasks_per_say[task.day_done] += 1


    # ax.plot(tasks_per_say.keys(), [2, 1, 3, 0, 4, 2, 2], marker="o")
    ax.bar(tasks_per_say.keys(), [2, 1, 3, 0, 4, 2, 2])
    ax.set_title("Tareas Realizadas")
    ax.set_xlabel("Días")
    ax.set_ylabel("No. de Tareas")
    ax.set_yticks([i for i in range(1, 6)])
    # Embed the figure into Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frm)  # A tk.DrawingArea
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill='y')

    tk.Label(frm, text='Tareas Realizadas', justify='center', font=('Arial', 20, 'bold')).pack(anchor='center', pady=15)
    no_tareas = tk.StringVar(value=str(14)) # cambiar value por len(user.tasks_done
    tk.Label(frm, textvariable=no_tareas, justify='center', font=('Arial', 15)).pack(anchor="center")

    ttk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=8, anchor="se")

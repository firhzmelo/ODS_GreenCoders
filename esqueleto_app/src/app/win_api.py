import ttkbootstrap as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

tamLetra = 10
tipLetra = "Verdana"
tipTitulo = "Century Gothic"

def fetch_data():
    """
    Conecta con la API de Open-Meteo y obtiene temperaturas horarias
    de León, Gto (últimas 24 horas).
    Devuelve dos listas: horas y temperaturas.
    """
    try:
        url = (
            "http://api.openweathermap.org/data/2.5/air_pollution?lat=21.12908&lon=-101.67374&appid=7be4d1e0efe08515585a25fb63b0c9b0"
        )
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        sustancias = data["list"][0]["components"].keys()

        datos = data["list"][0]["components"].values()

        return sustancias, datos
        #print(sustancias)
        #print(datos)
    
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron obtener los datos:\\n{e}")
        return [], []


def create_bar_chart(sustancias, datos):
    """Gráfica de barras."""
    fig, ax = plt.subplots(figsize=(4, 5))
    ax.bar(sustancias, datos, color="#89bdce")
    ax.set_title("Contaminación actual \ndel aire en León, Gto")
    ax.set_ylabel("μg/m3")
    ax.set_xlabel("Contaminantes")
    ax.grid(True, linestyle="--", alpha=.5)
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    return fig


def mostrar_graficas(frm, sustancias, datos):
    """Inserta las tres gráficas en el frame de la ventana tkinter."""
    # Barras
    fig2 = create_bar_chart(sustancias, datos)
    canvas2 = FigureCanvasTkAgg(fig2, master=frm)
    canvas2.draw()
    canvas2.get_tk_widget().pack(pady=10, fill="x")


def open_win_api(parent: tk.Window):
    """
    Crea la ventana secundaria con gráficas de la API.
    """
    win = tk.Toplevel(parent)
    win.title("Canvas con API (Open-Meteo) y gráficas")
    win.geometry("500x900")

    s=tk.Style()
    s.configure("TButton", font=("Verdana",10, "bold"), anchor=tk.CENTER)
    s.configure("Titulo.TLabel", font=(tipLetra, 20, "bold"))
    s.configure("TLabel", font=(tipLetra, tamLetra))

    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    # Botón para cargar datos y graficar
    def cargar():
        sustancias, datos = fetch_data()
        if sustancias and datos:
            mostrar_graficas(frm, sustancias, datos)

    ttk.Button(frm, text="Cargar y mostrar gráficas", command=cargar).pack(pady=10)

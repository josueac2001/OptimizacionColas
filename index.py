# index.py
import tkinter as tk
from tkinter import messagebox

from views.interfaz import PanelEntradas, PanelResultados
from models.fabric import FabricaModelos

class ControladorColas:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Colas")
        self.root.geometry("500x550") 
        self.root.configure(padx=15, pady=15)

        self.panel_entradas = PanelEntradas(self.root)
        self.panel_entradas.pack(fill="x", pady=10)

        btn_calcular = tk.Button(self.root, text="EJECUTAR CÁLCULO", bg="#0052cc", fg="white", font=("Arial", 11, "bold"), command=self.procesar_calculo)
        btn_calcular.pack(fill="x", pady=10)

        self.panel_resultados = PanelResultados(self.root)
        self.panel_resultados.pack(fill="both", expand=True, pady=10)

    def procesar_calculo(self):
        try:
            datos = self.panel_entradas.obtener_datos()

            # Ahora le pasamos 'sigma' a la fábrica
            modelo = FabricaModelos.crear_modelo(
                tipo_modelo=datos["modelo"],
                lmbda=datos["lmbda"],
                mu=datos["mu"],
                s=datos["s"],
                sigma=datos["sigma"]
            )

            resultados = modelo.calcular()
            self.panel_resultados.mostrar_resultados(resultados)

        except ValueError as e:
            messagebox.showwarning("Aviso", str(e))
        except Exception as e:
            messagebox.showerror("Error crítico", f"Verifica los campos ingresados. Error: {str(e)}")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = ControladorColas(ventana)
    ventana.mainloop()
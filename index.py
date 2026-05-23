# index.py
import tkinter as tk
from tkinter import messagebox

from views.interfaz import PanelEntradas, PanelResultados
from models.fabric import FabricaModelos

class ControladorColas:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Colas")
        # Se aumentó la altura a 600 para acomodar los nuevos campos de costos
        self.root.geometry("500x600") 
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

            modelo = FabricaModelos.crear_modelo(
                tipo_modelo=datos["modelo"],
                lmbda=datos["lmbda"],
                mu=datos["mu"],
                s=datos["s"],
                sigma=datos["sigma"]
            )

            resultados = modelo.calcular()

            if datos["cw"] > 0 or datos["cs"] > 0:
                
                servidores_reales = datos["s"] if datos["modelo"] == "M/M/s" else 1
                
                lq_val = 0.0
                for clave, valor in resultados.items():
                    if "Lq" in clave:
                        lq_val = float(valor)
                        break
                
                costo_total = modelo.calcular_costo_total(servidores_reales, lq_val, datos["cw"], datos["cs"])
                
                resultados["Costo Total (CT)"] = f"${costo_total:.2f}"

            self.panel_resultados.mostrar_resultados(resultados)

        except ValueError as e:
            messagebox.showwarning("Aviso", str(e))
        except Exception as e:
            messagebox.showerror("Error crítico", f"Verifica los campos ingresados. Error: {str(e)}")

if __name__ == "__main__":
    ventana = tk.Tk()
    app = ControladorColas(ventana)
    ventana.mainloop()
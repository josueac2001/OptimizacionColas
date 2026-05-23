# views/interfaz.py
import tkinter as tk
from tkinter import ttk

class PanelEntradas(tk.LabelFrame):
    """Componente visual que maneja los campos de entrada."""
    def __init__(self, parent):
        super().__init__(parent, text="Parámetros del Sistema", padx=10, pady=10)
        
        # 1. Selector de Modelo ampliado
        tk.Label(self, text="Seleccione el Modelo:").grid(row=0, column=0, sticky="w", pady=5)
        self.combo_modelo = ttk.Combobox(self, values=["M/M/1", "M/M/s", "M/G/1", "M/D/1"], state="readonly", width=17)
        self.combo_modelo.current(0)
        self.combo_modelo.grid(row=0, column=1, pady=5)
        self.combo_modelo.bind("<<ComboboxSelected>>", self._gestionar_estado_campos)

        # 2. Tasa de llegadas (λ)
        tk.Label(self, text="Tasa de llegadas (λ):").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_lambda = tk.Entry(self, width=20)
        self.entry_lambda.grid(row=1, column=1, pady=5)

        # 3. Tasa de servicio (μ)
        tk.Label(self, text="Tasa de servicio (μ):").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_mu = tk.Entry(self, width=20)
        self.entry_mu.grid(row=2, column=1, pady=5)

        # 4. Número de Servidores (s)
        tk.Label(self, text="Número de servidores (s):").grid(row=3, column=0, sticky="w", pady=5)
        self.spin_s = ttk.Spinbox(self, from_=2, to=5, width=18)
        self.spin_s.set("1")
        self.spin_s.configure(state="disabled")
        self.spin_s.grid(row=3, column=1, pady=5)

        # 5. Desviación Estándar (σ) - Solo para M/G/1
        tk.Label(self, text="Desviación estándar (σ) [M/G/1]:").grid(row=4, column=0, sticky="w", pady=5)
        self.entry_sigma = tk.Entry(self, width=20)
        self.entry_sigma.insert(0, "0.0")
        self.entry_sigma.configure(state="disabled")
        self.entry_sigma.grid(row=4, column=1, pady=5)

    def _gestionar_estado_campos(self, event):
        modelo = self.combo_modelo.get()
        
        # Reseteo por defecto
        self.spin_s.configure(state="normal")
        self.spin_s.set("1")
        self.spin_s.configure(state="disabled")
        
        self.entry_sigma.configure(state="normal")
        self.entry_sigma.delete(0, tk.END)
        self.entry_sigma.insert(0, "0.0")
        self.entry_sigma.configure(state="disabled")

        # Activar según modelo
        if modelo == "M/M/s":
            self.spin_s.configure(state="normal")
            self.spin_s.set("2")
        elif modelo == "M/G/1":
            self.entry_sigma.configure(state="normal")
            self.entry_sigma.delete(0, tk.END)

    def obtener_datos(self):
        sigma_val = self.entry_sigma.get()
        if not sigma_val or sigma_val.strip() == "":
            sigma_val = "0.0"

        return {
            "modelo": self.combo_modelo.get(),
            "lmbda": float(self.entry_lambda.get()),
            "mu": float(self.entry_mu.get()),
            "s": int(self.spin_s.get()),
            "sigma": float(sigma_val)
        }

class PanelResultados(tk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Métricas Esperadas", padx=10, pady=10)
        self.texto_salida = tk.Text(self, height=8, font=("Courier", 10), bg="#2b2b2b", fg="#a9b7c6")
        self.texto_salida.pack(fill="both", expand=True)

    def mostrar_resultados(self, resultados):
        self.texto_salida.delete(1.0, tk.END)
        for clave, valor in resultados.items():
            self.texto_salida.insert(tk.END, f" {clave:<35} |  {valor}\n")
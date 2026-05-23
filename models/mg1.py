import math
from .base import ModeloCola

class ModeloMG1(ModeloCola):
    def __init__(self, lmbda, mu, sigma):
        super().__init__(lmbda, mu)
        self.sigma = float(sigma)

    def calcular(self):
        rho = self.lmbda / self.mu
        if rho >= 1:
            raise ValueError("Sistema inestable: λ debe ser menor que μ.")

        p0 = 1 - rho
        lq_exacto = ((self.lmbda**2) * (self.sigma**2) + (rho**2)) / (2 * (1 - rho))
        
        # Redondeo al mayor
        lq_aprox = math.ceil(lq_exacto)
        l_aprox = math.ceil(lq_aprox + rho)
        
        wq_aprox = lq_aprox / self.lmbda
        w_aprox = wq_aprox + (1 / self.mu)

        return {
            "Factor de Utilización (ρ)": f"{round(rho * 100, 1)} %",
            "Prob. sistema vacío (P0)": f"{round(p0 * 100, 1)} %",
            "Consultas esperadas en cola (Lq)": lq_aprox,
            "Consultas esperadas en sistema (L)": l_aprox,
            "Tiempo esperado en cola (Wq)": round(wq_aprox, 4),
            "Tiempo esperado en sistema (W)": round(w_aprox, 4)
        }
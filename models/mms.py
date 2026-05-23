import math
from .base import ModeloCola

class ModeloMMs(ModeloCola):
    def __init__(self, lmbda, mu, s):
        super().__init__(lmbda, mu)
        self.s = int(s)

    def calcular(self):
        rho = self.lmbda / (self.s * self.mu)
        if rho >= 1:
            raise ValueError(f"Sistema inestable: λ debe ser menor que {self.s} * μ.")

        sumatoria = sum([((self.lmbda / self.mu)**i) / math.factorial(i) for i in range(self.s)])
        termino_s = (((self.lmbda / self.mu)**self.s) / math.factorial(self.s)) * (1 / (1 - rho))
        p0 = 1 / (sumatoria + termino_s)

        lq_exacto = ((((self.lmbda / self.mu)**self.s) * rho) / (math.factorial(self.s) * ((1 - rho)**2))) * p0
        
        lq_aprox = math.ceil(lq_exacto)
        l_aprox = math.ceil(lq_aprox + (self.lmbda / self.mu))
        
        wq_aprox = lq_aprox / self.lmbda
        w_aprox = wq_aprox + (1 / self.mu)

        return {
            "Factor de Utilización (ρ)": f"{round(rho * 100, 1)} %",
            "Prob. sistema vacío (P0)": f"{round(p0 * 100, 1)} %",
            "Clientes esperados en cola (Lq)": lq_aprox,
            "Clientes esperados en sistema (L)": l_aprox,
            "Tiempo esperado en cola (Wq)": round(wq_aprox, 3),
            "Tiempo esperado en sistema (W)": round(w_aprox, 3)
        }
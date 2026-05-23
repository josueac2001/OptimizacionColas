from abc import ABC, abstractmethod

class ModeloCola(ABC):
    """Clase base abstracta para todos los modelos de colas."""
    def __init__(self, lmbda, mu):
        self.lmbda = float(lmbda)
        self.mu = float(mu)

    @abstractmethod
    def calcular(self):
        """Método que debe ser implementado por cada modelo específico."""
        pass

    def calcular_costo_total(self, s, Lq, cw, cs):
        """
        Calcula el costo total (CT) del sistema.
        s: número de servidores (1 para mm1, md1, mg1; 's' para mms)
        Lq: número promedio de clientes en cola
        cw: costo de espera por hora
        cs: costo de servicio por hora
        """
        costo_servicio = s * cs
        costo_espera = Lq * cw
        costo_total = costo_servicio + costo_espera
        
        return costo_total
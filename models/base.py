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
# models/fabric.py
from .mm1 import ModeloMM1
from .mms import ModeloMMs
from .mg1 import ModeloMG1
from .md1 import ModeloMD1

class FabricaModelos:
    """Clase encargada de instanciar el modelo correcto según el dropdown."""
    @staticmethod
    def crear_modelo(tipo_modelo, lmbda, mu, s=1, sigma=0.0):
        if tipo_modelo == "M/M/1":
            return ModeloMM1(lmbda, mu)
        
        elif tipo_modelo == "M/M/s":
            if 2 <= s <= 5:
                return ModeloMMs(lmbda, mu, s)
            else:
                raise ValueError("Para el modelo M/M/s, el número de servidores debe estar entre 2 y 5.")
                
        elif tipo_modelo == "M/G/1":
            return ModeloMG1(lmbda, mu, sigma)
            
        elif tipo_modelo == "M/D/1":
            return ModeloMD1(lmbda, mu)
            
        else:
            raise ValueError("Modelo no reconocido.")
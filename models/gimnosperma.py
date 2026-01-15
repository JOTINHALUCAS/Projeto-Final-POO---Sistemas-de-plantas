from planta import Planta

class Gimnosperma(Planta):
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida, tipo_semente):
        super().__init__(nome_cientifico, nome_popular, familia, habitat, ciclo_vida)
        self._tipo_semente = tipo_semente

    def classificar(self):
        return "Planta -> Gimnosperma"
    

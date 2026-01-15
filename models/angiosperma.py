from planta import Planta

class Angiosperma(Planta):
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida,tipo_flor):
        super().__init__(nome_cientifico,nome_popular,familia,habitat, ciclo_vida)
        self.tipo_flor = tipo_flor
        
    def classificar(self):
        return "Planta -> Angiosperma"
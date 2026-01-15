from angiosperma import Angiosperma

class Herbacea(Angiosperma):
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida, tipo_flor, uso_medicinal: bool):
        super().__init__(nome_cientifico, nome_popular, familia, habitat, ciclo_vida, tipo_flor)
        self._uso_medicinal = uso_medicinal
    
    def classificar(self):
        return "Planta -> Angiosperma -> Herbacea"
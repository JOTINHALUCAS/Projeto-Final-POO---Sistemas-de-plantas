from angiosperma import Angiosperma

class Arbusto(Angiosperma):
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida, tipo_flor, ramificacao):
        super().__init__(nome_cientifico, nome_popular, familia, habitat, ciclo_vida, tipo_flor)
        self._ramificacao = ramificacao
        
    def classificar(self):
        return "Planta -> Angiosperma -> Arbusto"
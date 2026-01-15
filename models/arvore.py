from angiosperma import Angiosperma

class Arvore(Angiosperma):
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida, tipo_flor, porte, produz_fruto:bool):
        super().__init__(nome_cientifico, nome_popular, familia, habitat, ciclo_vida,tipo_flor)
        self._porte = porte
        self._produz_fruto = produz_fruto

    def classificar(self):
        return "Arvore"

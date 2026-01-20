from models.angiosperma import Angiosperma

class Arvore(Angiosperma):
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida, porte, produz_fruto:bool):
        super().__init__(nome_cientifico, nome_popular, familia, habitat, ciclo_vida)
        self._porte = porte
        self._produz_fruto = produz_fruto

    def classificar(self):
        return super().classificar()
    
    def descrever(self):
        return (
            f"Essa é uma planta do tipo Árvore (Angiosperma), "
            f"com nome popular {self._nome_popular}, "
            f"da família {self._familia} "
            f"e nome científico {self._nome_cientifico}."
        )

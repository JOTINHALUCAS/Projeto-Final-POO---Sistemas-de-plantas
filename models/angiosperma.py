from models.planta import Planta

class Angiosperma(Planta):
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida):
        super().__init__(nome_cientifico,nome_popular,familia,habitat, ciclo_vida)
 
    def classificar(self):
        return super().classificar() + '\nTipo: Angiosperma'

    def descrever(self):
        return (
            f"Essa é uma planta do grupo Angiosperma, "
            f"com nome popular {self._nome_popular}, "
            f"da família {self._familia} "
            f"e nome científico {self._nome_cientifico}."
        )
    
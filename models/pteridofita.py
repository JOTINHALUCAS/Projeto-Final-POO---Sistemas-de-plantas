from models.planta import Planta

class Pteridofita(Planta):
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida, possui_esporros=True):
        super().__init__(nome_cientifico, nome_popular, familia, habitat, ciclo_vida)
        self._possui_esporos = possui_esporros

    def classificar(self):
        return (
            super().classificar() +
            '\nGrupo: Pteridófita\n'
            'Reprodução por esporos'
        )

    def descrever(self):
        return (
            f"Essa é uma planta do grupo Pteridófita, "
            f"com nome popular {self._nome_popular}, "
            f"da família {self._familia} "
            f"e nome científico {self._nome_cientifico}."
        )
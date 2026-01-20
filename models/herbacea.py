from models.angiosperma import Angiosperma

class Herbacea(Angiosperma):
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida, uso_medicinal: bool):
        super().__init__(nome_cientifico, nome_popular, familia, habitat, ciclo_vida)
        self._uso_medicinal = uso_medicinal
    
    def classificar(self):
        return (
            super().classificar() +
            '\nCategoria: Herbácea\n'
            f'Uso medicinal: {"Sim" if self._uso_medicinal else "Não"}'
        )

    def descrever(self):
        return (
            f"Essa é uma planta do tipo Herbácea (Angiosperma), "
            f"com nome popular {self._nome_popular}, "
            f"da família {self._familia} "
            f"e nome científico {self._nome_cientifico}."
        )

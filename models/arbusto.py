from models.angiosperma import Angiosperma

class Arbusto(Angiosperma):
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida, ramificacao):
        super().__init__(nome_cientifico, nome_popular, familia, habitat, ciclo_vida)
        self._ramificacao = ramificacao
        
    def classificar(self):
        return (
            super().classificar() +
            f'\nCategoria: Arbusto\n'
            f'Ramificação: {self._ramificacao}'
        )

    def descrever(self):
        return (
            f"Essa é uma planta do tipo Arbusto (Angiosperma), "
            f"com nome popular {self._nome_popular}, "
            f"da família {self._familia} "
            f"e nome científico {self._nome_cientifico}."
        )
        
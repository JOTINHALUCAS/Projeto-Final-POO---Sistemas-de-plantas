from planta import Planta

class Gimnosperma(Planta):
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida, tipo_semente):
        super().__init__(nome_cientifico, nome_popular, familia, habitat, ciclo_vida)
        self._tipo_semente = tipo_semente

    def classificar(self):
        return (
            super().classificar() +
            '\nGrupo: Gimnosperma\n'
            f'Tipo de semente: {self._tipo_semente}'
        )

    def descrever(self):
        return (
            f"Essa é uma planta do grupo Gimnosperma, "
            f"com nome popular {self._nome_popular}, "
            f"da família {self._familia} "
            f"e nome científico {self._nome_cientifico}."
        )
    
    

    

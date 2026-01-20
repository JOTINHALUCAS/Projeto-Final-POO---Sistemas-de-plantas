from models.planta import Planta

class Briofita(Planta):
    def __init__(self,nome_cientifico,nome_popular, habitat, ciclo_vida, possui_vassos = False):
        super().__init__(self, nome_cientifico, nome_popular, habitat,ciclo_vida)
        self._possui_vaso = possui_vassos

    def classificar(self):
        return super().classificar()

    def descrever(self):
        return (
            super().descrever() + '\n'
            f'Possui vasos condutores: {"Sim" if self._possui_vasos else "Não"}\n'
            'Reprodução por esporos\n'
            'Não possui sementes, flores ou frutos'
    )
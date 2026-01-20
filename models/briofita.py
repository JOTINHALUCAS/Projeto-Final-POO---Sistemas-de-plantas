from models.planta import Planta

class Briofita(Planta):
    def __init__(self,nome_cientifico,nome_popular, familia, habitat, ciclo_vida, possui_vasso= False):
        super().__init__(nome_cientifico, nome_popular, familia, habitat,ciclo_vida)
        self._possui_vaso = possui_vasso

    def classificar(self):
        return super().classificar()

    def descrever(self):
        return (
            f'Essa é uma planta do Reino Plantae, '
            f'com nome popular {self._nome_popular}, '
            f'da família {self._familia} e '
            f'nome científico {self._nome_cientifico}.\n'
            f'Possui vasos condutores: {"Sim" if self._possui_vaso else "Não"}\n'
            f'Reprodução por esporos\n'
            f'Não possui sementes, flores ou frutos'
        )
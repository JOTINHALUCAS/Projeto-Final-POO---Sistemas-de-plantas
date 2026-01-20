class Planta:
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida):
        self._nome_cientifico = nome_cientifico
        self._nome_popular = nome_popular
        self._familia = familia
        self._habitat = habitat
        self._ciclo_vida = ciclo_vida

    def descrever(self):
        return (
            f"Essa é uma planta do Reino Plantae, "
            f"com nome popular {self._nome_popular}, "
            f"da família {self._familia} "
            f"e nome científico {self._nome_cientifico}."
        )

    def classificar(self):
        return(
            f'Nome Popular: {self._nome_popular}\n'
            f'Nome científico: {self._nome_cientifico}\n'
            f'Família: {self._familia}\n'
            f'Habitat: {self._habitat}\n'
            f'Ciclo de vida: {self._ciclo_vida}'
        )
        
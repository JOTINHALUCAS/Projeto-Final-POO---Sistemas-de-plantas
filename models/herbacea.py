from models.angiosperma import Angiosperma

class Herbacea(Angiosperma):
    def __init__(self, nome_cientifico, nome_popular, familia, habitat, ciclo_vida, uso_medicinal: bool, produz_fruto: bool):
        super().__init__(nome_cientifico, nome_popular, familia, habitat, ciclo_vida)
        self._uso_medicinal = uso_medicinal
        self._produz_fruto = produz_fruto
    
    def classificar(self):
        
        partes = [
            super().classificar(),
            'Categoria: Herbácea',
            f'Uso medicinal (s/n): {"s" if self._uso_medicinal else "n"}',
            f'Produz fruto (s/n): {"s" if self._produz_fruto else "n"}'
        ]
        return '\n'.join(partes)


    def descrever(self):
        return (
            f"Essa é uma planta do tipo Herbácea (Angiosperma), "
            f"com nome popular {self._nome_popular}, "
            f"da família {self._familia} "
            f"e nome científico {self._nome_cientifico}."
        )

from models.arvore import Arvore
from models.arbusto import Arbusto
from models.herbacea import Herbacea

jatoba = Arvore(
    "Hymenaea courbaril",
    "Jatobá",
    "Fabaceae",
    "Florestas tropicais",
    "Longo",
    "Flor branca",
    "Grande",
    True
)

cajueiro = Arvore(
    "Anacardium occidentale",
    "Cajueiro",
    "Anacardiaceae",
    "Caatinga",
    "Perene",
    "Flor branca",
    "Médio",
    True
)

aroeira = Arbusto(
    "Myracrodruon urundeuva",
    "Aroeira",
    "Anacardiaceae",
    "Caatinga",
    "Perene",
    "Flor pequena",
    "Alta"
)

mandacaru = Herbacea(
    "Cereus jamacaru",
    "Mandacaru",
    "Cactaceae",
    "Caatinga",
    "Perene",
    "Flor branca",
    True
)

manaca_da_serra = Arbusto(
    "Tibouchina mutabilis",
    "Manacá-da-serra",
    "Melastomataceae",
    "Mata úmida",
    "Perene",
    "Flor roxa",
    "Desde a base"
)

plantas = [jatoba, cajueiro, aroeira, mandacaru, manaca_da_serra]

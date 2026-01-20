from models.arvore import Arvore
from models.arbusto import Arbusto
from models.herbacea import Herbacea
from models.briofita import Briofita
from models.pteridofita import Pteridofita
from models.gimnosperma import Gimnosperma

arvores = [
    Arvore("Hymenaea courbaril", "Jatobá", "Fabaceae", "Florestas tropicais", "Longo", "Grande", True),
    Arvore("Anacardium occidentale", "Cajueiro", "Anacardiaceae", "Caatinga", "Perene", "Médio", True),
    Arvore("Copernicia prunifera", "Carnaúba", "Arecaceae", "Caatinga", "Perene", "Alto", False),
    Arvore("Myracrodruon urundeuva", "Aroeira", "Anacardiaceae", "Caatinga", "Perene", "Grande", False),
    Arvore("Amburana cearensis", "Cumaru", "Fabaceae", "Caatinga", "Perene", "Médio", False),
    Arvore("Tabebuia aurea", "Craibeira", "Bignoniaceae", "Caatinga", "Perene", "Médio", False),
    Arvore("Aspidosperma pyrifolium", "Pereiro", "Apocynaceae", "Caatinga", "Perene", "Médio", False),
    Arvore("Poincianella pyramidalis", "Catingueira", "Fabaceae", "Caatinga", "Perene", "Médio", False),
    Arvore("Licania rigida", "Oiticica", "Chrysobalanaceae", "Mata ciliar", "Perene", "Grande", True),
    Arvore("Spondias tuberosa", "Umbuzeiro", "Anacardiaceae", "Caatinga", "Perene", "Médio", True)
]

arbustos = [
    Arbusto("Croton sonderianus", "Marmeleiro", "Euphorbiaceae", "Caatinga", "Perene", "Desde a base"),
    Arbusto("Jatropha mollissima", "Pinhão-bravo", "Euphorbiaceae", "Caatinga", "Perene", "Baixa"),
    Arbusto("Mimosa tenuiflora", "Jurema-preta", "Fabaceae", "Caatinga", "Perene", "Densa"),
    Arbusto("Cordia leucocephala", "Moleque-duro", "Boraginaceae", "Caatinga", "Perene", "Irregular"),
    Arbusto("Baccharis trimera", "Carqueja", "Asteraceae", "Caatinga", "Perene", "Alta"),
    Arbusto("Maytenus rigida", "Bom-nome", "Celastraceae", "Caatinga", "Perene", "Compacta"),
    Arbusto("Lippia gracilis", "Alecrim-do-sertão", "Verbenaceae", "Caatinga", "Perene", "Baixa"),
    Arbusto("Cnidoscolus quercifolius", "Faveleira", "Euphorbiaceae", "Caatinga", "Perene", "Espalhada"),
    Arbusto("Solanum paniculatum", "Jurubeba", "Solanaceae", "Caatinga", "Perene", "Alta"),
    Arbusto("Turnera subulata", "Chanana", "Passifloraceae", "Caatinga", "Perene", "Baixa")
]

herbaceas = [
    Herbacea("Cereus jamacaru", "Mandacaru", "Cactaceae", "Caatinga", "Perene", False),
    Herbacea("Opuntia ficus-indica", "Palma-forrageira", "Cactaceae", "Caatinga", "Perene", True),
    Herbacea("Aloe vera", "Babosa", "Asphodelaceae", "Cultivo", "Perene", True),
    Herbacea("Portulaca oleracea", "Beldroega", "Portulacaceae", "Caatinga", "Anual", True),
    Herbacea("Chenopodium ambrosioides", "Mastruz", "Amaranthaceae", "Caatinga", "Perene", True),
    Herbacea("Cymbopogon citratus", "Capim-santo", "Poaceae", "Cultivo", "Perene", True),
    Herbacea("Ocimum basilicum", "Manjericão", "Lamiaceae", "Cultivo", "Anual", True),
    Herbacea("Mentha spicata", "Hortelã", "Lamiaceae", "Cultivo", "Perene", True),
    Herbacea("Bidens pilosa", "Picão-preto", "Asteraceae", "Caatinga", "Anual", True),
    Herbacea("Peperomia pellucida", "Erva-de-jabuti", "Piperaceae", "Úmido", "Anual", True)
]

briofitas = [
    Briofita("Sphagnum palustre", "Musgo-do-brejo", "Sphagnaceae", "Ambiente úmido", "Perene"),
    Briofita("Polytrichum commune", "Musgo-cabeludo", "Polytrichaceae", "Solo úmido", "Perene"),
    Briofita("Marchantia polymorpha", "Hepática", "Marchantiaceae", "Ambiente sombreado", "Perene"),
    Briofita("Bryum argenteum", "Musgo-prateado", "Bryaceae", "Ambiente urbano", "Perene"),
    Briofita("Riccia fluitans", "Riccia", "Ricciaceae", "Ambiente aquático", "Perene"),
]

pteridofitas = [
    Pteridofita("Nephrolepis exaltata", "Samambaia", "Nephrolepidaceae", "Ambiente úmido", "Perene"),
    Pteridofita("Adiantum capillus-veneris", "Avenca", "Pteridaceae", "Ambiente sombreado", "Perene"),
    Pteridofita("Pteridium aquilinum", "Samambaia-do-campo", "Dennstaedtiaceae", "Campos", "Perene"),
    Pteridofita("Equisetum giganteum", "Cavalinha", "Equisetaceae", "Áreas alagadas", "Perene"),
    Pteridofita("Selaginella kraussiana", "Selaginela", "Selaginellaceae", "Ambiente úmido", "Perene"),
]

gimnospermas = [
    Gimnosperma("Araucaria angustifolia", "Araucária", "Araucariaceae", "Região serrana", "Perene", "Semente nua"),
    Gimnosperma("Pinus elliottii", "Pinus", "Pinaceae", "Florestas plantadas", "Perene", "Semente nua"),
    Gimnosperma("Cycas revoluta", "Cica", "Cycadaceae", "Jardins", "Perene", "Semente nua"),
    Gimnosperma("Ginkgo biloba", "Ginkgo", "Ginkgoaceae", "Urbano", "Perene", "Semente nua"),
    Gimnosperma("Cupressus sempervirens", "Cipreste", "Cupressaceae", "Cultivo", "Perene", "Semente nua"),
]


plantas = arvores + arbustos + herbaceas + briofitas + pteridofitas + gimnospermas

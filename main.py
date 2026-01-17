from data.plantas_ceara import plantas
#1from models.angiosperma import Angiosperma
from models.arbusto import Arbusto
from models.arvore import Arvore
#from models.gimnosperma import Gimnosperma
from models.herbacea import Herbacea
#from models.planta import Planta

def menu():
    print('\n 1 - Listar plantas')
    print('\n 2 - Cadastrar planta')
    print('\n 0 - Sair')
print('--'*40)

while True:
    menu()
    op = input('Digite um núemro acima:')
    if op == '1':
        for planta in plantas:
            print(f'- {planta.classificar()}')
            print('--'*40)

    elif op == '2':
        tipo = input('Tipo ("Arvore, Arbusto, Herbacea")').lower()
        nome_popular = input('Nome popular:')
        nome_cientifico = input('Nome cientifico:')
        familia = input('Familia:')
        habitat = input('Habitat:')
        ciclo_vida = input('Ciclo de vida:')

        if tipo == 'arvore':
            porte = input('Porte:')
            fruto = input('Fruto:') == "s"
            nova_planta = Arvore(nome_popular,nome_cientifico,familia,habitat,ciclo_vida,porte,fruto)

        elif tipo == 'arbusto':
            ramificacao = input('Ramificação:')
            nova_planta = Arbusto(nome_popular,nome_cientifico,familia,habitat,ciclo_vida,ramificacao)

        elif tipo == 'herbacea':
            medicinal = input('Possui uso medecinal: ') == 's'
            nova_planta = Herbacea(nome_popular,nome_cientifico,familia,habitat,ciclo_vida,medicinal)

        plantas.append(nova_planta)
        print('Planta cadastrada com sucesso.')

    elif op == '0':
        print('Saindo...')
        break

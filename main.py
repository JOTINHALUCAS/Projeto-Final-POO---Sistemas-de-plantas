from data.plantas_ceara import plantas
#1from models.angiosperma import Angiosperma
from models.arbusto import Arbusto
from models.arvore import Arvore
#from models.gimnosperma import Gimnosperma
from models.herbacea import Herbacea
import json


def menu():
    print('1 - Listar plantas')
    print('2 - Cadastrar planta')
    print('3 - Procurar planta')
    print('0 - Sair')
print('--'*40)

def salvar_planta(nova_planta):
    try:
        with open("data/plantas_usuario.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = []

    base = {
        "tipo": nova_planta.__class__.__name__,
        "nome_cientifico": nova_planta._nome_cientifico,
        "nome_popular": nova_planta._nome_popular,
        "familia": nova_planta._familia,
        "habitat": nova_planta._habitat,
        "ciclo_vida": nova_planta._ciclo_vida,
    }

    if isinstance(nova_planta, Arvore):
        base["porte"] = nova_planta._porte
        base["produz_fruto"] = nova_planta._produz_fruto

    elif isinstance(nova_planta, Arbusto):
        base["ramificacao"] = nova_planta._ramificacao

    elif isinstance(nova_planta, Herbacea):
        base["uso_medicinal"] = nova_planta._uso_medicinal

    dados.append(base)

    with open("data/plantas_usuario.json", "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

def carregar_plantas_usuario():
    try:
        with open("data/plantas_usuario.json", "r", encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        return []

    lista = []

    for p in dados:
        if p["tipo"] == "Arvore":
            lista.append(
                Arvore(
                    p["nome_cientifico"],
                    p["nome_popular"],
                    p["familia"],
                    p["habitat"],
                    p["ciclo_vida"],
                    p.get("porte", "desconhecido"),
                    p.get("produz_fruto", False)
                )
            )
        elif p["tipo"] == "Arbusto":
            lista.append(
                Arbusto(
                    p["nome_cientifico"],
                    p["nome_popular"],
                    p["familia"],
                    p["habitat"],
                    p["ciclo_vida"],
                    p["ramificacao"]
                )
            )
        elif p["tipo"] == "Herbacea":
            lista.append(
                Herbacea(
                    p["nome_cientifico"],
                    p["nome_popular"],
                    p["familia"],
                    p["habitat"],
                    p["ciclo_vida"],
                    p["uso_medicinal"]
                )
            )

    return lista

def listar_planta():
    print('---'*50)
    for j , planta in enumerate(plantas, start=1):
        print(f'[{j}] - {planta.descrever()}')
    print('---'*50)

def procurar_planta():
    print('---'*50)
    nome_proc = input('Qual planta você deseja encontrar: ').capitalize().strip()
    encontrada = False

    for planta in plantas:
        if nome_proc in planta._nome_popular:
            print('\nPlanta encontrada!! ')
            print(planta.classificar())
            encontrada = True

    if not encontrada:
        print('Não existe essa planta, cadastre ela!!')
    print('---'*50)

plantas = plantas + carregar_plantas_usuario()

while True:
    menu()
    op = input('Digite um número acima:')
    if op == '1':
        listar_planta()

    elif op == '2':
        tipo = input('Tipo ("Arvore, Arbusto, Herbacea")').capitalize()
        nome_popular = input('Nome popular:').capitalize()
        nome_cientifico = input('Nome cientifico:').capitalize()
        familia = input('Familia:').capitalize()
        habitat = input('Habitat:').capitalize()
        ciclo_vida = input('Ciclo de vida:').capitalize()

        if tipo == 'Arvore':
            porte = input('Porte:')
            produz_fruto = input('Fruto:').lower() == "s"
            nova_planta = Arvore(
                nome_popular=nome_popular,
                nome_cientifico=nome_cientifico,
                familia=familia,
                habitat=habitat,
                ciclo_vida=ciclo_vida,
                porte=porte,
                produz_fruto=produz_fruto
                )

        elif tipo == 'Arbusto':
            ramificacao = input('Ramificação:').capitalize()
            nova_planta = Arbusto(
                nome_popular=nome_popular,
                nome_cientifico=nome_cientifico,
                familia=familia,
                habitat=habitat,
                ciclo_vida=ciclo_vida,
                ramificacao=ramificacao
                )

        elif tipo == 'Herbacea':
            medicinal = input('Possui uso medecinal: ') == 's'
            nova_planta = Herbacea(
                nome_popular=nome_popular,
                nome_cientifico=nome_cientifico,
                familia=familia,
                habitat=habitat,
                ciclo_vida=ciclo_vida,
                medicinal=medicinal
                )
        else:
            print('Tipo invalido')

        plantas.append(nova_planta)
        salvar_planta(nova_planta)
        print('Planta cadastrada com sucesso.')

    elif op == '3':
        procurar_planta()

    elif op == '0':
        print('Saindo...')
        break

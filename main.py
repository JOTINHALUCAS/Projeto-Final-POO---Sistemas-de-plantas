from data.plantas_ceara import plantas
from models.arbusto import Arbusto
from models.arvore import Arvore
from models.gimnosperma import Gimnosperma
from models.herbacea import Herbacea
from models.briofita import Briofita
from models.pteridofita import Pteridofita
import json


def menu():
    print('1 - Listar plantas')
    print('2 - Cadastrar planta')
    print('3 - Procurar planta')
    print('0 - Sair')

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
        base["produz_fruto"] = nova_planta._produz_fruto

    elif isinstance(nova_planta, Pteridofita):
        base["possui_esporos"] = nova_planta._possui_esporos

    elif isinstance(nova_planta, Gimnosperma):
        base["tipo_semente"] = nova_planta._tipo_semente

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
        if p["tipo"] == "Arvore" or p["tipo"] == "1":
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
        elif p["tipo"] == "Arbusto" or p["tipo"] == "2":
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
        elif p["tipo"] == "Herbacea" or p["tipo"] == "3":
            lista.append(
                Herbacea(
                    p["nome_cientifico"],
                    p["nome_popular"],
                    p["familia"],
                    p["habitat"],
                    p["ciclo_vida"],
                    p["uso_medicinal"],
                    p.get("produz_fruto", False)
                )
            )

        elif p["tipo"] == "Briofita" or p["tipo"] == "4":
            lista.append(
                Briofita(
                    p["nome_cientifico"],
                    p["nome_popular"],
                    p["familia"],
                    p["habitat"],
                    p["ciclo_vida"]
                )
            )

        elif p["tipo"] == "Pteridofita" or p["tipo"] == "5":
            lista.append(
                Pteridofita(
                    p["nome_cientifico"],
                    p["nome_popular"],
                    p["familia"],
                    p["habitat"],
                    p["ciclo_vida"],
                    p.get("possui_esporos", True)
                )
            )

        elif p["tipo"] == "Gimnosperma" or p["tipo"] == "6":
            lista.append(
                Gimnosperma(
                    p["nome_cientifico"],
                    p["nome_popular"],
                    p["familia"],
                    p["habitat"],
                    p["ciclo_vida"],
                    p["tipo_semente"]
                )
            )
    return lista

plantas = plantas + carregar_plantas_usuario()

def listar_planta():
    print('---'*50)
    for j , planta in enumerate(plantas, start=1):
        print(f'[{j}] - {planta.descrever()}')
        print('---'*60)  

def procurar_planta():
    print('---'*50)
    nome_proc = input('Qual planta você deseja encontrar (nome popular): ').capitalize().strip()
    encontrada = False

    for planta in plantas:
        if nome_proc in planta._nome_popular and nome_proc == planta._nome_popular:
            print('\nPlanta encontrada!! ')
            print(planta.classificar())
            encontrada = True

    if not encontrada:
        print('Não existe essa planta no sistema, cadastre ela!!')
    print('---'*50)



while True:
    menu()
    op = input('Digite um número acima:')
    if op == '1':
        listar_planta()

    elif op == '2':
        tipo = input('Tipo ("1 - Arvore, 2 - Arbusto, 3 - Herbacea, 4 - Briofita, 5 - Pteridofita, 6 - Gimnosperma"): ').capitalize()
        nome_popular = input('Nome popular:').capitalize()
        nome_cientifico = input('Nome cientifico:').capitalize()
        familia = input('Familia:').capitalize()
        habitat = input('Habitat:').capitalize()
        ciclo_vida = input('Ciclo de vida:').capitalize()

        if tipo == 'Arvore' or tipo == '1':
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

        elif tipo == 'Arbusto' or tipo == '2':
            ramificacao = input('Ramificação:').capitalize()
            nova_planta = Arbusto(
                nome_popular=nome_popular,
                nome_cientifico=nome_cientifico,
                familia=familia,
                habitat=habitat,
                ciclo_vida=ciclo_vida,
                ramificacao=ramificacao
                )

        elif tipo == 'Herbacea' or tipo == '3':
            uso_medicinal = input('Possui uso medecinal(s/n): ') == 's'
            produz_fruto = input('Produz fruto (s/n): ') =='s'
            nova_planta = Herbacea(
                nome_popular=nome_popular,
                nome_cientifico=nome_cientifico,
                familia=familia,
                habitat=habitat,
                ciclo_vida=ciclo_vida,
                uso_medicinal=uso_medicinal,
                produz_fruto=produz_fruto
                )
            
        elif tipo == "Briofita" or tipo =='4':
            nova_planta = Briofita(
                nome_cientifico= nome_cientifico,
                nome_popular = nome_popular,
                familia=familia,
                habitat=habitat,
                ciclo_vida=ciclo_vida
            )

        elif tipo == "Pteridofita" or tipo == '5':
            possui_esporos = input('Possui esporos?(s/n) ').lower() =='s'
            nova_planta = Pteridofita(
                nome_cientifico=nome_cientifico,
                nome_popular=nome_popular,
                familia=familia,
                habitat=habitat,
                ciclo_vida=ciclo_vida,
                possui_esporos= possui_esporos
            )

        elif tipo == 'Gimnosperma' or tipo == '6':
            tipo_semente = input('Tipo de semente: ').capitalize().strip()
            nova_planta = Gimnosperma(
                nome_cientifico=nome_cientifico,
                nome_popular=nome_popular,
                familia=familia,
                habitat=habitat,
                ciclo_vida=ciclo_vida,
                tipo_semente=tipo_semente
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

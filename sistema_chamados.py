import datetime
import os

# Cores ANSI
COR_RESET = "\033[0m" 
COR_VERDE = "\033[32m"
COR_AMARELO = "\033[33m"
COR_VERMELHO = "\033[31m"
COR_CIANO = "\033[36m"
COR_ROXO = "\033[35m"
COR_BRANCO = "\033[37m"

chamados = []

# Matriz para os setores
setores = ["ti", "manutenção", "rh", "financeiro", "marketing"]
matriz_setores = {setor: {"abertos": 0, "resolvidos": 0, "urgencias": {"baixa": 0, "média": 0, "alta": 0}} for setor in setores}

#Gera um id
def gerar_id(): 
    return len(chamados) + 1

#Função auxiliar para a urgência do chamado
def pedir_urgencia():
    opcoes_validas = ["baixa", "média", "alta"]
    while True:
        urgencia = input(f"{COR_CIANO}\nUrgência (baixa/media/alta): {COR_RESET}").strip().lower()
        if urgencia == "media": urgencia = "média"
        if urgencia in opcoes_validas:
            return urgencia
        else:
            print(f"{COR_VERMELHO}\nUrgência inválida! Digite 'baixa', 'media' ou 'alta'.{COR_RESET}")    

#Atualiza a matriz
def atualizar_matriz_setores(chamado, status):
    setor = chamado["setor"]
    if setor in matriz_setores:
        if status == "Aberto":
            matriz_setores[setor]["abertos"] += 1
            matriz_setores[setor]["urgencias"][chamado["urgencia"]] += 1
        elif status == "Resolvido":
            matriz_setores[setor]["resolvidos"] += 1

#Abre o chamado completo
def abrir_chamado():
    os.system("cls")
    print(f"{COR_CIANO}\n--- ABRIR NOVO CHAMADO ---{COR_RESET}")
    setor = ''
    while setor not in matriz_setores:
        print(f"\n{COR_AMARELO}Setores Disponíveis:{COR_RESET}")
        for i in setores: print(f" ➤  {i.capitalize()}")
        setor = input(f"\n{COR_CIANO}Setor responsável: {COR_RESET}").lower()
        if setor not in matriz_setores:
            print(f"{COR_VERMELHO}\n⚠️ Setor inválido!{COR_RESET}")

    descricao = input(f"\n{COR_CIANO}Descrição do problema: {COR_RESET}")
    urgencia = pedir_urgencia()
    horario = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    status = "Aberto"

    chamado = {
        "id": gerar_id(),
        "setor": setor,
        "descricao": descricao,
        "urgencia": urgencia,
        "horario": horario,
        "status": status
    }

    chamados.append(chamado)
    atualizar_matriz_setores(chamado, status)
    os.system("cls")
    print(f"{COR_VERDE}\n--- Chamado registrado com sucesso! ---{COR_RESET}")

#Lista todos os chamados
def listar_chamados():
    if not chamados:
        os.system("cls")
        print(f"{COR_VERMELHO}\n--- Nenhum chamado registrado ainda! ---{COR_RESET}")
        return

    os.system("cls")
    print(f"{COR_CIANO}\n--- LISTA DE CHAMADOS ---{COR_RESET}")
    for chamado in chamados:
        print(f"🆔 ID: {COR_AMARELO}{chamado['id']}{COR_RESET} | 🏢 Setor: {COR_AMARELO}{chamado['setor'].capitalize()}{COR_RESET} | 🚨 Urgência: {COR_AMARELO}{chamado['urgencia'].capitalize()}{COR_RESET} | 🔖 Status: {COR_AMARELO}{chamado['status']}{COR_RESET}")
        print(f"Descrição: {chamado['descricao']}")
        print(f"Horário: {chamado['horario']}")
        print("-" * 30)

#Faz a checagem de quantos chamados estão abertos
def checar_chamados_abertos():
    chamados_abertos = [chamado for chamado in chamados if chamado["status"] == "Aberto"]
    return (chamados_abertos)

#Mostra apenas os chamados abertos
def listar_chamados_abertos():
    os.system("cls")
    print(f"{COR_CIANO}\n--- LISTA DE CHAMADOS ABERTOS ---{COR_RESET}")
    if not checar_chamados_abertos():
        print(f"{COR_VERMELHO}\n--- Nenhum chamado aberto registrado! ---{COR_RESET}")
        return

    for chamado in chamados:
        if chamado["status"] == "Aberto":
            print(f"🆔 ID: {COR_AMARELO}{chamado['id']}{COR_RESET} | 🏢 Setor: {COR_AMARELO}{chamado['setor'].capitalize()}{COR_RESET} | 🚨 Urgência: {COR_AMARELO}{chamado['urgencia'].capitalize()}{COR_RESET} | 🔖 Status: {COR_AMARELO}{chamado['status']}{COR_RESET}")
            print(f"Descrição: {chamado['descricao']}")
            print(f"Horário: {chamado['horario']}")
            print("-" * 30)

#Filtragem por urgência
def filtrar_urgencia():
    os.system("cls")
    opcoes_validas = ["baixa", "média", "alta"]
    urgencia = ""
    if not chamados:
        print(f"{COR_VERMELHO}\n--- Nenhum chamado registrado ainda! ---{COR_RESET}")
        return
    while urgencia not in opcoes_validas:
        urgencia = input(f"{COR_CIANO}Digite o nível de urgência para filtrar (baixa/média/alta): {COR_RESET}").strip().lower() 
        if urgencia == "media": urgencia = "média"

    print(f"\n{COR_CIANO}--- FILTRANDO CHAMADOS COM URGÊNCIA: {urgencia.lower()} ---{COR_RESET}")
    for chamado in chamados:
        if chamado["urgencia"].lower() == urgencia.lower():
            print(f"🆔 ID: {COR_AMARELO}{chamado['id']}{COR_RESET} | 🏢 Setor: {COR_AMARELO}{chamado['setor'].capitalize()}{COR_RESET} | 🚨 Urgência: {COR_AMARELO}{chamado['urgencia'].capitalize()}{COR_RESET} | 🔖 Status: {COR_AMARELO}{chamado['status']}{COR_RESET}")
            print(f"Descrição: {chamado['descricao']}")
            print(f"Horário: {chamado['horario']}")
            print("-" * 30)

#Fecha os chamados
def fechar_chamado():
    os.system("cls")
    if not checar_chamados_abertos():
        print (f"\n{COR_VERMELHO}Não há chamados abertos no momento!{COR_RESET}")
        return
    listar_chamados_abertos()

    id_procura = input(f"{COR_CIANO}Digite o ID do chamado a ser fechado: {COR_RESET}")
    if not id_procura.isdigit():
        print(f"{COR_VERMELHO}ID inválido. Digite um número inteiro.{COR_RESET}")
        return
    id_procura = int(id_procura)

    for chamado in chamados:
        if chamado["id"] == id_procura and chamado["status"] == "Aberto":
            chamado["status"] = "Resolvido"
            atualizar_matriz_setores(chamado, "Resolvido")
            os.system("cls")
            print(f"{COR_VERDE}Chamado fechado com sucesso.{COR_RESET}")
            return

    os.system("cls")
    print(f"{COR_VERMELHO}Chamado não encontrado ou já fechado.{COR_RESET}")

#Fecha todos os chamados
def fim_do_dia():
    os.system("cls")
    abertos = [c for c in chamados if c["status"] == "Aberto"]
    if not abertos:
        print(f"{COR_VERDE}\nTodos os chamados foram encerrados!{COR_RESET}")
        return

    chamado = abertos[0]
    chamado["status"] = "Resolvido"
    atualizar_matriz_setores(chamado, "Resolvido")
    print(f"{COR_VERDE}Chamado ID {chamado['id']} resolvido.{COR_RESET}")

    fim_do_dia()

#Conta os chamados com len
def contador_de_chamados():
    abertos = len([c for c in chamados if c["status"] == "Aberto"])
    resolvidos = len([c for c in chamados if c["status"] == "Resolvido"])
    total = len(chamados)
    print(f"{COR_CIANO}\n📋 Total de chamados: {total} | 🟢 Abertos: {abertos} | ✅ Resolvidos: {resolvidos}\n{COR_RESET}")

#Exibe a matriz referente a cada setor
def exibir_matriz_setores():
    os.system("cls")
    print(f"{COR_CIANO}\n--- MATRIZ DE CHAMADOS POR SETOR ---{COR_RESET}")
    for setor, dados in matriz_setores.items():
        print(f"\n{COR_AMARELO}Setor: {setor}{COR_RESET}")
        print(f"📈 Abertos: {dados['abertos']} | ✅ Resolvidos: {dados['resolvidos']}")
        print(f"Urgências: Baixa: {dados['urgencias']['baixa']} | Média: {dados['urgencias']['média']} | Alta: {dados['urgencias']['alta']}")
        print("-" * 30)

#Menu
def menu():
    while True:
        print(f"\n{COR_VERDE}" + "=" * 40)
        print('''
 ██████╗  ██████╗     ████████╗ █████╗ ███████╗██╗  ██╗
██╔════╝ ██╔═══██╗    ╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝
██║  ███╗██║   ██║       ██║   ███████║███████╗█████╔╝ 
██║   ██║██║   ██║       ██║   ██╔══██║╚════██║██╔═██╗ 
╚██████╔╝╚██████╔╝       ██║   ██║  ██║███████║██║  ██╗
 ╚═════╝  ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝''')


        print("=" * 40 + f"{COR_RESET}")

        contador_de_chamados()

        print(f"{COR_CIANO}1️⃣  Abrir chamado{COR_RESET}")
        print(f"{COR_CIANO}2️⃣  Listar todos os chamados{COR_RESET}")
        print(f"{COR_CIANO}3️⃣  Listar chamados abertos{COR_RESET}")
        print(f"{COR_CIANO}4️⃣  Filtrar chamados por urgência{COR_RESET}")
        print(f"{COR_CIANO}5️⃣  Fechar chamado por ID{COR_RESET}")
        print(f"{COR_CIANO}6️⃣  Encerrar todos os chamados abertos (fim do dia){COR_RESET}")
        print(f"{COR_CIANO}7️⃣  Exibir chamados por setor{COR_RESET}")  
        print(f"{COR_CIANO}0️⃣  Sair do sistema{COR_RESET}\n")
        print("=" * 40)

        escolha = input(f"{COR_CIANO}\n👉 Escolha uma opção: {COR_RESET}")

        if escolha == "1":
            abrir_chamado()
        elif escolha == "2":
            listar_chamados()
        elif escolha == "3":
            listar_chamados_abertos()    
        elif escolha == "4":
            filtrar_urgencia()
        elif escolha == "5":
            fechar_chamado()
        elif escolha == "6":
            fim_do_dia()
        elif escolha == "7":
            exibir_matriz_setores()  
        elif escolha == "0":
            print(f"{COR_VERDE}👋 Saindo do sistema... Até logo!{COR_RESET}")
            break
        else:
            os.system("cls")
            print(f"{COR_VERMELHO}❌ Opção inválida. Tente novamente.{COR_RESET}")

def main():
    os.system("cls")
    print(f"{COR_CIANO}\nInicializando Sistema de chamados...{COR_RESET}")
    menu()

main()

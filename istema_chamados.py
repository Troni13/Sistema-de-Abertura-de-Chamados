import datetime
import os

chamados = []

# Gera um id para cada novo chamado
def gerar_id():
    return len(chamados) + 1

# Filtra se a urgencia digitada é uma permitida
def pedir_urgencia():
    opcoes_validas = ["baixa", "média", "alta"]
    while True:
        urgencia = input("\nUrgência (baixa/media/alta): ").strip().lower()
        if urgencia == "media":
            urgencia = "média"
        if urgencia in opcoes_validas:
            return urgencia
        else:
            print("\nUrgência inválida! Digite 'baixa', 'media' ou 'alta'.")

# Opção responsável por abertura de novos chamados
def abrir_chamado():
    print("\n--- ABRIR NOVO CHAMADO ---")
    setor = input("\nSetor responsável: ")
    descricao = input("\nDescrição do problema: ")
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
    os.system("cls")
    print("\n--- Chamado registrado com sucesso! ---")

def listar_chamados_abertos():
    if not chamados:
        os.system("cls")
        print("\n--- Nenhum chamado aberto registrado! ---")
        return False

    os.system("cls")
    print("\n--- LISTA DE CHAMADOS ---")
    for chamado in chamados:
        if chamado["status"] == "Aberto":
            print(f"🆔 ID: {chamado['id']} | 🏢 Setor: {chamado['setor']} | 🚨 Urgência: {chamado['urgencia'].capitalize()} | 🔖 Status: {chamado['status']}")
            print(f"Descrição: {chamado['descricao']}")
            print(f"Horário: {chamado['horario']}")
            print("-" * 30)

# Lista os chamados que foram abertos
def listar_chamados():
    if not chamados:
        os.system("cls")
        print("\n--- Nenhum chamado registrado ainda! ---")
        return

    os.system("cls")
    print("\n--- LISTA DE CHAMADOS ---")
    for chamado in chamados:
        print(f"🆔 ID: {chamado['id']} | 🏢 Setor: {chamado['setor']} | 🚨 Urgência: {chamado['urgencia'].capitalize()} | 🔖 Status: {chamado['status']}")
        print(f"Descrição: {chamado['descricao']}")
        print(f"Horário: {chamado['horario']}")
        print("-" * 30)

# Filtro de urgencias
def filtrar_urgencia():
    os.system("cls")
    opcoes_validas = ["baixa", "média", "alta"]
    urgencia = ""
    if not chamados:
        print("\n--- Nenhum chamado registrado ainda! ---")
        return
    else:
        while urgencia not in opcoes_validas:
            urgencia = input("Digite o nível de urgência para filtrar (baixa/média/alta): ").strip().lower()
            if urgencia == "media":
                urgencia = "média"

        print(f"\n--- FILTRANDO CHAMADOS COM URGÊNCIA: {urgencia.lower()} ---")
        for chamado in chamados:
            if chamado["urgencia"].lower() == urgencia.lower():
                print(f"🆔 ID: {chamado['id']} | 🏢 Setor: {chamado['setor']} | 🚨 Urgência: {chamado['urgencia'].capitalize()} | 🔖 Status: {chamado['status']}")
                print(f"Descrição: {chamado['descricao']}")
                print(f"Horário: {chamado['horario']}")
                print("-" * 30)

# Fecha os chamados já abertos
def fechar_chamado():
    os.system("cls")
    if not chamados:
        print("\n--- Nenhum chamado registrado ainda! ---")
        return
    else:
        listar_chamados()
        try:
            id_procura = int(input("Digite o ID do chamado a ser fechado: "))
        except ValueError:
            os.system("cls")
            print("ID inválido. Digite um número inteiro.")
            return
        for chamado in chamados:
            if chamado["id"] == id_procura and chamado["status"] == "Aberto":
                chamado["status"] = "Resolvido"
                os.system("cls")
                print("Chamado fechado com sucesso.")
                return
        os.system("cls")
        print("Chamado não encontrado ou já fechado.")

def contador_de_chamados():
    abertos = len([c for c in chamados if c["status"] == "Aberto"])
    resolvidos = len([c for c in chamados if c["status"] == "Resolvido"])
    total = len(chamados)
    print(f"\n📋 Total de chamados: {total} | 🟢 Abertos: {abertos} | ✅ Resolvidos: {resolvidos}\n")

# Menu para navegação
def menu():
    print("\n" + "=" * 40)
    print("📌  SISTEMA DE CHAMADOS - MENU PRINCIPAL")
    print("=" * 40)

    contador_de_chamados()

    print("1️⃣  Abrir chamado")
    print("2️⃣  Listar todos os chamados")
    print("3️⃣  Listar chamados abertos")
    print("4️⃣  Filtrar chamados por urgência")
    print("5️⃣  Fechar chamado por ID")
    print("0️⃣  Sair do sistema\n")
    print("=" * 40)

    escolha = input("\n👉 Escolha uma opção: ")

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
    elif escolha == "0":
        print("👋 Saindo do sistema... Até logo!")
        return
    else:
        os.system("cls")
        print("❌ Opção inválida. Tente novamente.")

    menu()

# Main
def main():
    os.system("cls")
    print("\nInicializando Sistema de chamados ()...")
    menu()

# Início
if __name__ == "__main__":
    main()

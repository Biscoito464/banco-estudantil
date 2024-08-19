import json

estudantes = []
disciplinas = []
professores = []
turmas = []
matriculas = []

def salvar_dados():
    dados = {
        "estudantes": estudantes,
        "disciplinas": disciplinas,
        "professores": professores,
        "turmas": turmas,
        "matriculas": matriculas
        }

    with open("dados.json", "w") as arquivo:
        json.dump(dados,arquivo)

def carregar_dados():
    try:
        with open("dados.json", "r") as arquivo:
            dados = json.load(arquivo)
            global estudantes, disciplinas, professores, turmas, matriculas
            estudantes = dados["estudantes"]
            disciplinas = dados["disciplinas"]
            professores = dados["professores"]
            turmas = dados["turmas"]
            matriculas = dados["matriculas"]

    except FileNotFoundError:
        pass
    
def exibir_menu_principal():
    print("\nMenu Principal")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matriculas")
    print("6. Sair")

def exibir_menu_operacoes():
    print("\nMenu de Operacoes")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu principal")

def main():
    carregar_dados()

    while True:
        exibir_menu_principal()
        opcao_principal = input("Digite a opcao desejada (1 a 6): ")

        if opcao_principal == "1":
            print("Voce escolheu: Estudantes")
            submenu_estudantes()

        if opcao_principal == "2":
            print("Voce escolheu: Disciplinas")
            submenu_disciplinas()

        if opcao_principal == "3":
            print("Voce escolheu: Professores")
            submenu_professores()

        if opcao_principal == "4":
            print("Voce escolheu: Turmas")
            submenu_turmas()

        if opcao_principal == "5":
            print("Voce escolheu: Matriculas")
            submenu_matriculas()

        elif opcao_principal == "6":
            print("Salvando os dados...")
            salvar_dados()
            print("Saindo do programa...")
            break

        else:
            print("Opcao invalida. Digite uma opcao valida (1 a 6).")

#estudantes
def criar_estudante(codigo, nome, idade, CPF ):
    novo_estudante =  {"codigo":codigo,"nome": nome,"idade": idade,"CPF": CPF}
    estudantes.append(novo_estudante)
    print("Estudante criado com sucesso!")
    
def listar_estudantes():
    if estudantes:
        for estudante in estudantes:
            print(estudante["codigo"], "-", estudante["nome"], "-", estudante["idade"],"-",estudante["CPF"])
    else:
        print("Nao ha estudantes cadastrados.")

def atualizar_estudante(codigo, novo_nome, nova_idade, novo_CPF):
    for estudante in estudantes:
        if estudante["codigo"] == codigo:
            estudante["nome"] = novo_nome
            estudante["idade"] = nova_idade
            estudante["CPF"] = novo_CPF
            print("Estudante atualizado com sucesso!")
            break
    else:
        print("Estudante nao encontrado.")

def excluir_estudante(codigo):
    global estudantes
    estudantes_restantes = [estudante for estudante in estudantes if estudante["codigo"] != codigo]
    if len(estudantes_restantes) < len(estudantes):
        estudantes = estudantes_restantes
        print("Estudante removido com sucesso!")
    else:
        print("Estudante não encontrado.")

#menudeestudantes
def submenu_estudantes():
    while True:
        exibir_menu_operacoes()
        opcao_estudantes = input("Digite a operacao desejada (1 a 5): ")

        if opcao_estudantes == "1":
            codigo = int(input("Digite o codigo do estudante: "))
            nome = input("Digite o nome do estudante: ")
            idade = int(input("Digite a idade do estudante: "))
            CPF = input("Digite o CPF do estudante: ")
            criar_estudante(codigo, nome, idade, CPF)

        elif opcao_estudantes == "2":
            print("Voce escolheu: listar estudantes")
            listar_estudantes()

        elif opcao_estudantes == "3":
            print("Você escolheu: Atualizar Estudante")
            codigo = int(input("Digite o codigo do estudante que deseja atualizar: "))
            novo_nome = input("Digite o novo nome do estudante: ")
            nova_idade = int(input("Digite a nova idade do estudante: "))
            novo_CPF = input("Digite o novo CPF do aluno: ")
            atualizar_estudante(codigo, novo_nome, nova_idade, novo_CPF)

        elif opcao_estudantes == "4":
            print("Você escolheu: Excluir Estudante")
            codigo = int(input("Digite o codigo do estudante que deseja excluir: "))
            excluir_estudante(codigo)

        elif opcao_estudantes == "5":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opcao invalida. Digite uma opcao valida (1 a 5).")

#diciplinas
def criar_disciplina(codigo, nome):
    nova_disciplina = {"codigo": codigo, "nome": nome}
    disciplinas.append(nova_disciplina)
    print("Disciplina criada com sucesso!")
    
def listar_disciplinas():
    if disciplinas:
        for disciplina in disciplinas:
            print(disciplina["codigo"], "-", disciplina["nome"])
    else:
        print("Nao ha disciplina cadastradas.")

def atualizar_disciplina(codigo, novo_nome):
    for disciplina in disciplinas:
        if disciplina["codigo"] == codigo:
            disciplina["nome"] = novo_nome
            print("Disciplina atualizada com sucesso!")
            break
    else:
        print("Disciplina nao encontrada.")

def excluir_disciplina(codigo):
    global disciplinas
    disciplinas_restantes = [disciplina for disciplina in disciplinas if disciplina["codigo"] != codigo]
    if len(disciplinas_restantes) < len(disciplinas):
        disciplinas = disciplinas_restantes

def submenu_disciplinas():
    while True:
        exibir_menu_operacoes()
        opcao_disciplinas = input("Digite a operacao desejada (1 a 5): ")

        if opcao_disciplinas == "1":
            codigo = int(input("Digite o codigo da disciplina: "))
            nome = input("Digite o nome da disciplina: ")
            criar_disciplina(codigo, nome)

        elif opcao_disciplinas == "2":
            print("Voce escolheu: listar disciplinas")
            listar_disciplinas()

        elif opcao_disciplinas == "3":
            print("Você escolheu: Atualizar disciplina")
            codigo = int(input("Digite o codigo da disciplina que deseja atualizar: "))
            novo_nome = input("Digite o novo nome da disciplina: ")
            atualizar_disciplina(codigo, novo_nome)

        elif opcao_disciplinas == "4":
            print("Você escolheu: Excluir disciplina")
            codigo = int(input("Digite o codigo da disciplina que deseja excluir: "))
            excluir_disciplina(codigo)

        elif opcao_disciplinas == "5":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opcao invalida. Digite uma opcao valida (1 a 5).")

#profesores
def criar_professor(codigo, nome, cpf):
    novo_professor = {"codigo": codigo, "nome": nome, "cpf": cpf}
    professores.append(novo_professor)
    print("Professor criado com sucesso!")

def listar_professores():
    if professores:
        print("Lista de Professores:")
        for professor in professores:
            print(f"Código: {professor['codigo']}, Nome: {professor['nome']}, CPF: {professor['cpf']}")
    else:
        print("Não há professores cadastrados.")

def atualizar_professor(codigo, novo_nome, novo_cpf):
    for professor in professores:
        if professor["codigo"] == codigo:
            professor["nome"] = novo_nome
            professor["cpf"] = novo_cpf
            print("Professor atualizado com sucesso!")
            break
    else:
        print("Professor não encontrado.")

def excluir_professor(codigo):
    global professores
    professores_restantes = [professor for professor in professores if professor["codigo"] != codigo]
    if len(professores_restantes) < len(professores):
        professores = professores_restantes
        print("Professor removido com sucesso!")
    else:
        print("Professor não encontrado.")


def submenu_professores():
    while True:
        exibir_menu_operacoes()
        opcao_professores = input("Digite a operacao desejada (1 a 5): ")

        if opcao_professores == "1":
            codigo = int(input("Digite o codigo do professor: "))
            nome = input("Digite o nome do professor: ")
            cpf = input("Digite o CPF do professor: ")
            criar_professor(codigo, nome, cpf)

        elif opcao_professores == "2":
            print("Voce escolheu: listar professor")
            listar_professores()

        elif opcao_professores == "3":
            print("Você escolheu: Atualizar professor")
            codigo = input("Digite o codigo do professor que deseja atualizar: ")
            novo_nome = input("Digite o novo nome da professor: ")
            novo_cpf = input("Digite o novo CPF do professor: ")
            atualizar_professor(codigo, novo_nome, novo_cpf)

        elif opcao_professores == "4":
            print("Você escolheu: Excluir professor")
            codigo = int(input("Digite o codigo da professor que deseja excluir: "))
            excluir_professor(codigo)

        elif opcao_professores == "5":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opcao invalida. Digite uma opcao valida (1 a 5).")

#turma
def criar_turma(codigo_turma, codigo_professor, codigo_disciplina):
    nova_turma = {"codigo_turma": codigo_turma, "codigo_professor": codigo_professor, "codigo_disciplina": codigo_disciplina}
    turmas.append(nova_turma)
    print("Turma criada com sucesso!")

def listar_turmas():
    if turmas:
        print("Lista de Turmas:")
        for turma in turmas:
            print(f"Código da Turma: {turma['codigo_turma']}, Código do Professor: {turma['codigo_professor']}, Código da Disciplina: {turma['codigo_disciplina']}")
    else:
        print("Não há turmas cadastradas.")

def atualizar_turma(codigo_turma, novo_codigo_professor, novo_codigo_disciplina):
    for turma in turmas:
        if turma["codigo_turma"] == codigo_turma:
            turma["codigo_professor"] = novo_codigo_professor
            turma["codigo_disciplina"] = novo_codigo_disciplina
            print("Turma atualizada com sucesso!")
            break
    else:
        print("Turma não encontrada.")

def excluir_turma(codigo_turma):
    global turmas
    turmas_restantes = [turma for turma in turmas if turma["codigo_turma"] != codigo_turma]
    if len(turmas_restantes) < len(turmas):
        turmas = turmas_restantes
        print("Turma removida com sucesso!")
    else:
        print("Turma não encontrada.")

def submenu_turmas():
    while True:
        exibir_menu_operacoes()
        opcao_turmas = input("Digite a operacao desejada (1 a 5): ")

        if opcao_turmas == "1":
            codigo_turma = int(input("Digite o codigo da turma: "))
            codigo_professor = input("Digite o codigo do professor: ")
            codigo_disciplina = input("Digite o codigo da disciplina: ")
            criar_turma(codigo_turma, codigo_professor, codigo_disciplina)

        elif opcao_turmas == "2":
            print("Voce escolheu: listar turmas")
            listar_turmas()

        elif opcao_turmas == "3":
            print("Você escolheu: Atualizar Turma")
            codigo_turma = int(input("Digite o codigo do Turma que deseja atualizar: "))
            novo_codigo_professor = input("Digite o novo codigo da professor: ")
            novo_codigo_disciplina = input("Digite o novo codigo da disciplina: ")
            atualizar_turma(codigo_turma, novo_codigo_professor, novo_codigo_disciplina)

        elif opcao_turmas == "4":
            print("Você escolheu: Excluir turma")
            codigo_turma = int(input("Digite o codigo da turma que deseja excluir: "))
            excluir_turma(codigo_turma)

        elif opcao_turmas == "5":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opcao invalida. Digite uma opcao valida (1 a 5).")

#matriculas
def criar_matricula(codigo_matricula, codigo_estudante, codigo_turma):
    nova_matricula = {"codigo_matricula": codigo_matricula, "codigo_estudante": codigo_estudante, "codigo_turma": codigo_turma}
    matriculas.append(nova_matricula)
    print("Matrícula criada com sucesso!")

def listar_matriculas():
    if matriculas:
        print("Lista de Matrículas:")
        for matricula in matriculas:
            print(f"Código da Matrícula: {matricula['codigo_matricula']}, Código do Estudante: {matricula['codigo_estudante']}, Código da Turma: {matricula['codigo_turma']}")
    else:
        print("Não há matrículas cadastradas.")

def atualizar_matricula(codigo_matricula, novo_codigo_estudante, novo_codigo_turma):
    for matricula in matriculas:
        if matricula["codigo_matricula"] == codigo_matricula:
            matricula["codigo_estudante"] = novo_codigo_estudante
            matricula["codigo_turma"] = novo_codigo_turma
            print("Matrícula atualizada com sucesso!")
            break
    else:
        print("Matrícula não encontrada.")

def excluir_matricula(codigo_matricula):
    global matriculas
    matriculas_restantes = [matricula for matricula in matriculas if matricula["codigo_matricula"] != codigo_matricula]
    if len(matriculas_restantes) < len(matriculas):
        matriculas = matriculas_restantes
        print("Matrícula removida com sucesso!")
    else:
        print("Matrícula não encontrada.")

def submenu_matriculas():
    while True:
        exibir_menu_operacoes()
        opcao_matriculas = input("Digite a operação desejada (1 a 5): ")

        if opcao_matriculas == "1":
            codigo_matricula = int(input("Digite o código da matrícula: "))
            codigo_estudante = input("Digite o código do estudante: ")
            codigo_turma = input("Digite o código da turma: ")
            criar_matricula(codigo_matricula, codigo_estudante, codigo_turma)

        elif opcao_matriculas == "2":
            print("Você escolheu: listar matrículas")
            listar_matriculas()

        elif opcao_matriculas == "3":
            print("Você escolheu: Atualizar Matrícula")
            codigo_matricula = int(input("Digite o código da matrícula que deseja atualizar: "))
            novo_codigo_estudante = input("Digite o novo código do estudante: ")
            novo_codigo_turma = input("Digite o novo código da turma: ")
            atualizar_matricula(codigo_matricula, novo_codigo_estudante, novo_codigo_turma)

        elif opcao_matriculas == "4":
            print("Você escolheu: Excluir Matrícula")
            codigo_matricula = int(input("Digite o código da matrícula que deseja excluir: "))
            excluir_matricula(codigo_matricula)

        elif opcao_matriculas == "5":
            print("Voltando ao menu principal...")
            break

        else:
            print("Opção inválida. Digite uma opção válida (1 a 5).")

if __name__ == "__main__":
    main()
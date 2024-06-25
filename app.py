from modelos.alunos import Aluno
from modelos.jurado import Jurado
def cadastrar_aluno():
    nome = input("Nome do aluno: ")
    categoria = input("Categoria Miss (1) | Mister (2): ")
    return Aluno(nome, categoria)

def cadastrar_jurado():
    nome = input("Nome do jurado: ")
    return Jurado(nome)

def registrar_voto(aluno, jurado):
    for categoria in aluno.notas.keys():
        if aluno.jurados[categoria] is None:
            nota = float(input(f"Nota para {categoria} (0-10): "))
            aluno.notas[categoria] = nota
            aluno.jurados[categoria] = jurado.nome
        else:
            print(f"{jurado.nome} já votou para a categoria {categoria}.")

def gerar_relatorio(alunos):
    for aluno in alunos:
        print(f"\nAluno: {aluno.nome} ({aluno.categoria})")
        for categoria, nota in aluno.notas.items():
            jurado = aluno.jurados[categoria]
            print(f"{categoria}: {nota} (Jurado: {jurado})")

def main():
    alunos = []
    jurados = []

    while True:
        opcao = input("1. Cadastrar Aluno\n2. Cadastrar Jurado\n3. Registrar Voto\n4. Gerar Relatório\n5. Sair\nEscolha uma opção: ")
        
        if opcao == "1":
            alunos.append(cadastrar_aluno())
        elif opcao == "2":
            jurados.append(cadastrar_jurado())
        elif opcao == "3":
            aluno_nome = input("Nome do aluno: ")
            jurado_nome = input("Nome do jurado: ")

            aluno = next((a for a in alunos if a.nome == aluno_nome), None)
            jurado = next((j for j in jurados if j.nome == jurado_nome), None)

            if aluno and jurado:
                registrar_voto(aluno, jurado)
            else:
                print("Aluno ou Jurado não encontrado.")
        elif opcao == "4":
            gerar_relatorio(alunos)
        elif opcao == "5":
            print("Exibindo o relatório final...")
            gerar_relatorio(alunos)
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
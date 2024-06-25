class Jurado:
    def __init__(self,nome):
        self.nome = nome

    def __str__(self) : 
        return f'{self.nome}'
    
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

        
        
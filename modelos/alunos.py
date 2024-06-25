class Aluno:

    alunos = []

    def __init__(self,nome):
        self.nome = nome
        self._jurado = None
        self.alunos.append(self)
        self._notas = None


    def __str__(self):
        return f'------------Nome do aluno: {self.nome}----------------\nJurado: {self._jurado}  Notas: {self._notas}'

    @classmethod
    def listar_alunos(cls):
        print(f"{'Nome do aluno'.ljust(20)} |{'Nome do jurado'.ljust(20)} | {'Nota de elegancia:'.ljust(20)} | {'Nota de desenvoltura:'.ljust(20)} | {'Nota de simpatia:'.ljust(20)} | {'Nota de item reciclavel:'}")
        for nota in cls.alunos:
            print(f'{str(nota.nome).ljust(20)} |{str(nota._jurado).ljust(20)} |{str(nota._notas).ljust(20)} ')

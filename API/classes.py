class TelaInicial:
    def exibirTelaLogin(self):
        # Código para exibir a tela de login
        pass

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

class Responsavel(Usuario):
    def designarTarefa(self, aluno, tarefa, prazo, dificuldade):
        # Código para designar uma tarefa ao aluno
        pass

    def adicionarRecompensa(self, descricao, pontos):
        # Código para adicionar uma recompensa ao sistema
        pass

class Aluno(Usuario):
    def acessarAtividades(self):
        # Código para acessar as atividades do aluno
        pass

class Atividade:
    def __init__(self, descricao, prazo, dificuldade, pontosRecompensa, status):
        self.descricao = descricao
        self.prazo = prazo
        self.dificuldade = dificuldade
        self.pontosRecompensa = pontosRecompensa
        self.status = status

class BarraProgresso:
    def __init__(self, tempoRestante, tempoTotal):
        self.tempoRestante = tempoRestante
        self.tempoTotal = tempoTotal

    def calcularProgresso(self):
        # Cálculo do progresso da barra
        pass

class SistemaPontos:
    def __init__(self, pontosDisponiveis):
        self.pontosDisponiveis = pontosDisponiveis

    def acumularPontos(self, pontos):
        # Código para acumular pontos no sistema
        pass

class Recompensa:
    def __init__(self, descricao, pontosNecessarios):
        self.descricao = descricao
        self.pontosNecessarios = pontosNecessarios

class Sistema:
    def __init__(self):
        self.usuarios = []
        self.atividadesConcluidas = []

    def login(self, usuario, senha):
        # Código para realizar o login
        pass

    def exibirAtividades(self, aluno):
        # Código para exibir as atividades do aluno
        pass

    def exibirRecompensas(self, aluno):
        # Código para exibir as recompensas disponíveis para o aluno
        pass

    def resgatarRecompensa(self, aluno, recompensa):
        # Código para resgatar uma recompensa pelo aluno
        pass

    def notificarRecompensaResgatada(self, responsavel, aluno, recompensa):
        # Código para notificar o responsável sobre a recompensa resgatada pelo aluno
        pass

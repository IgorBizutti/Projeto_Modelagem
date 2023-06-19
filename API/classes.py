class TelaInicial:
    def exibirTelaLogin(self):
        print("Tela de Login")

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

class Responsavel(Usuario):
    def designarTarefa(self, aluno, tarefa, prazo, dificuldade):
        aluno.atividades.append(tarefa)
        aluno.prazos.append(prazo)
        aluno.dificuldades.append(dificuldade)
        print(f"Tarefa '{tarefa}' designada para o aluno '{aluno.nome}'")

    def adicionarRecompensa(self, aluno, descricao, pontos):
        recompensa = Recompensa(descricao, pontos)
        aluno.recompensas.append(recompensa)
        print(f"Recompensa '{descricao}' ({pontos} pontos) adicionada para o aluno")

        print(f"Recompensa '{descricao}' adicionada ao aluno '{aluno.nome}' com sucesso!")

class Aluno(Usuario):
    def __init__(self, nome, senha):
        super().__init__(nome, senha)
        self.atividades = []
        self.prazos = []
        self.dificuldades = []
        self.recompensas = []

    def acessarAtividades(self):
        print("Atividades do Aluno:")
        for i in range(len(self.atividades)):
            print(f"Atividade: {self.atividades[i]}, Prazo: {self.prazos[i]}, Dificuldade: {self.dificuldades[i]}")

class Atividade:
    def __init__(self, descricao, prazo, dificuldade, pontosRecompensa, status):
        self.descricao = descricao
        self.prazo = prazo
        self.dificuldade = dificuldade
        self.pontosRecompensa = pontosRecompensa
        self.status = status

    def __str__(self):
        return f"Descrição: {self.descricao}\n" \
               f"Prazo: {self.prazo}\n" \
               f"Dificuldade: {self.dificuldade}\n" \
               f"Pontos de Recompensa: {self.pontosRecompensa}\n" \
               f"Status: {'Concluída' if self.status else 'Pendente'}"

class BarraProgresso:
    def __init__(self, tempoRestante, tempoTotal):
        self.tempoRestante = tempoRestante
        self.tempoTotal = tempoTotal

    def calcularProgresso(self):
        progresso = (self.tempoTotal - self.tempoRestante) / self.tempoTotal * 100
        print(f"Progresso: {progresso}%")

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
        if usuario == "admin" and senha == "admin123":
            print("Login realizado com sucesso")
        else:
            print("Login inválido")

    def exibirAtividades(self, aluno):
        print(f"Atividades do aluno '{aluno.nome}':")
        for atividade in aluno.atividades:
            print(f"- Descrição: {atividade.descricao}")
            print(f"  Prazo: {atividade.prazo}")
            print(f"  Dificuldade: {atividade.dificuldade}")

    def exibirRecompensas(self, aluno):
        print(f"Recompensas disponíveis para o aluno '{aluno.nome}':")
        for recompensa in aluno.recompensas:
            print(f"- Descrição: {recompensa.descricao}")
            print(f" Pontos necessários: {recompensa.pontosNecessarios}")

    def resgatarRecompensa(self, aluno, recompensa):
        if recompensa in aluno.recompensas:
            if aluno.pontos >= recompensa.pontosNecessarios:
                aluno.pontos -= recompensa.pontosNecessarios
                aluno.recompensas.remove(recompensa)
                print(f"Aluno '{aluno.nome}' resgatou a recompensa '{recompensa.descricao}'")
            else:
                print("Pontos insuficientes para resgatar a recompensa")
        else:
            print("Recompensa não encontrada")

    def notificarRecompensaResgatada(self, responsavel, aluno, recompensa):
        print(f"Responsável '{responsavel.nome}' foi notificado sobre a recompensa '{recompensa.descricao}' resgatada pelo aluno '{aluno.nome}'")

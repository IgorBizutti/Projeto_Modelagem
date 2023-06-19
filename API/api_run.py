from classes import TelaInicial, Responsavel, Aluno, Atividade, Recompensa, Sistema

# Criando os objetos
tela_inicial = TelaInicial()
responsavel = Responsavel("João", "123456")
aluno = Aluno("Maria", "654321")
atividade1 = Atividade("Fazer exercícios", "30/05/2023", "Fácil", 10, False)
atividade2 = Atividade("Ler um livro", "15/06/2023", "Média", 20, False)
recompensa1 = Recompensa("Assistir a um filme", 15)
recompensa2 = Recompensa("Passear no parque", 30)
sistema = Sistema()

# Exemplo de uso das funções
tela_inicial.exibirTelaLogin()

responsavel.designarTarefa(aluno, atividade1, "30/05/2023", "Fácil")
responsavel.designarTarefa(aluno, atividade2, "15/06/2023", "Média")
responsavel.adicionarRecompensa(aluno, recompensa1.descricao, recompensa1.pontosNecessarios)
responsavel.adicionarRecompensa(aluno, recompensa2.descricao, recompensa2.pontosNecessarios)

aluno.acessarAtividades()

sistema.exibirAtividades(aluno)
sistema.exibirRecompensas(aluno)

sistema.resgatarRecompensa(aluno, recompensa1)
sistema.resgatarRecompensa(aluno, recompensa2)

sistema.notificarRecompensaResgatada(responsavel, aluno, recompensa1)

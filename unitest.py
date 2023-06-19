from API.classes import Aluno, Atividade, Recompensa, Responsavel
import unittest

class TestClasses(unittest.TestCase):
    def setUp(self):
        self.responsavel = Responsavel("João", "senha123")
        self.aluno = Aluno("João", "123")
        self.atividade = Atividade("Tarefa 1", "2023-06-01", "Fácil", 10, False)
        self.recompensa = Recompensa("Recompensa 1", 20)
    
    def test_aluno_inicializado_corretamente(self):
        self.assertEqual(self.aluno.nome, "João")
        self.assertEqual(self.aluno.senha, "123")
        self.assertEqual(self.aluno.atividades, [])
    
    def test_atividade_inicializada_corretamente(self):
        self.assertEqual(self.atividade.descricao, "Tarefa 1")
        self.assertEqual(self.atividade.prazo, "2023-06-01")
        self.assertEqual(self.atividade.dificuldade, "Fácil")
        self.assertEqual(self.atividade.pontosRecompensa, 10)
        self.assertEqual(self.atividade.status, False)
    
    def test_recompensa_inicializada_corretamente(self):
        self.assertEqual(self.recompensa.descricao, "Recompensa 1")
        self.assertEqual(self.recompensa.pontosNecessarios, 20)
    
    def test_designar_tarefa(self):
        # Criação dos objetos
        aluno = Aluno("João", "senha_aluno")
        responsavel = Responsavel("Maria", "senha_responsavel")
        tarefa = Atividade("Fazer exercícios", "2023-05-30", "Média", 10, False)

        # Designar tarefa ao aluno
        responsavel.designarTarefa(aluno, tarefa, "2023-05-30", "Média")

        # Verificar se a tarefa foi atribuída corretamente
        self.assertIn(tarefa, aluno.atividades)
        self.assertEqual(aluno.atividades[0].descricao, "Fazer exercícios")
        self.assertEqual(aluno.atividades[0].prazo, "2023-05-30")
        self.assertEqual(aluno.atividades[0].dificuldade, "Média")
        self.assertEqual(aluno.atividades[0].pontosRecompensa, 10)
        self.assertFalse(aluno.atividades[0].status)
    
    def test_acessar_atividades(self):
        self.responsavel.designarTarefa(self.aluno, self.atividade, "2023-06-15", "Médio")
        atividades = self.aluno.acessarAtividades()
        self.assertEqual(self.atividade, self.aluno.atividades[0])
    
    def test_adicionar_recompensa(self):
        # Criação dos objetos
        aluno = Aluno("João", "senha_aluno")
        responsavel = Responsavel("Maria", "senha_responsavel")
        recompensa = Recompensa("Brinquedo", 20)

        # Adicionar recompensa ao aluno
        responsavel.adicionarRecompensa(aluno, recompensa.descricao, recompensa.pontosNecessarios)

        # Verificar se a recompensa foi adicionada corretamente
        self.assertIn(recompensa.descricao, [rec.descricao for rec in aluno.recompensas])
        self.assertEqual(aluno.recompensas[0].descricao, "Brinquedo")
        self.assertEqual(aluno.recompensas[0].pontosNecessarios, 20)

if __name__ == '__main__':
    unittest.main()

# Execute o comando abaixo no terminal para rodar teste:
# python -m unittest unitest.py 

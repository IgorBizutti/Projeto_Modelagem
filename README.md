

Escopo da Api Rest

1 - Tela Inicial 

- De inicio haverá uma tela de login com usuário padronizado, exemplo: professores serão prof.(nome e sobrenome), crianças serão aluno.(nome e sobrenome), e os pais serão Pais.(nome e sobrenome)



2 - Professor

- O Professor possuem acesso para designar tarefa a criança, o prazo da tarefa, o grau de dificuldade e referente a isso a quantidade de pontos que aquela tarefa vale, ex: tarefas dificeis valem 50, médias 25 e fáceis valem 10. 
- O professor também possui acesso para corrigir a atividade e adicionar novas recompensas. 
- O Professor pode abrir chat com os alunos e também com os pais.



3 - Pai
- Mesmos acessos que os alunos.

4 - Aluno
- A criança poderá apenas acessar a aba de atividades e de recompensas para visualizá-las. 
- E Acesso à aba de atividades
- E poder abrir chat com professor




ABA DE ATIVIDADES 

- a aba de atividades, onde será dividida por matérias(portugues, matematica, ciencias, historia), cada matéria terá suas atividades, com descrição, prazo, grau de dificuldade e pontos de recompensa referente ao grau de dificuldade.
- haverá um marcador em formato de barra de progresso determinando o tempo restante para o prazo da tarefa. 
- Na aba de atividades também haverá um setor para atividades ja concluídas.



ABA DE PONTOS

- os pontos ficarão disponíveis no cabeçalho para serem visualizados, e conforme as atividades forem sendo concluidas, os pontos irao acumulando ate alguma recompensa for resgatada.
- Todas as recompensas serão mostradas, porém estarão disponiveis para resgate apenas aquelas nas quais a pontuação necessária seja menor da qual a criança possuí. 
- Recompensas resgatadas serão notificadas aos professores para que possam ser entregues. 


  Driagrama de Classes
  
Classe: TelaInicial
Métodos:
- exibirTelaLogin()


Classe: Usuario

Atributos:
- nome: string
- senha: string

Métodos:
- abrirChat(usuario: Usuario)
 

Classe: Professor (herda de Usuario)

Métodos:
- designarTarefa(aluno: Aluno, tarefa: Atividade, prazo: string, dificuldade: string)
- corrigirAtividade(aluno: Aluno, tarefa: Atividade, nota: int)
- adicionarRecompensa(descricao: string, pontos: int)


Classe: Pai (herda de Usuario)

Classe: Aluno (herda de Usuario)

Métodos:
- acessarAtividades()
- abrirChatProfessor(professor: Professor)

Classe: Atividade

Atributos:
- materia: string
- descricao: string
- prazo: string
- dificuldade: string
- pontosRecompensa: int
- concluida: bool

Classe: Materia

Atributos:
- nome: string
- atividades: list[Atividade]

Classe: BarraProgresso

Atributos:
- tempoRestante: int
- tempoTotal: int

Métodos:
- calcularProgresso()

Classe: SistemaPontos

Atributos:
- pontosDisponiveis: int

Métodos:
- acumularPontos(pontos: int)

Classe: Recompensa

Atributos:
- descricao: string
- pontosNecessarios: int

Classe: Sistema

Atributos:
- usuarios: list[Usuario]
- atividadesConcluidas: list[Atividade]

Métodos:
- login(usuario: string, senha: string)
- exibirAtividades(aluno: Aluno)
- exibirRecompensas(aluno: Aluno)
- resgatarRecompensa(aluno: Aluno, recompensa: Recompensa)
- notificarRecompensaResgatada(professor: Professor, aluno: Aluno, recompensa: Recompensa)



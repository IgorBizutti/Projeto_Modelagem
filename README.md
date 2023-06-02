

Escopo da Api Rest

1 - Tela Inicial 

- De inicio haverá uma tela de login com usuário padronizado

2 - Responsável

- O Responsável possuí acesso para designar tarefa a criança, o prazo da tarefa, o grau de dificuldade e referente a isso a quantidade de pontos que aquela tarefa vale, ex: tarefas dificeis valem 50, médias 25 e fáceis valem 10. 


3 - Aluno
- A criança poderá apenas acessar a aba de atividades e de recompensas para visualizá-las. 

ABA DE ATIVIDADES 

- a aba de atividades, com descrição, prazo, grau de dificuldade e pontos de recompensa referente ao grau de dificuldade.
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
 
Classe: Responsável (herda de Usuario)

Métodos:
- designarTarefa(aluno: Aluno, tarefa: Atividade, prazo: string, dificuldade: string)
- adicionarRecompensa(descricao: string, pontos: int)

Classe: Aluno (herda de Usuario)

Métodos:
- acessarAtividades()

Classe: Atividade

Atributos:
- descricao: string
- prazo: string
- dificuldade: string
- pontosRecompensa: int
- status: bool

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
- notificarRecompensaResgatada(responsável: Responsável, aluno: Aluno, recompensa: Recompensa)



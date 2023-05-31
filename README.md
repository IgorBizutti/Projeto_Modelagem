## Projeto_Modelagem

#Bem-Vindo a equipe desenvolvedor!
<p> Neste projeto você deverá instalar a linguagem PYTHON na versão 3.11: https://www.python.org/downloads/ </p>
<p>Utilizamos o Visual Studio Code: https://code.visualstudio.com/download</p>

#Para clonar o repositório em sua máquina, siga as seguintes instruções
1. Abra o CMD do Windows
2. Nesse caso iremos clonar o repositório dentro da pasta Documentos do Windows, então digite: cd Documents 
3. Insira o seguinte comando: git clone https://github.com/IgorBizutti/Projeto_Modelagem.git
<p>Com isso você terá feito o download do repositório em sua máquina</p>

#Para fazer envios ao GIT
1. Abra o Terminal dentro do Visual Studio Code > New Terminal
2. Insira os seguintes comandos: git add .
3. git commit -m "Seu Commit"
4. git push
<p>Com isso você conseguirá enviar suas contribuições</p>

#Para manter seu repositório atualizado
1. Abra o Terminal dentro do Visual Studio Code > New Terminal
2. Insira o comando: git pull


Escopo da Api Rest

1 - Tela Inicial 

- De inicio haverá uma tela de login com usuário padronizado, exemplo: professores serão prof.(nome e sobrenome), crianças serão aluno.(nome e sobrenome)



2 - Professor

- O Professor possuem acesso para designar tarefa a criança, o prazo da tarefa, o grau de dificuldade e referente a isso a quantidade de pontos que aquela tarefa vale, ex: tarefas dificeis valem 50, médias 25 e fáceis valem 10. 
- O professor também possui acesso para corrigir a atividade e adicionar novas recompensas. 



3 - Pai

mesmos acessos que os alunos.

4 - Criança(Aluno)

- A criança poderá apenas acessar a aba de atividades e de recompensas para visualizá-las. 
- E Acesso à aba de atividades




ABA DE ATIVIDADES 

- a aba de atividades, onde será dividida por matérias(portugues, matematica, ciencias, historia), cada matéria terá suas atividades, com descrição, prazo, grau de dificuldade e pontos de recompensa referente ao grau de dificuldade.

- haverá um marcador em formato de barra de progresso determinando o tempo restante para o prazo da tarefa. 

- Na aba de atividades também haverá um setor para atividades ja concluídas.



ABA DE PONTOS

- os pontos ficarão disponíveis no cabeçalho para serem visualizados, e conforme as atividades forem sendo concluidas, os pontos irao acumulando ate alguma recompensa for resgatada.

- Todas as recompensas serão mostradas, porém estarão disponiveis para resgate apenas aquelas nas quais a pontuação necessária seja menor da qual a criança possuí. 

- Recompensas resgatadas serão notificadas aos professores para que possam ser entregues. 


            +--------------+
            |   Usuário    |
            +--------------+
            | - nome       |
            | - senha      |
            | - tipo       |
            +--------------+
                  /_\
                   |
            +--------------+
            |   Professor  |
            +--------------+
            | - designarTarefa()  |
            | - definirPrazo()    |
            | - definirDificuldade() |
            | - definirPontos() |
            | - corrigirAtividade() |
            | - adicionarRecompensa() |
            +--------------+
                  /_\
                   |
            +--------------+
            |    Aluno     |
            +--------------+
            | - monitorarTarefasPendentes() |
            | - resgatarRecompensas() |
            | - marcarTarefaConcluida() |
            | - contatarProfessor() |
            +--------------+
                  /_\
                   |
            +------------------+
            |     Atividade    |
            +------------------+
            | - descricao       |
            | - prazo           |
            | - dificuldade     |
            | - pontosRecompensa|
            +------------------+
            /       |        \
           /        |         \
          /         |          \
+---------------+ +----------------+ +---------------+ +----------------+
|  Português    | |   Matemática   | |   Ciências    | |    História    |
+---------------+ +----------------+ +---------------+ +----------------+
| - atividades  | | - atividades   | | - atividades  | | - atividades   |
+---------------+ +----------------+ +---------------+ +----------------+
| - atividades  | | - atividades   | | - atividades  | | - atividades   |
|  concluídas   | |  concluídas    | |  concluídas   | |  concluídas    |
+---------------+ +----------------+ +---------------+ +----------------+
            /_\
             |
    +------------------+
    |    Recompensa    |
    +------------------+
    | - descricao       |
    | - pontosNecessarios|
    +------------------+
    /       |        \
   /        |         \
  /         |          \
+---------------+ +----------------+ +---------------+
| Recompensa 1  | | Recompensa 2   | | Recompensa 3 |
+---------------+ +----------------+ +---------------+



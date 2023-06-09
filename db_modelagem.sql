/* Rodar o SCRIPT abaixo em uM DATABASE conectado em um banco de dados ORACLE

/* Usuarios */
CREATE TABLE usuarios (
    id_usuario INT GENERATED BY DEFAULT ON NULL AS IDENTITY,
    email VARCHAR(40)UNIQUE NOT NULL,
    senha VARCHAR2(20) NOT NULL,
    ocupacao CHECK (UPPER(ocupacao) IN ('PROFESSOR', 'ALUNO')) NOT NULL,
    nome VARCHAR(12) NOT NULL,
    sobrenome VARCHAR(20) NOT NULL,
    cpf_rg INT CONSTRAINT UNIQUE PRIMARY KEY NOT NULL,
    pontos INT,
    qtd_atividades_concluidas INT
);

/* Recompensas */

CREATE TABLE recompensas (
      id_recompensa INT GENERATED BY DEFAULT ON NULL AS IDENTITY CONSTRAINT UNIQUE PRIMARY KEY,
      valor_pontos VARCHAR2(40),
      descricao_recompensa VARCHAR(20) NOT NULL
);

/* Atividades */
CREATE TABLE atividades (
      id_atividades INT GENERATED BY DEFAULT ON NULL AS IDENTITY CONSTRAINT UNIQUE PRIMARY KEY,
      nome_atividade VARCHAR2(25) NOT NULL,
      descricao_atividade VARCHAR(50) NOT NULL,
      prazo DATE NOT NULL,
      dificuldade CHECK (UPPER(dificuldade) IN ('FACIL', 'MODERADO', 'DIFICIL')) NOT NULL,
      status CHECK (UPPER(status) IN ('NOVO', 'CONCLUIDA')) NOT NULL,
      valor_pontos INT
);

CREATE TABLE IF NOT EXISTS "responsavel" (
        "id"    INTEGER NOT NULL,
        "nome"  VARCHAR(80) NOT NULL,
        "cpf"   VARCHAR(11) NOT NULL,
        "sexo"  VARCHAR(10) NOT NULL,
        "email" VARCHAR(255) NOT NULL,
        "tipo_responsavel"      VARCHAR(255) NOT NULL,
        "profissao"     VARCHAR(100) NOT NULL,
        "endereco"      VARCHAR(250),
        "contatos"      VARCHAR,
        "status"        INTEGER NOT NULL DEFAULT 0,
        "criadoem"      DATE NOT NULL DEFAULT (date('now')),
        "atualizadoem"  DATE,
        "photo" VARCHAR,
        PRIMARY KEY("id")
);
CREATE UNIQUE INDEX "responsavel_cpf" ON "responsavel" (
        "cpf"
);

CREATE TABLE IF NOT EXISTS "aluno" (
        "id"    INTEGER NOT NULL,
        "nome"  varchar(80) NOT NULL,
        "cpf"   varchar(11),
        "rg"    varchar(15),
        "orgao_exp_rg"  VARCHAR(15),
        "uf_exp_rg"     VARCHAR(2),
        "nascimento"    date,
        "sexo"  varchar(10) NOT NULL,
        "pai"   INTEGER,
        "mae"   INTEGER,
        "endereco"      varchar(255),
        "photo" blob,
        "criadoem"      DATE DEFAULT 'date(''now'')',
        "atualizadoem"  DATE,
        "bairro"        varchar(80),
        "cidade"        varchar(80),
        "uf"    varchar(2),
        PRIMARY KEY("id")
);
CREATE UNIQUE INDEX "aluno_cpf" ON "aluno" (
        "cpf"
);

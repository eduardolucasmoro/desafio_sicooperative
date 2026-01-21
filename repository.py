from db import get_connection


def criar_tabelas():
    sql = """
        -- =========================
        -- TABELA: associado
        -- =========================
        CREATE TABLE associado (
            id INT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            sobrenome VARCHAR(100) NOT NULL,
            data_nascimento DATE,
            email VARCHAR(100)
        );

        -- =========================
        -- TABELA: conta
        -- =========================
        CREATE TABLE conta (
            id INT PRIMARY KEY,
            tipo INT NOT NULL,
            data_criacao TIMESTAMP NOT NULL,
            id_associado INT NOT NULL,
            CONSTRAINT fk_conta_associado
                FOREIGN KEY (id_associado)
                REFERENCES associado (id)
        );

        -- =========================
        -- TABELA: cartao
        -- =========================
        CREATE TABLE cartao (
            id INT PRIMARY KEY,
            num_cartao INT NOT NULL,
            nom_impresso VARCHAR(100) NOT NULL,
            data_criacao_cartao TIMESTAMP NOT NULL,
            id_conta INT NOT NULL,
            id_associado INT NOT NULL,
            CONSTRAINT fk_cartao_conta
                FOREIGN KEY (id_conta)
                REFERENCES conta (id),
            CONSTRAINT fk_cartao_associado
                FOREIGN KEY (id_associado)
                REFERENCES associado (id)
        );

        -- =========================
        -- TABELA: movimento
        -- =========================
        CREATE TABLE movimento (
            id INT PRIMARY KEY,
            vlr_transacao DECIMAL(10,2) NOT NULL,
            des_transacao VARCHAR(200),
            data_movimento TIMESTAMP NOT NULL,
            id_cartao INT NOT NULL,
            CONSTRAINT fk_movimento_cartao
                FOREIGN KEY (id_cartao)
                REFERENCES cartao (id)
        );
    """

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(sql)
        conn.commit()
    finally:
        cur.close()
        conn.close()


def inserir_dados():
    sql = """
        -- =========================
        -- TABELA: associado
        -- =========================
        INSERT INTO associado (id, nome, sobrenome, data_nascimento, email) VALUES
        (1,'João','Silva','1985-03-10','joao.silva@email.com'),
        (2,'Maria','Santos','1990-07-22','maria.santos@email.com'),
        (3,'Carlos','Oliveira','1982-11-05','carlos.oliveira@email.com'),
        (4,'Ana','Pereira','1995-01-18','ana.pereira@email.com'),
        (5,'Pedro','Costa','1988-09-30','pedro.costa@email.com'),
        (6,'Juliana','Rodrigues','1992-06-14','juliana.rodrigues@email.com'),
        (7,'Marcos','Almeida','1980-04-02','marcos.almeida@email.com'),
        (8,'Fernanda','Lima','1987-12-19','fernanda.lima@email.com'),
        (9,'Lucas','Gomes','1993-08-25','lucas.gomes@email.com'),
        (10,'Patricia','Nogueira','1984-10-11','patricia.nogueira@email.com'),
        (11,'Rafael','Martins','1991-05-09','rafael.martins@email.com'),
        (12,'Camila','Araujo','1996-02-27','camila.araujo@email.com'),
        (13,'Bruno','Ribeiro','1989-07-07','bruno.ribeiro@email.com'),
        (14,'Renata','Barbosa','1983-03-21','renata.barbosa@email.com'),
        (15,'Diego','Teixeira','1994-09-13','diego.teixeira@email.com'),
        (16,'Aline','Freitas','1990-12-01','aline.freitas@email.com'),
        (17,'Eduardo','Pacheco','1986-06-17','eduardo.pacheco@email.com'),
        (18,'Larissa','Farias','1997-04-29','larissa.farias@email.com'),
        (19,'Thiago','Moura','1981-11-23','thiago.moura@email.com'),
        (20,'Beatriz','Cunha','1998-08-06','beatriz.cunha@email.com');

        -- =========================
        -- TABELA: conta
        -- =========================
        INSERT INTO conta (id, tipo, data_criacao, id_associado) VALUES
        (1,1,'2023-01-10 10:00:00',1),
        (2,2,'2023-01-12 11:30:00',2),
        (3,1,'2023-01-15 09:45:00',3),
        (4,3,'2023-01-18 14:20:00',4),
        (5,2,'2023-01-20 16:10:00',5),
        (6,1,'2023-01-22 08:50:00',6),
        (7,3,'2023-01-25 13:00:00',7),
        (8,2,'2023-01-27 17:40:00',8),
        (9,1,'2023-01-30 12:15:00',9),
        (10,2,'2023-02-01 10:05:00',10),
        (11,1,'2023-02-03 09:00:00',11),
        (12,3,'2023-02-05 15:30:00',12),
        (13,2,'2023-02-07 11:10:00',13),
        (14,1,'2023-02-09 14:55:00',14),
        (15,3,'2023-02-11 16:45:00',15),
        (16,2,'2023-02-13 08:35:00',16),
        (17,1,'2023-02-15 10:20:00',17),
        (18,3,'2023-02-17 13:50:00',18),
        (19,2,'2023-02-19 17:25:00',19),
        (20,1,'2023-02-21 09:40:00',20);

        -- =========================
        -- TABELA: cartao
        -- =========================
        INSERT INTO cartao (id, num_cartao, nom_impresso, data_criacao_cartao, id_conta, id_associado) VALUES
        (1,50000001,'João Silva','2023-01-11 09:00:00',1,1),
        (2,50000002,'Maria Santos','2023-01-13 10:00:00',2,2),
        (3,50000003,'Carlos Oliveira','2023-01-16 11:00:00',3,3),
        (4,50000004,'Ana Pereira','2023-01-19 12:00:00',4,4),
        (5,50000005,'Pedro Costa','2023-01-21 13:00:00',5,5),
        (6,50000006,'Juliana Rodrigues','2023-01-23 14:00:00',6,6),
        (7,50000007,'Marcos Almeida','2023-01-26 15:00:00',7,7),
        (8,50000008,'Fernanda Lima','2023-01-28 16:00:00',8,8),
        (9,50000009,'Lucas Gomes','2023-01-31 17:00:00',9,9),
        (10,50000010,'Patricia Nogueira','2023-02-02 09:00:00',10,10),
        (11,50000011,'Rafael Martins','2023-02-04 10:00:00',11,11),
        (12,50000012,'Camila Araujo','2023-02-06 11:00:00',12,12),
        (13,50000013,'Bruno Ribeiro','2023-02-08 12:00:00',13,13),
        (14,50000014,'Renata Barbosa','2023-02-10 13:00:00',14,14),
        (15,50000015,'Diego Teixeira','2023-02-12 14:00:00',15,15),
        (16,50000016,'Aline Freitas','2023-02-14 15:00:00',16,16),
        (17,50000017,'Eduardo Pacheco','2023-02-16 16:00:00',17,17),
        (18,50000018,'Larissa Farias','2023-02-18 17:00:00',18,18),
        (19,50000019,'Thiago Moura','2023-02-20 09:00:00',19,19),
        (20,50000020,'Beatriz Cunha','2023-02-22 10:00:00',20,20);

        -- =========================
        -- TABELA: movimento
        -- =========================
        INSERT INTO movimento (id, vlr_transacao, des_transacao, data_movimento, id_cartao) VALUES
        (1,125.90,'Compra supermercado','2023-03-01 10:15:00',1),
        (2,45.70,'Compra farmácia','2023-03-01 11:30:00',2),
        (3,220.00,'Compra loja de roupas','2023-03-01 12:40:00',3),
        (4,89.50,'Compra restaurante','2023-03-01 13:20:00',4),
        (5,60.00,'Compra padaria','2023-03-01 14:10:00',5),
        (6,150.30,'Abastecimento combustível','2023-03-01 15:00:00',6),
        (7,32.90,'Compra cafeteria','2023-03-01 16:45:00',7),
        (8,410.00,'Compra eletrônicos','2023-03-01 17:30:00',8),
        (9,25.00,'Pagamento aplicativo transporte','2023-03-01 18:00:00',9),
        (10,78.60,'Compra farmácia','2023-03-01 19:10:00',10),
        (11,199.99,'Compra online marketplace','2023-03-02 09:20:00',11),
        (12,54.40,'Compra livraria','2023-03-02 10:30:00',12),
        (13,310.00,'Compra supermercado','2023-03-02 11:40:00',13),
        (14,90.00,'Compra restaurante','2023-03-02 12:50:00',14),
        (15,140.75,'Compra farmácia','2023-03-02 14:00:00',15),
        (16,22.00,'Compra cafeteria','2023-03-02 15:15:00',16),
        (17,180.00,'Compra loja de calçados','2023-03-02 16:30:00',17),
        (18,65.90,'Compra padaria','2023-03-02 17:40:00',18),
        (19,250.00,'Compra eletrônicos','2023-03-02 18:50:00',19),
        (20,35.00,'Pagamento aplicativo transporte','2023-03-02 19:30:00',20);
    """

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(sql)
        conn.commit()
    finally:
        cur.close()
        conn.close()


def consultar_dados(sql):
    
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(sql)
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()

CREATE TABLE PRODUTO(
    COD_PRODUTO SERIAL PRIMARY KEY,
    NOME_PRODUTO VARCHAR(100),
    VALOR NUMERIC(10,2),
    QUANTIDADE INTEGER,
    CATEGORIA VARCHAR(10) CHECK(CATEGORIA IN ('Vinho', 'Whisky', 'Vodka', 'Cerveja', 'Champanhe', 'Tequila', 'Gin', 'Conhaque', 'Licor'))
);

/*VALORES ESTÃO SOMADOS*/

INSERT INTO PRODUTO (COD_PRODUTO, NOME_PRODUTO, VALOR, QUANTIDADE, CATEGORIA)
VALUES (1, '1945 Petrus 750ml', 42000.00, 1, 'Vinho');

INSERT INTO PRODUTO (COD_PRODUTO, NOME_PRODUTO, VALOR, QUANTIDADE, CATEGORIA)
VALUES (2, 'Royal Salute 21 anos 700ml', 2100.00, 1, 'Whisky');

INSERT INTO PRODUTO (COD_PRODUTO, NOME_PRODUTO, VALOR, QUANTIDADE, CATEGORIA)
VALUES (3, 'Absolut 1l', 69.99, 1, 'Vodka');

INSERT INTO PRODUTO (COD_PRODUTO, NOME_PRODUTO, VALOR, QUANTIDADE, CATEGORIA)
VALUES (4, 'Colorado Appia 600ml', 9.99, 1, 'Cerveja');

INSERT INTO PRODUTO (COD_PRODUTO, NOME_PRODUTO, VALOR, QUANTIDADE, CATEGORIA)
VALUES (5, 'Moet & Chandon Imperial Brut 750ml', 449.00, 1, 'Champanhe');

INSERT INTO PRODUTO (COD_PRODUTO, NOME_PRODUTO, VALOR, QUANTIDADE, CATEGORIA)
VALUES (6, 'Don Julio 750ml', 999.99, 1, 'Tequila');

INSERT INTO PRODUTO (COD_PRODUTO, NOME_PRODUTO, VALOR, QUANTIDADE, CATEGORIA)
VALUES (7, 'Beefeater London Dry 750ml', 360.00, 1, 'Gin');

INSERT INTO PRODUTO (COD_PRODUTO, NOME_PRODUTO, VALOR, QUANTIDADE, CATEGORIA)
VALUES (8, 'Richard Hennessy 700ml', 350.00, 1, 'Conhaque');

INSERT INTO PRODUTO (COD_PRODUTO, NOME_PRODUTO, VALOR, QUANTIDADE, CATEGORIA)
VALUES (9, 'Gekkeikan Black & Gold 750ml', 380.00, 1, '#');

INSERT INTO PRODUTO (COD_PRODUTO, NOME_PRODUTO, VALOR, QUANTIDADE, CATEGORIA)
VALUES (10, 'Bacardi Gran Reversa 8 anos 700ml', 160.00, 1, '#');

INSERT INTO PRODUTO (COD_PRODUTO, NOME_PRODUTO, VALOR, QUANTIDADE, CATEGORIA)
VALUES (11, 'Licor 43 700ml', 140.00, 1, 'Licor');


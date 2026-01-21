# Documentação do projeto sicooperative
Repositório do desafio técnico de carregamento de dados de movimentação de cartões.

Abaixo segue instruções para executar os scripts e realizar as cargas necessárias para a ingestão dos dados.

## Stack utilizada
* __PostgreSQL__ - Banco de dados utilizado para popular os dados
* __Python__ - Linguagem de programação utilizada para fazer aingestão dos dados no banco de dados PostgreSQL
* __Spark__ - Framework de processamento para realizar a extração dos dados, a transformação e o carregamento no Lake

## Criação do banco de dados, criar tabelas e popular os dados
Criar um banco de dados PostgreSQL chamado `sicooperative`. 

No Python, executar a instalação das bibliotecas necessárias para executar o projeto através do seguinte comando

```
pip install -r requirements.txt
```

Após a criação do banco de dados, abrir o código python `main.py` e realizar a execução do mesmo, esse código irá criar as tabelas e já popular as mesmas.

Caso seja necessário, realizar a troca dos parâmetros de host, porta e usuário dentro do arquivo `db.py`

## Script para realizar o ETL dos dados no Lake
Uma vez criado e populado as tabelas, abrir o notebook no spark `movimento_flat.ipynb` e executar o mesmo.

A carga já vai realizar a leitura do banco de dados, realizar os cruzamentos de dados necessários e gravar o arquivo flat `movimento_flat.csv` no diretório informado pelo usuário no código.

Caso seja necessário, também deverá ser alterado os parâmetros de conexão com o banco de dados, dentro do arquivo `utils.ipynb`.
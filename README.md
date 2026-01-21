# Documentação do projeto sicooperative
Repositório do desafio técnico de carregamento de dados de movimentação de cartões.

Abaixo segue instruções para executar os scripts e realizar as cargas necessárias para a ingestão dos dados.

## Stack utilizada
* __PostgreSQL__ - Banco de dados utilizado para popular os dados
* __Python__ - Linguagem de programação utilizada para fazer aingestão dos dados no banco de dados PostgreSQL
* __Spark__ - Framework de processamento para realizar a extração dos dados, a transformação e o carregamento no Lake

## Modelagem utilizada
Por ser uma carga simples, com poucos dados e a persistência em arquivos flat, não foi necessário realizar a modelagem do lake no formato medalão, por nesse caso não teria benefício utilizar este formato.

A parte importante do ETL, para principalmente não onerar o banco de dados de origem, é realizar o cruzamento dos dado dentro do Spark. Claro que no exemplo isso não afetaria, mas é um boa prática a seguir.

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

## Desafios encontrados
Por trabalhar com Databricks e já fazer um tempo que não utilizava mais o Spark puro, tive alguns contratempos para provisionar o ambiente e configurar para o ambiente funcionar corretamente.

## Melhorias Futuras
Fica como pontos de melhorias futuras, utilização de uma arquitetura medalhão, utilizar um serviço de secrets para guardar as credenciais utilizadas para acessar o banco de dados e não deixar as credenciais no código

Também configurar um docker compose configurando, automatizando e personalizando a criação dos recursos.

from repository import (
    criar_tabelas,
    inserir_dados,
    consultar_dados
)


def main():
    print("Criando tabela...")
    criar_tabelas()

    print("Populando Dados...")
    inserir_dados()

    print("Total de associados:")
    associados = consultar_dados("select count(*) from associado")
    for associado in associados:
        print(associado)


if __name__ == "__main__":
    main()

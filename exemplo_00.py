import csv

path_name = "vendas.csv"

def ler_csv(path_name_csv: str) -> list[dict]:
    """
    Função que recebe o caminho de um arquivo csv e retorna uma lista de dicionários
    """

    lista_dict = []
    with open(path_name_csv, 'r', encoding='latin-1') as arquivo:
        for linha in csv.DictReader(arquivo):
            lista_dict.append(linha)
    
    return lista_dict

def filtrar_produtos_entregues(lista_dict_produto: list[dict]) -> list[dict]:
    """
    Função que recebe uma lista de dicionários de produtos e retorna uma lista de dicionários
    de produtos entregues
    """
    lista_dict_produtos_entregues = []
    for produto in lista_dict_produto:
        if produto.get('Entregue', None) == "True":
            lista_dict_produtos_entregues.append(produto)

    return lista_dict_produtos_entregues

lista_dict_produtos = ler_csv("vendas.csv")

print(f"Lista de produtos: {lista_dict_produtos}")
print(f"Lista de produtos entregues:{filtrar_produtos_entregues(lista_dict_produtos)}")
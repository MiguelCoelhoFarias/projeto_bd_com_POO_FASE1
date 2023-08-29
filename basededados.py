import basedosdados as bd
import pandas
import requests
import json


# api gratuita que consome dados de usuarios de bandalarga fixa no brasil contendo a média por mês
df = bd.read_table(dataset_id='br_anatel_banda_larga_fixa',
                   table_id='densidade_brasil',
                   billing_project_id="projetobandalargafixa")
# acessando as tabelas da api
# usando o id do projeto criado na conta gcloud com meu email institucional

# transformando em dicionario para depois transformar em json:
data_dict = df.to_dict(orient='records')

# Escreve os dados em um arquivo JSON
with open('dados.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)
# espaçamento de 4 linhas como padrão de construção json
print("Dados exportados para dados.json")

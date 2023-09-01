import basedosdados as bd
import pandas as pd
import requests
import psycopg2
import csv
# api gratuita que consome dados de usuarios de bandalarga fixa no brasil contendo a média por mês
df = bd.read_table(dataset_id='br_anatel_banda_larga_fixa',
                   table_id='densidade_brasil',
                   billing_project_id="projetobandalargafixa")
# acessando as tabelas da api
# usando o id do projeto criado na conta gcloud com meu email institucional

# Transforma o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)
print("Dados exportados para dados.csv")

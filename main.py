import basedosdados as bd
import pandas as pd

# api gratuita que consome dados de usuários de banda larga fixa no Brasil contendo a média por mês
df = bd.read_table(dataset_id='br_anatel_banda_larga_fixa',
                   table_id='densidade_brasil',
                   billing_project_id="projetobandalargafixa")

# Transforma o DataFrame em um arquivo JSON com orientação 'records'
df.to_json('dados.json', orient='records', lines=True)

# Abre o arquivo JSON gerado e lê cada linha para formatá-lo corretamente
with open('dados.json', 'r') as json_file:
    lines = json_file.readlines()

# Remove quebras de linha e vírgula no final da última linha
formatted_data = '[' + ','.join(lines) + ']'

# Reescreve o arquivo JSON com a formatação correta
with open('dados.json', 'w') as json_file:
    json_file.write(formatted_data)

print("Dados exportados para dados.json")

# Script criado por Rildo Souza - rildo.ras@gmail.com
# Data: 15/01/2024

import json
from jinja2 import Template

# Como sabemos que o json_data é um dicionário
# Vamos focar nas chaves que contêm os dados que queremos exibir em HTML.

# Informar qual é o arquivo json que iremos trabalhar
file_path = '/home/rildo/Documents/Kubernetes/kubernetes_conf/resultados/results.json'

# Ler e parsear o arquivo JSON
with open(file_path, 'r') as file:
    json_data = json.load(file)

# Extrair e exibir algumas informações importantes do JSON 
info_keys = ['kics_version', 'files_scanned', 'lines_scanned', 'files_parsed', 'lines_parsed']
info_data = {key: json_data[key] for key in info_keys}

# Analisando o arquivo é possível assumir que os resultados que queremos estão na chave 'queries' 
if 'queries' in json_data:
    queries_sample = json_data['queries'][:1]  # Mostrando apenas os primeiros 5 itens para amostra (esse número irá variar conforme o número de vulnerabilidades que aparecerem no .json)

info_data, queries_sample if 'queries' in json_data else "Chave 'queries' não encontrada no JSON - validação"


# Criando o template HTML para exibir os dados
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KICS Scan Results</title>
    <style>
        body { font-family: Arial, sans-serif; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background-color: #f2f2f2; }
        tr:hover { background-color: #ddd; }
    </style>
</head>
<body>
    <h1>KICS Scan Results</h1>
    <h2>Scan Information</h2>
    <table>
        <tr>
            {% for key, value in info_data.items() %}
                <th>{{ key }}</th>
            {% endfor %}
        </tr>
        <tr>
            {% for key, value in info_data.items() %}
                <td>{{ value }}</td>
            {% endfor %}
        </tr>
    </table>

    <h2>Queries</h2>
    {% for query in queries %}
        <h3>{{ query.query_name }} (Severity: {{ query.severity }})</h3>
        <p>{{ query.description }}</p>
        <table>
            <tr>
                <th>File Name</th>
                <th>Resource Type</th>
                <th>Resource Name</th>
                <th>Issue Type</th>
                <th>Expected Value</th>
                <th>Actual Value</th>
            </tr>
            {% for file in query.files %}
                <tr>
                    <td>{{ file.file_name }}</td>
                    <td>{{ file.resource_type }}</td>
                    <td>{{ file.resource_name }}</td>
                    <td>{{ file.issue_type }}</td>
                    <td>{{ file.expected_value }}</td>
                    <td>{{ file.actual_value }}</td>
                </tr>
            {% endfor %}
        </table>
    {% endfor %}
</body>
</html>
"""

# Gerando o HTML
template = Template(html_template)
html_content = template.render(info_data=info_data, queries=json_data['queries'])

# Salvando o HTML em um arquivo
output_html_path = '/home/rildo/Documents/Kubernetes/kubernetes_conf/resultados/results.html'
with open(output_html_path, 'w') as html_file:
    html_file.write(html_content)

print(output_html_path)
# Script created by Rildo Souza - rildo.ras@gmail.com
# Data: 15/01/2024

import json
from jinja2 import Template

# As we know that json_data is a dictionary
# Let's focus on the keys that contain the data we want to display in HTML.

# Specify which json file we will be working with ( Kics file that was created)
file_path = '/dir/kics-example.json'

# Read and parser the Json file
with open(file_path, 'r') as file:
    json_data = json.load(file)


# Extract and display some important information from the JSON
info_keys = ['kics_version', 'files_scanned', 'lines_scanned', 'files_parsed', 'lines_parsed']
info_data = {key: json_data[key] for key in info_keys}

# Analyzing the file, we can assume that the results we want are in the 'queries' key
if 'queries' in json_data:
    queries_sample = json_data['queries'][:1]  # Displaying only the first 5 items for sampling (this number will vary depending on the number of vulnerabilities that appear in the .json)

info_data, queries_sample if 'queries' in json_data else "Key 'queries' not found in JSON file- Validation"


# Create a template to display the data
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

# Creating a HTML file
template = Template(html_template)
html_content = template.render(info_data=info_data, queries=json_data['queries'])

# Save the html file
output_html_path = '/dir/filename.html'
with open(output_html_path, 'w') as html_file:
    html_file.write(html_content)

print(output_html_path)

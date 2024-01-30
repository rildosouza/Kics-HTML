# Kics_html
Create a personal report in html format using Kicks 

The HTML format created by the kics tool does not allow you to customize and group vulnerabilities by severity. Given these facts, the idea emerged to take the report in json format and create a script that converts it to HTML in a way that allows the user to specify.

License and author

This application is distributed under the GNU license.

Contact the author at rildo.ras@gmail.com

Dependency, Library and Environment:

Kics Reports has been tested in the following environment:

Python 3.10.12
kics 1.7.12

Running the Application

1 - You need a kics json scan file(First)

2 - Install Python 3.10.12

3 - Install ninja2 library

4 - Create your html template(we provide a example)

5 - Inform the file path(json kics file)

6 - Inform the output file path (html file)

6 - python3 kics_json_to_html.py

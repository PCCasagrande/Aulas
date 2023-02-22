import requests
import pandas as pd

url = "https://www.sintegraws.com.br/api/v1/execute-api.php"

querystring = {"token":"D8863F1A-F8C0-47DE-8C9E-E9D74E4CFAF8","cnpj":"06990590000123","plugin":"ST"}

response = requests.request("GET", url, params=querystring)

print(response.text)



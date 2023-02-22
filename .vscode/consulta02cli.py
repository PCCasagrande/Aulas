import http.client

token = "D8863F1A-F8C0-47DE-8C9E-E9D74E4CFAF8"
cnpj = "06990590000123";
plugin = "ST";

url =  "/api/v1/execute-api.php?token=" + token + "&cnpj=" + cnpj + "&plugin=" + plugin;

conn = http.client.HTTPSConnection("www.sintegraws.com.br")

conn.request("GET", url)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))




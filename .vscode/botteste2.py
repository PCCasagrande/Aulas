from os import scandir
from os.path import getmtime


files = scandir('D:\Patrick_Tudo\Patrick_Tudo\A')
mais_antigo = 0
arquivo_mais_recente = None

for entry in files:
    if entry.is_file() and entry.name.lower().endswith('.txt'):
        modificado_em = getmtime(entry.path)

        if mais_antigo < modificado_em:
            mais_antigo = modificado_em
            arquivo_mais_recente = entry.path

print(arquivo_mais_recente)
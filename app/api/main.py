# Importanto Bibliotecas
import requests
from pathlib import Path

# Definindo URL da API para extrair texto de imagem
api_url = 'COLOCAR URl DA API AQUI'

# Abrindo uma imagem em uma variável para usar no corpo da requisição
image_file_descriptor = open('teste.jpg', 'rb')

print(image_file_descriptor)

# Formatando um JSON para a requisição
files = {'image': image_file_descriptor}

# Formatando um header para adicionar a chave da API
api_key = 'COLOCAR A CHAVE DA API AQUI'
headers = {'X-Api-Key': api_key}

# Realizando o POST para text extract
r = requests.post(api_url, files=files, headers=headers)

# Formatando a response em formato de JSON
json_extract = r.json()

# Formatando o texto através de uma estrutura de repetição
texto_formatado = ""

for i in range(len(json_extract)):
    palavra = json_extract[i]['text']
    texto_formatado += palavra + ' '

print(texto_formatado)
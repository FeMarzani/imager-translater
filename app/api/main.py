# Importanto Bibliotecas
import requests
from pathlib import Path
from openai import OpenAI

def text_extract(arqu_path):

    # Definindo URL da API para extrair texto de imagem
    api_key = 'COLOCAR CHAVE DA API AQUI'

    # Abrindo uma imagem em uma variável para usar no corpo da requisição
    image_file_descriptor = open(arqu_path, 'rb')

    print(image_file_descriptor)

    # Formatando um JSON para a requisição
    files = {'image': image_file_descriptor}

    # Formatando um header para adicionar a chave da API
    api_url = 'COLOCAR URL DA API AQUI'
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

    return texto_formatado

def text_translate(texto_formatado):

    # Cliente OpenAI
    client = OpenAI(api_key="COLOCAR CHAVE DA API AQUI")

    messages = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f'Traduza a seguinte frase para o português: {texto_formatado}'}
        ]
    )

    # Retorna o resumo gerado
    messages = messages.choices[0].message.content

    return messages
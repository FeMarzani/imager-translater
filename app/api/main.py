# Importanto Bibliotecas
import requests
import io
from pathlib import Path
from openai import OpenAI
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

# Cliente OpenAI
client = OpenAI(api_key="COLOCAR CHAVE DA API AQUI")

app = Flask(__name__)

CORS(app)

# Definindo funções:

# Função para extrair texto de imagem.
def text_extract(arqu_path):

    # Definindo URL da API para extrair texto de imagem
    api_key = 'COLOCAR CHAVE DA API AQUI'

    # Formatando um JSON para a requisição
    files = {'image': arqu_path}

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

# Função para realizar a tradução do texto retirado da imagem.
def text_translate(texto_formatado):

    texto_traduzido = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f'Traduza a seguinte frase para o português: {texto_formatado}'}
        ]
    )

    # Retorna o resumo gerado
    texto_traduzido = texto_traduzido.choices[0].message.content

    return texto_traduzido

# Criando uma rota de API do tipo POST
@app.route('/traducao', methods=['POST'])
def speech():

    # Verificando se há uma imagem na requisição enviada.
    if 'image' not in request.files:
        return jsonify({'error': 'Nenhuma imagem enviada'}), 400

    image = request.files['image']

    # Verificando o nome do arquivo corretamente
    if image.filename == '':
        return jsonify({'error': 'Nome do arquivo vazio'}), 400

    # Lendo o arquivo diretamente na memória.
    arqu_path = io.BytesIO()
    image.save(arqu_path)
    arqu_path.seek(0)

    # Extraindo texto da imagem.
    texto_formatado = text_extract(arqu_path)

    # Traduzindo texto da imagem.
    texto_traduzido = text_translate(texto_formatado)

    # Realizando agora o text to speech
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=texto_traduzido
    )

    response.stream_to_file(speech_file_path)

    return send_file(speech_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)



<div align="center">
    <img align="center" alt="Teams-Logo" height="200" width="200" src="https://freeiconshop.com/wp-content/uploads/edd/image-outline-filled.png">
    <h2>Imager Converter</h2>
</div>

### Ferramentas Utilizadas 📚
<div style="display: inline-block">
  <img align="center" alt="Html" height="33" width="44" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg">
  <img align="center" alt="Css" height="33" width="44" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg">
  <img align="center" alt="Javascript" height="28" width="42" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-plain.svg">
  <img align="center" alt="Git" height="28" width="42" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg">
  <img align="center" alt="Python" height="32" width="42" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg">
  <img align="center" alt="Flask" height="44" width="60" src="https://raw.githubusercontent.com/devicons/devicon/v2.15.1/icons/flask/flask-original-wordmark.svg">
</div>

---

### 1️⃣ Descrição
O Imager Converter é uma ferramenta que permite o usuário traduzir uma imagem com texto em qualquer tipo de idioma para o português. Posteriormente, esta ferramente converte essa tradução da imagem para áudio. Portanto, é um conversor de imagem para áudio!
- Permite envio de imagem (png, jpg etc...).
- Retorna um áudio para o usuário, do tipo .mp3, contendo o conteúdo da imagem (texto) traduzida e em formato de áudio.

---

### 2️⃣ Estrutura de Pastas
- **app**
    - **api**
        - `main.py`
    - **css**
        - `style.css`
    - **js**
        - `script.js`
    - `index.html`

### 3️⃣ Como utilizar?
1. Clone este repositório,

2. É necessário ter Python instalado para o restante das ações, portanto se não possuir, instale. 

3. Instale as seguintes bibliotecas abaixo:

    ```bash
    pip3 install requests openai flask flask-cors
    ```

4. Cadastre sua chave de API da OpenAI e coloque ela na respectiva posição da linha 10 do arquivo ```app/api/main.py```. Posteriormente, crie sua conta na api-ninjas para obter uma chave de API e adicione a chave da api e a URL da API do tipo imagetotext nas respectivas linhas 22 e 28 da ```app/api/main.py```.

5. Por fim, abra o terminal dentro da pasta api. Verifique se quando abrir o terminal, está no caminho da pasta corretamente. Do contrário use o comando para ir da raiz até a pasta:

    ```bash
    cd app/api
    ```

6. Execute o arquivo ```main.py```:

    ```bash
    python3 main.py
    ```

7. Agora a API Flask estará pronta para uso. Portanto, abra o ```index.html``` no seu navegador e teste o envio do formulário utilizando algum arquivo de imagem. 

8. Assim que o enviar imagem for executado, juntamente com a execução da API Flask, será mostrada uma mensagem na tela e depois de alguns segundos um áudio será baixado contendo o conteúdo traduzido da imagem. 
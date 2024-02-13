function exibirNomeArquivo(input) {
    if (input.files && input.files[0]) {
        var nomeArquivo = input.files[0].name;
        document.getElementById('nome-arquivo').innerHTML = 'Arquivo selecionado: ' + nomeArquivo;
    }
};

document.querySelector('form').addEventListener('submit', function() {
    document.getElementById('retorno').style.display = 'block';
});
document.addEventListener('DOMContentLoaded', function() {
    const botaoPerfil = document.querySelector('.perfil');
    const dados = document.querySelector('.dados');
    const tituloConsultas = document.getElementById('titulo-consultas'); 

    botaoPerfil.addEventListener('click', function() {
        if (dados.style.visibility === 'hidden' || !dados.style.visibility) {
            dados.style.visibility = 'visible';
        }
        tituloConsultas.innerText = 'Dados';
    });
});

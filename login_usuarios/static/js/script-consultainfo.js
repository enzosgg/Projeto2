const mensagem = document.getElementById('mensagem');
const divConfirmacao = document.getElementById('confirmacao');
const linhas = document.querySelectorAll('.table-container tbody tr');

function mostrarMensagem(acao) {
    acaoEscolhida = acao;
    if (acao === 'confirmar') {
        mensagem.textContent = 'Deseja realmente confirmar a consulta?';
        divConfirmacao.style.display = 'flex';
    } else if (acao === 'cancelar') {
        mensagem.textContent = 'Deseja realmente cancelar a consulta?';
        divConfirmacao.style.display = 'flex';
    } else if (acao === 'reagendar') {
        document.getElementById('tabela-dados').style.display = 'none';
        document.querySelector('.table-container').style.display = 'block';
        document.getElementById('titulo-consultas').textContent = 'Reagendar consulta';
        adicionarEventoClicarNasLinhas();

        linhas.forEach(linha => {
            linha.addEventListener('click', function() {
                mostrarMensagem('remarcar');
            });
        });
    } else if (acao === 'remarcar') {
        mensagem.textContent = 'Deseja realmente remarcar a consulta para esta data?';
        divConfirmacao.style.display = 'flex';
    }
}

function fecharMensagem() {
    divConfirmacao.style.display = 'none';
}

function acaoConfirmada() {
    if (acaoEscolhida === 'confirmar') {
        alert('Consulta confirmada com sucesso!');
    } else if (acaoEscolhida === 'cancelar') {
        alert('Consulta cancelada com sucesso!');
    } else if (acaoEscolhida === 'remarcar') {
        alert('Consulta remarcada com sucesso!');
    }
    fecharMensagem();
}

function adicionarEventoClicarNasLinhas() {
    const linhas = document.querySelectorAll('.table-container tbody tr');
    linhas.forEach(linha => {
        linha.addEventListener('click', function() {
            acaoEscolhida = 'remarcar';
            mensagem.textContent = 'Deseja realmente remarcar a consulta?';
            divConfirmacao.style.display = 'flex';
        });
    });
}

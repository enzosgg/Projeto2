const btnConfirmar = document.getElementById('btnConfirmar');
const btnCancelar = document.getElementById('btnCancelar');
const btnReagendar = document.getElementById('btnReagendar');
const consultasAlternativas = document.getElementById('consultas-alternativas');
const tituloConsultas = document.getElementById('titulo-consultas');
const formularioConsulta = document.getElementById('formulario-consulta');
const consultaIdAtual = btnCancelar.getAttribute('data-id');

document.addEventListener('DOMContentLoaded', function() {


    btnConfirmar.addEventListener('click', function() {
        alert('Consulta confirmada com sucesso!');
    });

    btnCancelar.addEventListener('click', function() {
        if (confirm('Certeza que deseja cancelar a consulta?')) {
            const consultaId = btnCancelar.getAttribute('data-id');
            window.location.href = `/cancelar_consulta/${consultaId}/`;
        }
    });

    btnReagendar.addEventListener('click', function() {
        formularioConsulta.style.display = 'none';
        tituloConsultas.textContent = 'Consultas alternativas para reagendamento';
        consultasAlternativas.style.display = 'block';
    });

    consultasAlternativas.querySelectorAll('tr[data-consulta-id]').forEach(row => {
        row.addEventListener('click', function() {
            if (confirm('Tem certeza de que deseja reagendar a consulta?')) {
                const novaConsultaId = row.getAttribute('data-consulta-id');
                window.location.href = `/reagendar_consulta/${consultaIdAtual}/${novaConsultaId}/`;
            }
        });
    });
});
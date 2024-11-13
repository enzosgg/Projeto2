from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from .models import Usuario, Consulta


def usuarios_ou_perfil(request, usuario_id=None):
    usuario_logado_id = request.session.get('usuario_id')

    if not usuario_logado_id:
        return redirect('login')

    usuarios = []
    consultas = []

    if usuario_id is not None:
        try:
            if usuario_id == usuario_logado_id:
                usuarios = Usuario.objects.filter(id_usuario=usuario_id)
                usuario = usuarios.first()

                if request.method == 'POST':
                    telefone = request.POST.get('telefone')
                    email = request.POST.get('email')

                    usuario.telefone = telefone
                    usuario.email = email
                    usuario.save()

                    return redirect('perfil_usuario', usuario_id=usuario.id_usuario)

            else:
                return redirect('listagem_usuarios')
        except Usuario.DoesNotExist:
            usuarios = []
        template = 'html/perfil.html'
    else:
        usuarios = Usuario.objects.filter(id_usuario=usuario_logado_id)
        consultas = Consulta.objects.filter(usuario_id=usuario_logado_id)
        template = 'html/usuarios.html'

    return render(request, template, {'usuarios': usuarios, 'consultas': consultas})


def login(request):
    if request.method == 'POST':
        cpf = request.POST.get('CPF', '').replace('.', '').replace('-', '')
        senha = request.POST.get('Senha', '')

        try:
            usuario = Usuario.objects.get(CPF=cpf)
            if senha == usuario.Senha:

                request.session['usuario_id'] = usuario.id_usuario
                return redirect('listagem_usuarios')
            else:

                return redirect(f'{reverse("login")}?error=invalid')
        except Usuario.DoesNotExist:

            return redirect(f'{reverse("login")}?error=invalid')

    error_message = "CPF ou Senha inválidos." if request.GET.get(
        'error') == 'invalid' else None
    return render(request, 'html/index.html', {'error_message': error_message})


def consulta_info(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    usuario_id = request.session.get('usuario_id')
    usuario = get_object_or_404(Usuario, id_usuario=usuario_id)

    consultas_alternativas = Consulta.objects.exclude(
        id=consulta_id).filter(usuario__isnull=True)

    return render(request, 'html/consultainfo.html', {
        'consulta': consulta,
        'consultas_alternativas': consultas_alternativas,
        'usuario_nome': usuario.Nome
    })


def cancelar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    consulta.delete()
    messages.success(request, 'Consulta cancelada com sucesso!')
    return redirect('listagem_usuarios')


def reagendar_consulta(request, consulta_id, nova_consulta_id):

    consulta_atual = get_object_or_404(Consulta, id=consulta_id)
    nova_consulta = get_object_or_404(Consulta, id=nova_consulta_id)

    consulta_atual.data = nova_consulta.data
    consulta_atual.hora = nova_consulta.hora
    consulta_atual.medico = nova_consulta.medico
    consulta_atual.especialidade = nova_consulta.especialidade
    consulta_atual.local = nova_consulta.local
    consulta_atual.endereco = nova_consulta.endereco
    consulta_atual.save()

    nova_consulta.delete()

    messages.success(request, "Consulta reagendada com sucesso!")
    return redirect('listagem_usuarios')

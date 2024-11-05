from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
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
    return render(request, 'html/consultainfo.html', {'consulta': consulta})
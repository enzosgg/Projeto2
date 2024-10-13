from django.shortcuts import render

def login(request):
    return render(request, 'html/index.html')


def usuarios(request):
    return render(request, 'html/usuarios.html')

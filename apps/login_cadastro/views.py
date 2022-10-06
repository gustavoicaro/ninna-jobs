from vaga.models import Vagas
from .models import Users, Candidato, Empresa, AreaDeInteresse, Genero, Estado, FormacaoAcademica, Mes, Ano, Conquista, NivelIdioma
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from rolepermissions.decorators  import has_permission_decorator
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

def cadastro_candidato(request):
    if request.method == 'POST':
        candidato_nome = request.POST['candidato_nome']
        candidato_email = request.POST['candidato_email']
        candidato_senha = request.POST['candidato_senha']
        candidato_senha_conf = request.POST['candidato_senha_conf']
        print(candidato_email, candidato_senha, candidato_senha_conf)
        if candidato_senha != candidato_senha_conf:
            return redirect ('cadastro_candidatos')
        if Users.objects.filter(email=candidato_email).exists():
            messages.error(request, 'Usuario ja cadastrado')
            return redirect('longar_candidato')
        if Users.objects.filter(username=candidato_nome).exists():
            messages.error(request, 'Usuario ja cadastrado')
            return redirect('longar_candidato')
        candidato_user = Users.objects.create_user(username=candidato_nome, email=candidato_email, password=candidato_senha, funcao = "CAN")
        candidato_user.save()
        # candidato_user_na_tablela_user = User.objects.create_user(username=candidato_nome, email=candidato_email, password=candidato_senha)
        # candidato_user_na_tablela_user.save()
        candidato = Candidato.objects.create(email=candidato_email, senha=candidato_senha, nome=candidato_nome, nivel_prog="None", nivel_ing="None")
        candidato.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        print('Usuário cadastrado com sucesso')
        return redirect ('longar_candidato')
    else:
        return render(request, 'formcandidato.html')


def cadastro_empresa(request):
    if request.method == 'POST':
        empresa_nome = request.POST['empresa_nome']
        empresa_email = request.POST['empresa_email']
        empresa_senha = request.POST['empresa_senha']
        empresa_senha_conf = request.POST['empresa_senha_conf']
        print (empresa_email, empresa_senha)
        empresa_user = Users.objects.create_user(username=empresa_nome, email=empresa_email, password=empresa_senha, funcao = "EMP")
        empresa_user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
        return redirect('longar_empresa')


    else:
        return render(request, 'formempresa.html')


def logar_candidato(request):

    if request.method == 'POST':
        candidato_email = request.POST.get('candidato_email', None)
        candidato_senha = request.POST.get('candidato_senha', None)
        print(candidato_email, candidato_senha)

        if Users.objects.filter(email=candidato_email).exists():
            nome = Users.objects.filter(email=candidato_email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=candidato_senha, funcao = "CAN")
            print(nome)
            print(user)
            if user:
                auth.login(request, user)
                print("autenticado")
                return redirect('index')
        messages.error(request, "candidato não cadastrado")

    return render(request, 'loginCandidato.html')

# LOGAR EMPRESA
def logar_empresa(request):
    empresa_email = None
    empresa_email = None
    if request.method == 'POST':
        empresa_email = request.POST.get('empresa_email', None)
        empresa_senha = request.POST.get('empresa_senha', None)
        print(empresa_email, empresa_senha)
        if Users.objects.filter(email=empresa_email).exists():
            nome = Users.objects.filter(email=empresa_email).values_list('username', flat=True).get()
            user = auth.authenticate(username=nome, password=empresa_senha, funcao="EMP")
            if user:
                print("autenticado")
                return redirect('empresa')
            else:
                print("Email ou senha incorretos")
                print(f" resultado do user: {user} \nresultado do nome: {nome}")
        else:
            print("Email ou senha incorretos")

    return render(request, 'formempresa.html')

def nao_pode_estar_vazio(empresa_email, empresa_senha, candidato_email, candidato_senha):
    return (empresa_email == "" or empresa_senha == "") or (candidato_email == "" or candidato_senha == "")

def plataforma(request):
    '''exemplo de quando for para a tela principal'''
    if request.user.is_authenticated:
        return HttpResponse("tela de vagas")
    return redirect('login')

def arquivadas(request):
    return render(request, 'arquivadas.html')


def cadastro_candidato_2(request):
    #area = AreaDeInteresse.objects.all()
    generos = Genero.objects.all()
    estados = Estado.objects.all()
    #formacao = FormacaoAcademica.objects.all()
    #mes = Mes.objects.all()
    #ano = Ano.objects.all()
    #conquista = Conquista.objects.all()
    #idioma = NivelIdioma.objects.all()


    dados = {
        #'area' : area,
        'generos' : generos,
        'estados' : estados
    }
    return render(request, 'formcandidato.html', dados)

# def tela_404(request, exception):
    '''ERRO 404'''
#     return render(request, '404.html')
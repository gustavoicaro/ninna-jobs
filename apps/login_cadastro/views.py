from vaga.models import Vagas
from .models import Users, Candidato, Empresa, AreaDeInteresse, Genero, Estado, FormacaoAcademica, Mes, Ano, Conquista, NivelIdioma
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.shortcuts import render, redirect
from rolepermissions.decorators import has_permission_decorator
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
        return render(request, 'loginCandidato.html')

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
        return render(request, 'login.html')

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

def sair(request):
    '''Desloga uma pessoa'''
    auth.logout(request)
    return redirect('index')

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

    return render(request, 'loginEmpresa.html')

def recuperar_senha(request):
    # if request.method == 'POST':
    #     email = request.POST.get('email', None)
    #     if Candidato.objects.filter(email=email).exists():# vê se é email de um cadidato
    #         senha_canditato = Candidato.objects.filter(email=email).values_list('senha', flat=True).get()
    #         print(f"senha candidato: {senha_canditato}")
    #         html_content = render_to_string('email/recuperar_senha.html', {'senha' : senha_canditato})
    #         text_content = strip_tags(html_content)

    #         email = EmailMultiAlternatives('Recuperar senha', text_content, settings.EMAIL_HOST_USER, [email])
    #         email.attach_alternative(html_content, 'text/html')
    #         email.send()

    #     # vê se é email de uma empresa
    #     elif Empresa.objects.filter(email=email).exists():
    #         senha_empresa = Empresa.objects.filter(email=email).values_list('senha', flat=True).get()
    #         print(f"senha empresa: {senha_empresa}")
    #         html_content = render_to_string('email/recuperar_senha.html', {'senha' : senha_empresa})
    #         text_content = strip_tags(html_content)

    #         email = EmailMultiAlternatives('Recuperar senha', text_content, settings.EMAIL_HOST_USER, [email])
    #         email.attach_alternative(html_content, 'text/html')
    #         email.send()
    #         print('enviou o email para empresa')


    #         # try:
    #         #     senha_canditato = Candidato.objects.filter(email=email).values_list('senha', flat=True).get()
    #         #     senha_empresa = Empresa.objects.filter(email=email).values_list('senha', flat=True).get()
    #         # except:
    #         #     if senha_canditato != None:
    #         #         print(email, senha_canditato)
    #         #     elif senha_empresa != None:
    #         #         print(email, senha_empresa)
    #         #     pass
    #         # if senha_canditato !=
    #         # send_mail("assunto", "esse é o email", "ninnajobs72@gmail.com", [email])
    #     else:
    #         print('email não cadastrado')
    return render(request, 'emails/pedirEmail.html')

def nao_pode_estar_vazio(empresa_email, empresa_senha, candidato_email, candidato_senha):
    return (empresa_email == "" or empresa_senha == "") or (candidato_email == "" or candidato_senha == "")

def plataforma(request):
    '''exemplo de quando for para a tela principal'''
    if request.user.is_authenticated:
        return HttpResponse("tela de vagas")
    return redirect('login')

def arquivadas(request):
    return render(request, 'arquivadas.html')

def empresa(request):
    return render(request, 'empresa.html')

def cadastro_candidato_2(request):
    areas = AreaDeInteresse.objects.all()
    generos = Genero.objects.all()
    estados = Estado.objects.all()
    formacoes = FormacaoAcademica.objects.all()
    meses = Mes.objects.all()
    anos = Ano.objects.all()
    conquistas = Conquista.objects.all()
    niveis = NivelIdioma.objects.all()


    dados = {
        'areas' : areas,
        'generos' : generos,
        'estados' : estados,
        'formacoes' : formacoes,
        'meses' : meses,
        'anos' : anos,
        'conquistas' : conquistas,
        'niveis' : niveis
    }
    return render(request, 'formcandidato.html', dados)

# def tela_404(request, exception):
    '''ERRO 404'''
#     return render(request, '404.html')
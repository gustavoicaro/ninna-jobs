from django.urls import path
from . import views

urlpatterns = [
    path('login/candidato/', views.logar_candidato, name='longar_candidato'),
    path('login/empresa/', views.logar_empresa, name='longar_empresa'),
    path('recuperar_senha', views.recuperar_senha, name='recuperar_senha'),
    path('cadastro/candidato/', views.cadastro_candidato, name='cadastro_candidato'),
    path('cadastro/empresas/', views.cadastro_empresa, name='cadastro_empresa'),

    path('cadastrar/candidato/', views.cadastro_candidato_2, name='cadastro_candidato_2'),
    # para testar as partials
    path('arquivadas', views.arquivadas, name='arquivadas'),
    path('empresa/', views.empresa, name='empresa'),

    path('sair', views.sair, name='sair') #sair
]

from django.urls import path
from . import views

urlpatterns = [
    path('formulario/empresa/', views.registro, name='registro'),
    path('formulario/empresa/2', views.editar_registro, name='editar_registro'),
    path('apagar/formulario/empresa/', views.apagar_form_empresa, name='apagar_form_empresa'),
    path('editar/perfil/', views.formempresa, name='formempresa'),
    path('Informacoes/Iniciais/', views.formcandidato, name='formcandidato'),#form 1
    path('Dados/Pessoais/', views.informacoes_iniciais, name='Informacoes_iniciais'),#form 2
    path('ApagarInformacoes/Iniciais/', views.apagar_informacoes_iniciais, name='apagar_informacoes_iniciais'),#form 2
    path('Dados/Pessoais/2', views.editando_informacoes_iniciais, name='editando_informacoes_iniciais'),#caso o usuario volte
    path('Formacao/Academica/', views.dados_pessoais, name='Dados_Pessoais'),#form 3
    path('Apagar/Dados/Pessoais', views.apagar_dados_pessoais, name='apagar_dados_pessoais'),#form 3
    path('Formacao/Academica/2', views.editando_dados_pessoais, name='editando_Dados_Pessoais'),#form 3
    path('Certificados/Conquistas/', views.formacao_academica, name='Formacao_academica'),#form 4
    path('apagarF/<int:id_formacao>', views.deleta_formacao, name='apagarF'),#apaga formacao
    path('adicionarF', views.adicionar_formacao, name='adicionarF'),#adiciona Formaçao
    path('Experiencia/Profissional/', views.certificados_conquistas, name='Certificados_conquistas'),#form 5
    path('apagarC/<int:id_certificado>', views.deleta_certificado, name='apagarC'),#apaga Certificado
    path('adicionarC', views.adicionar_certificado, name='adicionarC'),#adiciona Certificado
    path('Nivel/Idioma/', views.experiencia_profissional, name='Experiencia_profissional'),#form 6
    path('apagarE/<int:id_experiencia>', views.deleta_experiencia, name='apagarE'),#apaga Experiencia
    path('adicionarE', views.adicionar_experiencia, name='adicionarE'),#adiciona nova Experiencia
    path('apagarI/<int:id_idioma>', views.deleta_idioma, name='apagarI'),#apaga Idiomas
    path('adicionarI', views.adicionar_idioma, name='adicionarI'),#adiciona novo idioma
    path('empresa/', views.empresa, name='empresa'),#dashboard de empresa
    path('dashboard/', views.dashboard, name='dashboard'),#dashboard de talento
    path('perfil', views.perfil, name='perfil'),#candidato ver o perfil
    path('perfil/empresa', views.perfilempresa, name='perfilempresa'),#empresa ver o perfil
    path('perfil/empresa/<int:id_empresa>', views.ver_perfil_empresa, name='ver_perfil_empresa'),#andidato ver o perfil de empresa
    path('perfil/candidato/<int:id_candidato>', views.perfil_candidato, name='perfil_candidato'),#empresa ver o perfil do candidato
    path('listar_candidatos/<int:pk_vaga>', views.listar_talentos_candidatados, name='listar_talentos_candidatados'),
    path('talentos', views.talentos, name='talentos'),#empresa ver candidatos
    path('resultados/', views.busca_talentos, name='busca_talentos'),#busca candidatos,
    path('empresas/favoritadas', views.empresas_favoritadas, name='empresas_favoritadas'),
    path('contato', views.contato, name='contato'),#busca candidatos
    path('favoritar_talento/<int:pk_talento>', views.favoritar_talento, name='favoritar_talento'),#favoritar talentos
    path('favoritar_empresa/<int:pk_empresa>', views.favoritar_empresa, name='favoritar_empresa'),#favoritar empresa
    path('configuracoes', views.configuracoes, name='configuracoes'),#apagar conta
    path('apagar/conta/verificao/', views.apagar_conta, name='apagar_conta'),
    path('candidato_fav', views.candidato_fav, name='candidato_fav'),
]

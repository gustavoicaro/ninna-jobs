from django.urls import path
from . import views

urlpatterns = [
    path('formulario/empresa/', views.registro, name='registro'),
    path('Informacoes/Iniciais/', views.cadastro_candidato_2, name='cadastro_candidato_2'),#form 1
    path('Dados/Pessoais/', views.Informacoes_iniciais, name='Informacoes_iniciais'),#form 2
    path('Dados/Pessoais/2', views.editando_informacoes_iniciais, name='editando_informacoes_iniciais'),#caso o usuario volte
    path('Formacao/Academica/', views.Dados_pessoais, name='Dados_Pessoais'),#form 3
    path('Formacao/Academica/2', views.editando_dados_pessoais, name='editando_Dados_Pessoais'),#form 3
    path('Certificados/Conquistas/', views.Formacao_academica, name='Formacao_academica'),#form 4
    path('apagarF/<int:id_formacao>', views.deleta_formacao, name='apagarF'),#apaga formacao
    path('adicionarF', views.adicionar_formacao, name='adicionarF'),#adiciona Formaçao
    path('Experiencia/Profissional/', views.Certificados_conquistas, name='Certificados_conquistas'),#form 5
    path('apagarC/<int:id_certificado>', views.deleta_certificado, name='apagarC'),#apaga Certificado
    path('adicionarC', views.adicionar_certificado, name='adicionarC'),#adiciona Certificado
    path('Nivel/Idioma/', views.Experiencia_profissional, name='Experiencia_profissional'),#form 6
    path('apagarE/<int:id_experiencia>', views.deleta_experiencia, name='apagarE'),#apaga Experiencia
    path('adicionarE', views.adicionar_experiencia, name='adicionarE'),#adiciona nova Experiencia
    path('apagarI/<int:id_idioma>', views.deleta_idioma, name='apagarI'),#apaga Idiomas
    path('adicionarI', views.adicionar_idioma, name='adicionarI'),#adiciona novo idioma
    path('empresa/', views.empresa, name='empresa'),#dashboard de empresa
    path('dashboard/', views.dashboard, name='dashboard'),
    path('perfil', views.perfil, name='perfil'),
    path('exibir_perfil', views.exibir_perfil_do_talento_candidatado, name='exibir_perfil_do_talento_candidatado'),
    path('listar_candidatos/<int:pk_vaga>', views.listar_talentos_candidatados, name='listar_talentos_candidatados'),#dashboard de empresa
    path('talentos', views.talentos, name='talentos'),#empresa ver candidatos
    path('perfil/candidato/<int:id_candidato>', views.perfil_candidato, name='perfil_candidato'),#empresa ver o perfil do candidato
    path('busca_talentos', views.busca_talentos, name='busca_talentos'),#busca candidatos
    path('contato', views.contato, name='contato'),#busca candidatos
]
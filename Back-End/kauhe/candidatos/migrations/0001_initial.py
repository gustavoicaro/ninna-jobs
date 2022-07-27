# Generated by Django 4.0.6 on 2022-07-27 22:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_candidato', models.CharField(max_length=100)),
                ('data_nascimento', models.DateField()),
                ('cpf_do_candidato', models.CharField(max_length=15)),
                ('sexo_candidato', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('empresa_onde_trabalhou', models.CharField(max_length=50)),
                ('cargo_exercido', models.CharField(max_length=50)),
                ('inicio_do_emprego', models.DateField()),
                ('data_da_demissao', models.DateField()),
                ('descricao_de_atividades', models.TextField()),
                ('experiencia', models.CharField(max_length=12)),
                ('status_fundamental', models.CharField(max_length=12)),
                ('status_medio', models.CharField(max_length=12)),
                ('status_tecnico', models.CharField(max_length=12)),
                ('curso_tecnico', models.CharField(max_length=50)),
                ('instituicao_do_curso_tecnico', models.CharField(max_length=50)),
                ('inicio_do_curso_tecnico', models.DateField()),
                ('termino_do_curso_tecnico', models.DateField()),
                ('grau_superior', models.CharField(max_length=12)),
                ('curso_superior', models.CharField(max_length=50)),
                ('instituicao_do_curso_superior', models.CharField(max_length=50)),
                ('inicio_do_curso_superior', models.DateField()),
                ('termino_do_curso_superior', models.DateField()),
                ('idioma', models.CharField(max_length=12)),
                ('nivel_idioma', models.CharField(max_length=13)),
                ('data_atual', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('data_atualizacao', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'tb_candidatos',
            },
        ),
        migrations.CreateModel(
            name='EducacaoFundamental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educacao_fundamental', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tb_EducacaoFundamental',
            },
        ),
        migrations.CreateModel(
            name='EducacaoMedio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educacao_medio', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tb_EducacaoMedio',
            },
        ),
        migrations.CreateModel(
            name='EducacaoSuperior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educacao_superior', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tb_EducacaoSuperior',
            },
        ),
        migrations.CreateModel(
            name='EducacaoTecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educacao_tecnico', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tb_EducacaoTecnico',
            },
        ),
        migrations.CreateModel(
            name='ExpAcademica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiancia_academica', models.CharField(max_length=100)),
                ('descriacao_experiancia_profissional', models.TextField(max_length=100)),
            ],
            options={
                'db_table': 'tb_ExpAcademica',
            },
        ),
        migrations.CreateModel(
            name='NivelIdiomas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.CharField(max_length=23)),
            ],
            options={
                'db_table': 'tb_NivelIdioma',
            },
        ),
        migrations.CreateModel(
            name='NumeroInscritos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_inscritos', models.CharField(max_length=34)),
            ],
            options={
                'db_table': 'tb_NumeroInscritos',
            },
        ),
    ]

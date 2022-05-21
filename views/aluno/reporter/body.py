from reportlab.platypus import Image, Table, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from PySide6.QtCore import QDir
from views.compenentes.linha import MCLine

import controller.ResponsavelController as responsavelController

static_dir = QDir.currentPath() + "/static"

def getBodyPage(row):
    Story = []

    styles = getSampleStyleSheet()

    text_style = ParagraphStyle(name='text_style', fontSize=10, alignment=TA_LEFT, spaceBefore=12, leading=10, leftIndent=45)
    text_style.fontName = 'Times-Roman'
    text_style.spaceBefore = 0
    text_style.spaceAfter = 0
    text_style.firstLineIndent = 0
    styles.add(text_style)

    headstyle = ParagraphStyle(
                    name='titulo',
                    fontName='Helvetica-Bold',
                    fontSize=14,
                    leading=10,
                    alignment=TA_CENTER
                ) 

    Story.append(Spacer(1, 15))
    if row.sexo == 'MASCULINO':
        titulo = '<b>DADOS PESSOAIS DO ALUNO</b>'
    else:
        titulo = '<b>DADOS PESSOAIS DA ALUNA</b>'

    Story.append(Paragraph(titulo, headstyle))
    Story.append(Spacer(1, 15))
    Story.append(MCLine(500))
    Story.append(Spacer(1, 15))
    nome = '<b>Nome do Aluno(a)</b>: {}'.format(row.nome)
    Story.append(Paragraph(nome, styles['text_style']))
    Story.append(Spacer(1, 12))
    cpf = '<b>CPF</b>: {}.{}.{}-{}'.format(row.cpf[:3], row.cpf[3:6], row.cpf[6:9], row.cpf[9:])
    Story.append(Paragraph(cpf, styles['text_style']))
    Story.append(Spacer(1, 12))
    rg = '<b>RG</b>: {}'.format(row.rg)
    Story.append(Paragraph(rg, styles['text_style']))
    Story.append(Spacer(1, 12))
    orgao_exp_rg = '<b>Órgão Expedidor</b>: {}'.format(row.orgao_exp_rg)
    Story.append(Paragraph(orgao_exp_rg, styles['text_style']))
    Story.append(Spacer(1, 12))
    uf_exp_rg = '<b>UF</b>: {}'.format(row.uf_exp_rg)
    Story.append(Paragraph(uf_exp_rg, styles['text_style']))
    Story.append(Spacer(1, 12))
    nascimento = '<b>Data de Nascimento</b>: {}'.format(row.nascimento)
    Story.append(Paragraph(nascimento, styles['text_style']))
    Story.append(Spacer(1, 12))
    sexo = '<b>Sexo</b>: {}'.format(row.sexo)
    Story.append(Paragraph(sexo, styles['text_style']))
    Story.append(Spacer(1, 12))
    pai = '<b>Nome do Pai</b>: {}'.format(buscaPais(row.pai))
    Story.append(Paragraph(pai, styles['text_style']))
    Story.append(Spacer(1, 12))
    mae = '<b>Nome da Mãe</b>: {}'.format(buscaPais(row.mae))
    Story.append(Paragraph(mae, styles['text_style']))
    Story.append(Spacer(1, 12))
    endereco = '<b>Residência</b>: {}'.format(row.endereco)
    Story.append(Paragraph(endereco, styles['text_style']))
    Story.append(Spacer(1, 12))
    bairro = '<b>Bairro</b>: {}'.format(row.bairro)
    Story.append(Paragraph(bairro, styles['text_style']))
    Story.append(Spacer(1, 12))
    cidade = '<b>Cidade</b>: {}'.format(row.cidade)
    Story.append(Paragraph(cidade, styles['text_style']))
    Story.append(Spacer(1, 12))
    uf = '<b>Estado</b>: {}'.format(row.uf)
    Story.append(Paragraph(uf, styles['text_style']))
    Story.append(Spacer(1, 12))

    return Story

def buscaPais(id):
    row = responsavelController.selectById(id)
    return row.nome
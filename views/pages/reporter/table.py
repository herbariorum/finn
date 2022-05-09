import controller.ResponsavelController as responsavelController
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfgen import canvas
from views.pages.compenentes.linha import MCLine
from reportlab.lib.units import inch

def getBodyTable(page, widht, height=0): # página tera 24 linhas

    rows = responsavelController.selectForPage(page, 22) 
    
    headers = ['NOME', 'CPF', 'TIPO RESPONSAVEL', 'PROFISSÃO', 'CONTATO']
    
    monta_tabela = []

    monta_tabela.append(headers)
    for values in rows:
        monta_tabela.append(
        [
            values.nome,
            values.cpf,
            values.tipo_responsavel,
            values.profissao,
            values.contatos  ,  
        ]        
    )  
    # styles = getSampleStyleSheet()
    headstyle = ParagraphStyle(
                    name='titulo',
                    fontName='Helvetica-Bold',
                    fontSize=14,
                    leading=10,
                    alignment=TA_CENTER
                )

    elements = []

    title = u'Listagem de Responsáveis'
    
    elements.append(Paragraph(title, style=headstyle))
    
    linha = MCLine(widht)    
    elements.append(Spacer(1, 12))
    elements.append(linha)
    elements.append(Spacer(1, 12))

    LIST_STYLE = TableStyle(
        [
            ('GRID', (0,0), (-1,-1), 1, colors.grey),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTSIZE', (0, 0), (-1, -1), 8),
            ('TEXTCOLOR', (0,0),(-1,-1), 'black'),
            ('BOTTOMPADDING', (0,0), (-1,-1),0),
        ]
    )
    
    if (len(rows) % 2 == 0):
        pass
    else:
        pass
    t = Table(monta_tabela, colWidths=[200, 65, 100, 150, 55], rowHeights=25, repeatRows=1)

    t.setStyle(LIST_STYLE)

    elements.append(t)
    elements.append(Spacer(1, 1 * inch))

    return elements
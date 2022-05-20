import controller.AlunoController as alunoController
import controller.ResponsavelController as responsavelController
from reportlab.platypus import Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfgen import canvas
from views.compenentes.linha import MCLine
from reportlab.lib.units import inch

def getTablePage(page, widht, height=0): # página tera 24 linhas

    rows = alunoController.selectForPage(page, 22) 
    
    headers = ['NOME', 'CPF', 'SEXO', 'MÃE', 'CIDADE']
    
    monta_tabela = []

    monta_tabela.append(headers)
    for values in rows:
        monta_tabela.append(
        [
            values.nome,
            values.cpf,
            values.sexo,            
            buscaPais(values.mae),
            values.cidade  ,  
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

    title = u'Listagem de Alunos'
    
    elements.append(Paragraph(title, style=headstyle))
    
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
    t = Table(monta_tabela, colWidths=[150, 65, 65, 150, 100], rowHeights=25, repeatRows=1)

    t.setStyle(LIST_STYLE)

    elements.append(t)
    elements.append(Spacer(1, 1 * inch))

    return elements

def buscaPais(id):
    row = responsavelController.selectById(id)
    return row.nome
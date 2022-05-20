from reportlab.platypus import Image, Table, Paragraph


import os

def getHeaderPage(width, height):
    path_atual = os.getcwd() + '/static/img'
    logo = os.path.join(path_atual, 'logotipo.jpeg')
    im = Image(logo, 64, 64)
    p = Paragraph('''
        <b>Escola Comunitária de Augustinópolis</b><br/>
        Rua Antônio De Sousa Gomes, S/N - Setor Popular<br/>
        Augustinópolis - TO<br/>
        77960-000
    ''')

    data = [[im, p]]
    res = Table(data, colWidths=[64, 300 ], rowHeights=height)
    res.setStyle([
        ('LEFTPADDING', (0,0), (0,2), 0), # 0 0 inicio -1 -1 final

        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TEXTCOLOR', (0,0),(-1,-1), 'black'), 
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ])

    return res
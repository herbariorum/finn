from reportlab.platypus import Image, Table
from reportlab.lib.units import mm

import os

def getHeaderTable(width, height):
    path_atual = os.getcwd() + '/static/img'
    logo = os.path.join(path_atual, 'logotipo.jpeg')
    im = Image(logo, 50*mm, 50*mm)
    
    res = Table([[
        im
    ]], width, height)
    res.setStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1),0),
    ])

    return res
from reportlab.platypus import Table
from reportlab.lib import colors

def getFooterPage(width, height):
    text = "Rua Dom Pedro I, sn - Augustinópolis - TO CEP 77960-000"
    color = colors.HexColor('#003363')
    res = Table([[text]], width, height)
    res.setStyle([
        # ('GRID', (0,0), (-1,-1), 1, 'red'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1),0),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'), # X=0, X=0 
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BACKGROUND', (0,0), (-1,-1), color),
        ('TEXTCOLOR', (0,0),(-1,-1), 'white'),
    ])
    return res 
from qt_core import *

import views.login.login as vl
import views.dashboard as d

import sys


def carrega_sistema():
    logou = vl.executa()   
    if logou: 
        d.executa()


carrega_sistema()
sys.exit(0)
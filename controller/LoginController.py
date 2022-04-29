from database.LoginDataset import LoginDataSet
from entities.User import User
from libs.seguranca import validarPassword

def validar_usuario(usuario, password):
    localizaEmail = LoginDataSet.selectByEmail(User, usuario)
   
    if not localizaEmail:
        return False

    seguranca = validarPassword(password, localizaEmail.password)
    if seguranca:
        return True
    return False
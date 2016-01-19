# -*- coding: utf-8 -*-
"""
Autores: XXX
Grupo YYY

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no 
haber colaborado de ninguna manera con otros grupos, haber compartido el ćodigo 
con otros ni haberlo obtenido de una fuente externa.
"""

from bottle import run, post
# Resto de importaciones
from pymongo import MongoClient
import random
import string

##############
# APARTADO A #
##############
client = MongoClient()
db = client['giw']

@post('/signup')
def signup():
    pass
    

@post('/change_password')
def change_password(nickname, old_password, new_password):
	message = ""
	found_user = db.users.find_one({"nickname":nickname})
	if (!found_user):
		message = "Usuario o contraseña incorrectos"
	else if (found_user['password'] == old_password):
		message = "Usuario o contraseña incorrectos"
	else:
		result = db.users.update_one({"nickname":nickname}, {"$set":{"password":new_password}})
		message = "La contraseña del usuario %s ha sido modificada!" % (nickname)
	return template("password_change", message = message);
            

@post('/login')
def login(nickname, password):
	message = ""
	found_user = db.users.find_one({"nickname":nickname})
	if (!found_user):
		message = "Usuario o contraseña incorrectos"
	else if(found_user['password']== password):
		message = "Usuario o contraseña incorrectos"
	else:
		message = "Bienvenido %s" %(nickname)
	return template ("login", message = message)


##############
# APARTADO B #
##############


def gen_secret():
    # Genera una cadena aleatoria de 16 caracteres a escoger entre las 26 
    # letras mayúsculas del inglés y los dígitos 2, 3, 4, 5, 6 y 7. 
    #
    # Ejemplo:
    # >>> gen_secret()
    # '7ZVVBSKR22ATNU26'
	secret = random_char(16)
    return secret;
    
    
def gen_gauth_url(app_name, username, secret):
    # Genera la URL para insertar una cuenta en Google Authenticator
    #
    # Ejemplo:
    # >>> gen_gauth_url( 'GIW_grupoX', 'pepe_lopez', 'JBSWY3DPEHPK3PXP')
    # 'otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX
    #    
    # Formato de la URL:
    # otpauth://totp/<ETIQUETA>?secret=<SECRETO>&issuer=<NOMBRE_APLICACION_WEB>
    #
    # Más información en: 
    #   https://github.com/google/google-authenticator/wiki/Key-Uri-Format
    pass
        

def gen_qrcode_url(gauth_url):
    # Genera la URL para generar el código QR que representa 'gauth_url'
    # Información de la API: http://goqr.me/api/doc/create-qr-code/
    #
    # Ejemplo:
    # >>> gen_qrcode_url('otpauth://totp/pepe_lopez?secret=JBSWY3DPEHPK3PXP&issuer=GIW_grupoX')
    # 'http://api.qrserver.com/v1/create-qr-code/?data=otpauth%3A%2F%2Ftotp%2Fpepe_lopez%3Fsecret%3DJBSWY3DPEHPK3PXP%26issuer%3DGIW_grupoX'
    pass
    


@post('/signup_totp')
def signup_totp():
    pass
        
        
@post('/login_totp')        
def login_totp():
    pass

    
if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)

###############################################################################
################# Funciones auxiliares a partir de este punto #################
###############################################################################

def random_char(n):
	chars = string.ascii_uppercase + "1234567890"
	return ''.join(random.choice(chars) for x in range(n))
	
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import run, get, template,request
import string
import random
import json
import urllib2
import urllib 

# Credenciales. 
# https://developers.google.com/identity/protocols/OpenIDConnect#appsetup
# Copiar los valores adecuados.
config = {
    'client_id': '700570345546-cgc40e1j5rqgjj1asm08vjgap7sl5c5n.apps.googleusercontent.com',
    'client_secret': 'UJ1SiIYSi2pgcbrXAOQOgqL6',
    'response_type' : 'code',
    'redirect_uri' : 'http://localhost:8080/token',
    'scope' : 'email',
    'state' : 'XXX',
    'discovery_doc': 'https://accounts.google.com/.well-known/openid-configuration'
}

# Fichero de descubrimiento para obtener el 'authorization endpoint' y el 
# 'token endpoint'
# https://developers.google.com/identity/protocols/OpenIDConnect#authenticatingtheuser
DISCOVERY_DOC = "https://accounts.google.com/.well-known/openid-configuration"

# Token validation endpoint para decodificar JWT
# https://developers.google.com/identity/protocols/OpenIDConnect#validatinganidtoken
TOKEN_VALIDATION_ENDPOINT = "https://www.googleapis.com/oauth2/v3/tokeninfo"

def gen_secret():
    # Genera una cadena aleatoria de 16 caracteres a escoger entre las 26 
    # letras mayúsculas del inglés y los dígitos 2, 3, 4, 5, 6 y 7. 
    #
    # Ejemplo:
    # >>> gen_secret()
    # '7ZVVBSKR22ATNU26'
    length = 30
    chars = string.ascii_uppercase + "234567"
    return ''.join(random.choice(chars) for x in range(length))

config['state'] = gen_secret();

@get('/login_google')
def login_google():
    global config
 
    url = "https://accounts.google.com/o/oauth2/v2/auth?"
    url += "client_id="      + config['client_id']
    url += "&response_type=" + config['response_type']
    url += "&redirect_uri="  + config['redirect_uri']
    url += "&scope="         + config['scope']
    url += "&state="         + config['state']

    return template('home', googleURL=url);

def getTokenEndPoint():
    global config
    data = json.load(urllib2.urlopen(config['discovery_doc']))
    return data['token_endpoint']

def getEncryptedToken(token_endpoint, userCode):
    global config 
    values = {
        'code' : userCode,
        'client_id' : config['client_id'],
        'client_secret' : config['client_secret'],
        'redirect_uri' : config['redirect_uri'],
        'grant_type' : 'authorization_code',
    }

    data = urllib.urlencode(values)
    req = urllib2.Request(token_endpoint, data)
    response = urllib2.urlopen(req)
    return response.read()

@get('/token')
def token():
    global config 

    state    = str(request.GET.get('state'))
    userCode = str(request.GET.get('code'))

    # Confirm that the state received from Google matches 
    # the session token we created

    if state == config['state']:

        token_endpoint = getTokenEndPoint(); 
        token = getEncryptedToken(token_endpoint, userCode)

        print token

if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)

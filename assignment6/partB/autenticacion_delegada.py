from bottle import run, get

# Credenciales. 
# https://developers.google.com/identity/protocols/OpenIDConnect#appsetup
# Copiar los valores adecuados.
CLIENT_ID     = XXXXX
CLIENT_SECRET = YYYYY
REDIRECT_URI  = "http://localhost:8080/token"

# Fichero de descubrimiento para obtener el 'authorization endpoint' y el 
# 'token endpoint'
# https://developers.google.com/identity/protocols/OpenIDConnect#authenticatingtheuser
DISCOVERY_DOC = "https://accounts.google.com/.well-known/openid-configuration"


# Token validation endpoint para decodificar JWT
# https://developers.google.com/identity/protocols/OpenIDConnect#validatinganidtoken
TOKEN_VALIDATION_ENDPOINT = "https://www.googleapis.com/oauth2/v3/tokeninfo"




@get('/login_google')
def login_google():
    pass


@get('/token')
def token():
    pass


if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)

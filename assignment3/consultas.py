# -*- coding: utf-8 -*-
"""
Autores: XXX
Grupo YYY

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no haber
colaborado de ninguna manera con otros grupos, haber compartido el ćodigo con
otros ni haberlo obtenido de una fuente externa.
"""

"""
	IMPLICIT SCHEME

	+---------------------------------------------------+
	| key             | types  | occurrences | percents |
	| --------------- | ------ | ----------- | -------- |
	| _id             | String |        1000 |    100.0 |
	| address         | Object |        1000 |    100.0 |
	| address.country | String |        1000 |    100.0 |
	| address.zip     | Number |        1000 |    100.0 |
	| email           | String |        1000 |    100.0 |
	| gender          | String |        1000 |    100.0 |
	| likes           | Array  |        1000 |    100.0 |
	| password        | String |        1000 |    100.0 |
	| year            | Number |        1000 |    100.0 |
	+---------------------------------------------------+

"""

from bottle import get, run, request
# Resto de importaciones


@get('/find_user_id')
def find_user_id():
    # http://localhost:8080/find_user_id?_id=user_1
    pass


# http://localhost:8080/find_users?gender=Male
# http://localhost:8080/find_users?gender=Male&year=2009

@get('/find_users')
def find_users():
    
    params 		= dict((k,request.query.getall(k)) for k in request.query.keys())
    validParams = {'_id', 'email', 'gender', 'year'}

    print validParams
    #if not checkParameters(params, len(params), validParams):
    #	return "Error........"
    #else:
    #	return "Valid"

    # Bad? Return...

    # Antes de la tabla aparecera un mensaje indicando el número de resultados encontrados.
    # Get user with that shit of parameters.

    print params['gender']

# http://localhost:8080/find_users_or?gender=Male&year=2000

@get('/find_users_or')
def find_users_or():
    
    # http://stackoverflow.com/questions/12064764/pymongo-query-on-list-field-and-or
    # https://docs.mongodb.org/manual/reference/operator/query/
    pass

       
@get('/find_like')
def find_like():
    # http://localhost:8080/find_like?like=football
    pass


@get('/find_country')
def find_country():
    # http://localhost:8080/find_country?country=Spain
    pass


@get('/find_email_year')
def email_year():
    # http://localhost:8080/find_email_year?year=1992
    pass


@get('/find_country_limit_sorted')
def find_country_limit_sorted():
    # http://localhost:8080/find_country_limit_sorted?country=Spain&limit=20&ord=asc
    pass


###############################################################################
################# Funciones auxiliares a partir de este punto #################
###############################################################################

def checkParameters(params, maxParams, validParams):
	if len(params) > maxParams:
		return (False,'More than valid parameters')

	print params
	for p in params:
		print p
		if p in validParams:
			continue
		else:
			return (False,'Key with multiple values');

	return True
	#if type(params) is Dict and type(validParams) is List
	#else:
	#	return False;
	# Check length (more than 4 are wrong) ---> show error
	# Check parameters name
	# 		How do we check parameters name?
			# if key in Dictionar - _id, email, gender y year



###############################################################################
###############################################################################

if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)

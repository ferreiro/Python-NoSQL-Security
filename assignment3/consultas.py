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

from bottle import get, run, request, template

# Resto de importaciones
import pymongo
from pymongo import MongoClient # install MongoClient
from pymongo import ReturnDocument

client 	= MongoClient()
db 		= client['giw']

@get('/find_user_id')
def find_user_id():
	# http://localhost:8080/find_user_id?_id=user_1
   
	maxParams   = 1 
	params      = dict((k,request.query.getall(k)) for k in request.query.keys())
	validParams = ['_id']

	(isValid, msg) = checkParameters(params, maxParams, validParams)

	if isValid:
		userID=params['_id'][0]
		cursor = db.users.find({'_id' : userID});
		if (cursor.count() == 0):
			msg = "No user with that ID"
			return template('error', msg=msg)
			#return template('error', msg=message)
		else:
			userList = []
			for c in cursor:
				userList.append(c)
	
			return str(userList)
			#return template('table', content=userList)
	else:
		return template('error', msg=msg)


# http://localhost:8080/find_users?gender=Male
# http://localhost:8080/find_users?gender=Male&year=2009

@get('/find_users')
def find_users():
	
	maxParams 	= 4
	params 		= dict((k,request.query.getall(k)) for k in request.query.keys())
	validParams = ['_id', 'email', 'gender', 'year']

	(isValid, msg) = checkParameters(params, maxParams, validParams)
	
	if isValid:
		_id =""
		email =""
		gender =""
		year =-1

		for p in params:
			if p == '_id':
				_id = params['_id'][0]
			elif p == 'email':
				email = params['email'][0]
			elif p == 'gender':
				gender = params['gender'][0]
			elif p == 'year':
				year = params['year'][0]

		cursor = db.users.find({"$or":[ 
			{"_id":_id},
			{"email":email},
			{"gender":gender},
			{"year":int(year)}
		]})

		if (cursor.count() == 0):
			return template('error', msg="Nothing found with your criteria")
		else:
			userList = []
			for c in cursor:
				userList.append(c)
		
			return template('table', userList=userList)
	else:
		return template('error', msg=msg)

	# Antes de la tabla aparecera un mensaje indicando el número de resultados encontrados.
	# Get user with that shit of parameters.

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

''' 
	Returns a tuple where first index is a boolean value (Valid or False) 
	and the second parameter is an string with the error or success message
	
	Accepted parameters:
	1. Params: Dictionary where key is the name of param and value is an array of elements for this parameter
	2. MaxParams: Integer of maximun different keys (parameters name) it accepts.
	3. ValidParams: Dictionary of valid parameters accepted: validParams = { 'name', 'surname' }
'''		
def checkParameters(params, maxParams, validParams):
	
	# Error type checking | source: http://stackoverflow.com/questions/2225038/determine-the-type-of-an-object
	if type(params) is not dict:
		return (False, 'Parameters are not dictionary type');
	elif type(maxParams) is not int:
		return (False, 'Maxium Parameters is not Integer Type');
	elif type(validParams) is not list:
		return (False, 'Valid Parameters are not List Type');

	# Now checks if the passed number of parameters are accepted.
	if len(params) > maxParams:
		return (False,'We don\'t accept more than ' + str(maxParams) + ' params passed by url')

	for key in params:
		
		totalParams = len(params[key]) # params associated with that key
		#print totalParams

		if totalParams > 1:
			errMsg = str(key) + " has " + str(totalParams) + " different values passing by params"; 
			return (False, errMsg)
		elif not key in validParams:
			errMsg = str(key) + " param is not valid" 
			return (False, errMsg);
		else:
			continue # The key params is valid

	return (True, 'Params are correct')

###############################################################################
###############################################################################

if __name__ == "__main__":
	run(host='localhost',port=8080,debug=True)

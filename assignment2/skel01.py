# -*- coding: utf-8 -*-
"""
Autores: XXX
Grupo YYY

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no haber
colaborado de ninguna manera con otros grupos, haber compartido el ćodigo con
otros ni haberlo obtenido de una fuente externa.
"""

dbName = 'giw';

from bottle import post, request, route, run, template
from pymongo import MongoClient # install MongoClient

client = MongoClient()
db = client['giw']
users = db['users']

#print result[0]
#print result[0]['email']

# ¡MUY IMPORTANTE!
# Todas las inserciones se deben realizar en la colección 'users' dentro de la
# base de datos 'giw'.

@route('/')
def createNewUser():
	return template('add_user');

@post('/add_user')
def add_user_post():

	user_id = str(request.forms.get('_id'));

	cursor = db.users.find({
		'_id': str(user_id),
		{
			upsert: true
		}
	});

	if (cursor.count() == 0):
		# Insert new user on database.
		db.users.insert({
			'_id' : user_id,
			'country': str(request.forms.get('country')),
			'zip': str(request.forms.get('zip')),
			'email': str(request.forms.get('email')),
			'gender': str(request.forms.get('gender')),
			'likes': str(request.forms.get('likes')).split(','), # Create array of strings.
			'password': str(request.forms.get('password')), 
			'year': str(request.forms.get('year')),
		})
	else:
		# Si el usuario ya existe en la colección el servidor web mostrará un mensaje indicándolo. 
		return "Your user exists on our database";
	
	# En otro caso mostrará un mensaje indicando que la inserción ha tenido éxito.
	return "The user was created :-)"
	


@post('/change_email')
def change_email():
	user_id = request.forms.get('_id');
	email = request.forms.get('email');

    

@post('/insert_or_update')
def insert_or_update():
    pass


@post('/delete')
def delete_id():
    pass
    
    
@post('/delete_year')
def delete_year():
    pass

run(host='127.0.0.1', port=3000);


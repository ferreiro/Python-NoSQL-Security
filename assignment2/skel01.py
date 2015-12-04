# -*- coding: utf-8 -*-
"""
Autores: Jorge García Ferreiro, Tomasso Innoccenti and Luis
Grupo 12

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no haber
colaborado de ninguna manera con otros grupos, haber compartido el ćodigo con
otros ni haberlo obtenido de una fuente externa.
"""

dbName = 'giw';

from bottle import post, get, request, route, run, template, static_file
import pymongo
from pymongo import MongoClient # install MongoClient
from pymongo import ReturnDocument
import json

client 	= MongoClient()
db 		= client['giw']
users 	= db['users']

#####################################
########## ASSETS ROUTING ###########
#####################################

@route('/views/<filepath:path>')
def file_stac(filepath):
    return static_file(filepath, root="./views")

@route('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/')

@route('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/')

@route('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/')

@route('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/')

# ¡MUY IMPORTANTE!
# Todas las inserciones se deben realizar en la colección 'users' dentro de la
# base de datos 'giw'.

####################################
########### GET METHODS ############
####################################

@get('/')
def index():
	return template('index');

@get('/change_email')
def change_email_view():
	return template('change_email');

@get('/insert')
def insert__view():
	return template('insert');

@get('/insert_or_update')
def insert_or_update_view():
	return template('insert_or_update');

@get('/delete')
def delete_view():
	return template('delete');

# Display user profile.
@get('/delete_year')
def delete_by_year_view():
	return template('delete_year');

# Display user profile.
@get('/<userID>')
def display_user_byID_view(userID):
	cursor = db.users.find({
		'_id' : userID
	});

	if (cursor.count() > 0): 
		user = cursor[0]
		return template('profile', user=user);
	
	return template('result', message="User doesn't exist...");
	
@get('/<userID>/edit')
def edit_user_byID_view(userID):
	
	cursor = db.users.find({
		'_id' : userID
	});

	if (cursor.count() == 0):
		print "No user with that ID"
		return "No user with that ID"
	else:
		user = cursor[0] # python dictionary from a user
		return template('change_email_profile', user=user);

#####################################
########### POST METHODS ############
#####################################

''' 
	Insert a new user into our database
	Only if user doesn't exist on our system.
	When success, print a message and show
	a success view.
'''

@post('/add_user')
def add_user_post():
	
	message = {
		"success" : "[ Good ] The user was created :-)",
		"error" : "[ Error ] Your user exists on our database"
	}

	try:
		userID = str(request.forms.get('_id'));
		users.insert({
			'_id' : str(request.forms.get('_id')),
			'country': str(request.forms.get('country')),
			'zip': str(request.forms.get('zip')),
			'email': str(request.forms.get('email')),
			'gender': str(request.forms.get('gender')),
			'likes': str(request.forms.get('likes')).split(','), # Create array of strings.
			'password': str(request.forms.get('password')), 
			'year': str(request.forms.get('year'))
		});

	except pymongo.errors.DuplicateKeyError, e:
		if (pymongo.errors.DuplicateKeyError):
			print  "\n" + str(message['error']) + "\n" # display on console success
		return template('result', message=message['error'])

	print  "\n" + str(message['success']) + "\n" # display on console success
	return template('result', message=message['success'])

'''
	Change email of a user that already exists in the collection.
	Como resultado de esta petición el servidor web debe mostrar el número de documentos modificados.
'''
@post('/change_email')
def change_email():

	_id 	= str(request.forms.get('_id'))
	email 	= str(request.forms.get('email'))

	updatedUser = None;

	try:
		updatedUser = users.find_one_and_update(
			{'_id':_id},
			{'$set' : {'email':email}},
			return_document=ReturnDocument.AFTER
		);

	except ValueError:
		print "Email coudln't change"
	
	if (updatedUser != None):
		print "\n1 documents modified\n"
		return template('profile', user=updatedUser);

	print "\n0 documents modified\n"
	return template('result', message="[ BAD ] Your user NOT exist on our database")

@post('/insert_or_update')
def insert_or_update():
    
    message = "Error inserting user"

    try:
    	userID = str(request.forms.get('_id'));

    	#find_one_and_update(filter, update, projection=None, sort=None, return_document=ReturnDocument.BEFORE, **kwargs)
    	doc = users.find_one_and_update(
    		{
    			'_id' :userID
    		},
    		{
    			'$set' : {
	    			'country': str(request.forms.get('country')),
		    		'zip': str(request.forms.get('zip')),
		    		'email': str(request.forms.get('email')),
		    		'gender': str(request.forms.get('gender')),
		    		'likes': str(request.forms.get('likes')).split(','), # Create array of strings.
		    		'password': str(request.forms.get('password')), 
		    		'year': str(request.forms.get('year'))
    			}
    		},
    		upsert=True,
    		return_document=ReturnDocument.BEFORE);

    	if doc == None:
    		message="\nThe user wasn't on our system. Inserting!\n"
    	else:
    		message="\nThe user was on the system. Modifying it!\n"
    		
    except ValueError:
    	message = ValueError;

    print message
    return template('result', message=message)

@post('/delete')
def delete_id():

	_id = str(request.forms.get('_id'));

	deleted = users.find_one_and_delete({'_id': _id});
	
	if deleted != None:
		return template('result', message="User deleted successfully!");
	
	return template('result', message="User doesn't exist!");

@post('/delete_year')
def delete_year():

	numDeleted = 0
	year = request.forms.get('year')
	cursor = users.find({'year':year})

	print year
	print cursor.count()

	for s in cursor:
		_id = s['_id'] 
		deleted = users.find_one_and_delete({'_id': _id});
		if deleted != None:
			numDeleted += 1

	msg = "deleted " + str(numDeleted) + " documents"
	print msg

	return template('result',message=msg)


@route('/*')
def error():
	return "Not found"

run(host='127.0.0.1', port=3000);


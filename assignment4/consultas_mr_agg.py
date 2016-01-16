# -*- coding: utf-8 -*-
"""
Autores: Jorge Ferreiro, Tommaso Innocenti & Luis
Grupo 12

Este código es fruto ÚNICAMENTE del trabajo de sus miembros. Declaramos no haber
colaborado de ninguna manera con otros grupos, haber compartido el ćodigo con
otros ni haberlo obtenido de una fuente externa.
"""

"""
	Implicit Schema
	+------------------------------------------------------+
	| key                | types  | occurrences | percents |
	| ------------------ | ------ | ----------- | -------- |
	| _id                | String |           1 |    100.0 |
	| country            | String |           1 |    100.0 |
	| gender             | String |           1 |    100.0 |
	| orders             | Array  |           1 |    100.0 |
	| orders.XX.item     | String |           1 |    100.0 |
	| orders.XX.quantity | Number |           1 |    100.0 |
	| orders.XX.total    | Number |           1 |    100.0 |
	+------------------------------------------------------+

	orders has an array, where each order has (item, quantity and total)
"""

# Importaciones
import pymongo
import math

from bson.son import SON
from bson.code import Code
from bottle import get, run, request, template
from pymongo import MongoClient # install MongoClient
from pymongo import ReturnDocument

client 	= MongoClient()
db 		= client['giw']

# MapReduce: usuarios en cada pais.
@get('/users_by_country_mr')
def users_by_country_mr():

	mapper = Code("""
			function countryMap() {
				emit(this.country, { count: 1 });
			}
			""")

	reducer = Code("""
			function countryReduce(key, values) {
				var total = 0;

				for (var i = 0; i < values.length; i++) {
					total += values[i].count;
				}

				return { count: Math.round(total) }
			}
			""")

	results = db.users.inline_map_reduce(mapper, reducer)
	return template('table_map_reduce', results=results, count=len(results));

# Aggregation Pipeline: usuarios en cada pais (orden descendente por numero
# de usuarios).
@get('/users_by_country_agg')
def users_by_country_agg():
	
	pipeline = [
		{"$group": {"_id": "$country", "count": {"$sum": 1}}},
		{"$sort": SON([("count", -1), ("_id", -1)])}
	]
	results= list(db.users.aggregate(pipeline))
	return template('table_pipeline', results=results, count=len(results));

# MapReduce: gasto total en cada pais.
@get('/spending_by_country_mr')
def spending_by_country_mr():

	mapper = Code("""
			function countryMap() 
			{
				var total = 0;
				var orders = this.orders;

				if (orders) {
					for (i=0; i < orders.length; i++) {
						total += orders[i].total
					}
				}

				emit(this.country, { count: total });
			}
			""")

	reducer = Code("""
			function countryReduce(key, values) {
				var total = 0;

				for (var i = 0; i < values.length; i++) {
					total += values[i].count;
				}

				return { count: total }
			}
			""")

	results = db.users.inline_map_reduce(mapper, reducer)
	return template('table_map_reduce', results=results, count=len(results));


# Aggregation Pipeline: gasto total en cada pais (orden descendente por nombre
# del pais).
@get('/spending_by_country_agg')
def spending_by_country_agg():
	
	pipeline = [
		{"$unwind": "$orders" },
		{"$group": {"_id": "$country", "count": {"$sum": "$orders.total" }}},
		{"$sort": SON([("count", 1), ("_id", -1)])}
	]
	results= list(db.users.aggregate(pipeline))
	return template('table_pipeline', results=results, count=len(results));



# MapReduce: gasto total realizado por las mujeres que han realizdo EXACTAMENTE
# 3 compras.
@get('/spending_female_3_orders_mr')
def spending_female_3_orders_mr():
	mapper = Code("""
			function spendingMap()
			{
				var total = 0;
				var orders = this.orders;

				if (orders) {
					for (i=0; i < orders.length; i++) {
						total += orders[i].total
					}
				}

				emit("Total", { count: total });
			}
			""")
	reducer = Code("""
			function spendingReduce(key, values) {
				var total = 0;
				for (var i = 0; i < values.length; i++) {
					total += values[i].count;
				}
				return { count: total }
			}
			""")
	results = db.users.inline_map_reduce(mapper, reducer, query={"orders":{"$size":3}, "gender":"Female"})
	return template('table_map_reduce', results=results, count=len(results));


# Aggregation Pipeline: gasto total realizado por las mujeres que han realizdo 
# EXACTAMENTE 3 compras.
@get('/spending_female_3_orders_agg')
def spending_female_3_orders_agg():
	pass

	
###############################################################################
###############################################################################

if __name__ == "__main__":
	run(host='localhost',port=8080,debug=True)
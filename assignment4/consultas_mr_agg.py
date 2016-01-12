# -*- coding: utf-8 -*-
"""
Autores: Jorge Ferreiro, Tommaso Innocenti & Luis
Grupo YYY

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
from bottle import get, run


# MapReduce: usuarios en cada pais.
@get('/users_by_country_mr')
def users_by_country_mr():
    pass


# Aggregation Pipeline: usuarios en cada pais (orden descendente por numero
# de usuarios).
@get('/users_by_country_agg')
def users_by_country_agg():
    pass
    
    
# MapReduce: gasto total en cada pais.
@get('/spending_by_country_mr')
def spending_by_country_mr():
    pass


# Aggregation Pipeline: gasto total en cada pais (orden descendente por nombre
# del pais).
@get('/spending_by_country_agg')
def spending_by_country_agg():
    pass


# MapReduce: gasto total realizado por las mujeres que han realizdo EXACTAMENTE
# 3 compras.
@get('/spending_female_3_orders_mr')
def spending_female_3_orders_mr():
    pass


# Aggregation Pipeline: gasto total realizado por las mujeres que han realizdo 
# EXACTAMENTE 3 compras.
@get('/spending_female_3_orders_agg')
def spending_female_3_orders_agg():
    pass
    
    
###############################################################################
###############################################################################

if __name__ == "__main__":
    run(host='localhost',port=8080,debug=True)

#!/usr/bin/env python
users = [
	{ 'admin': True, 'active': True, 'name': 'Alice' },
	{ 'admin': True, 'active': False, 'name': 'Bob' },
	{ 'admin': False, 'active': True, 'name': 'Cathy'},
	{ 'admin': False, 'active': False, 'name': 'Dan' },
	{ 'admin': False, 'active': False, 'name': 'Elsa' },
]

line = 1
for user in users:
	if user['admin'] and user['active']:
		print("%s Active - (Admin) %s" % (line, user['name']))
	elif user['admin']:
		print("%s (Admin) %s" % (line, user['name']))
	elif user['active']:
		print("%s Active - %s" % (line, user['name']))
	else:
		print("%s %s" % (line, user['name']))
	line += 1
# A script that uses a dict variable called user 

#!/usr/bin/env python
user = { 'admin': True, 'active': True, 'name': 'Neo' }

if user['admin'] and user['active']:
	print("ACTIVE - (ADMIN) %s" % user['name'])
elif user['admin']:
	print("(ADMIN) %s" % user['name'])
elif user['active']:
	print("ACTIVE - %s" % user['name'])
else:
	print(user['name'])
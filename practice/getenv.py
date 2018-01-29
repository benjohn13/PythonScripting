#!/usr/bin/python

import os

# Input is looking for a string value descibing what enviroment we are in. If none
# is provided, the "or" operation provides "development" as a default assumption

stage = (os.getenv("STAGE") or "development").upper()

output = "We're running in %s" % stage

if stage.startswith("PROD"):
	output = "DANGER! - " + output

print(output)

# Once you've made this an executable in your /bin directory, try it out in the terminal 
# "STAGE=production default_env"
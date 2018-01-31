# Creating a script for exit statuses called "pexit"

#!/bin/python

import sys

print("Something")

sys.exit(0)

print("After exit")

# ~ $
# ~ $ chmod u+x pexit 
# ~ $ ./pexit
# Something
# ~ $ 
# ~ $ echo $?
# 0 
# ~ $


# This script can be useful when looking to automate based on exit statuses

#!/bin/python

import sys

print("Something")

sys.exit(1)

print("After exit")

# ~ $
# ~ $ ./pexit
# Something
# ~ $ 
# ~ $ echo $?
# 1 
# ~ $
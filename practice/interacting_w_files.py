# Creating scripts that interact with other files. This particular one
# reads and prints out the contents of a text file called employees.

#!/bin/python

employees_file = open('employees.txt')

print(employees_file.read())

# You could use this for loop to add spacing between each printed line
# for line in employees_file:
#       print(line)
employees_file.close()


# This script will put us into read and write mode and we're going to add names

#!/bin/python

import os

employees_file = open('employees.txt', 'r+')

# Making sure we go to the end of the file and not writing over it
employees_file.seek(-1, os.SEEK_END)

# Adding a new line before adding a new name
employees_file.write("\nHarold\n")
employees_file.write("Illium\n")

employees_file.close()


# However the code could be improved by using the append mode for adding 
# names like this. We can make use of a list within the write function and 
# save ourselves from repeating the same code over and over. 

#!/bin/python

employees_file = open('employees.txt', 'a')

employees_file.writelines(['Jack\n', 'Karen\n'])

employees_file.close()


# And you could make the code more efficient by creating a block here using
# the 'with' statement and remove the file.close() function.

#!/bin/python

with open('employees.txt', 'a') as employees_file:
	employees_file.write('Leonardo\n')


# https://docs.python.org/3/library/functions.html#open
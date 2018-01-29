#!/bin/python

#Using raw_input() for name and birthdate, while using int() for age 

name = raw_input("Hello, what is your name? ")
birthdate = raw_input("What is your birthdate? ")
age = int(input("How old are you? " ))

print("Nice to meet you, %s! You were born on %s." % (name, birthdate))
print("%s is half your age." % (age / 2))


# https://docs.python.org/2/library/functions.html
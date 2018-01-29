# As a sysadmin, you will encounter dictionaries. While Lists in Python
# contain its data inside brackets, Dictionaries contain keys and values
# inside curly braces as shown below. 

# Creating a unordered dictionary called ages
>>> ages = dict(Alice=54, Bob=61, Cathy=38, Dan=29)
>>> ages
{'Cathy': 38, 'Dan': 29, 'Bob': 61, 'Alice': 54}
>>> 

# Using the key, you can call its value
>>> ages['Alice']
54
>>> ages['Bob']
61
>>>

# Let's say we want to add someone to the dictionary
# Using the assignment operator to add Elsa
>>> ages['Elsa'] = 21
>>> ages
{'Cathy': 38, 'Elsa': 21, 'Bob': 61, 'Dan': 29, 'Alice': 54}
>>>

# We can also use the assignment operator to make a change 
>>> ages['Bob'] = 91
>>> ages
{'Cathy': 38, 'Elsa': 21, 'Bob': 91, 'Dan': 29, 'Alice': 54}
>>> 

# Now let's delete some data (careful not to delete the whole dictionary)
>>> del ages['Alice']
>>> ages
{'Cathy': 38, 'Elsa': 21, 'Bob': 91, 'Dan': 29}
>>> 

# You could also use the pop method and be sparing with the del option
>>> ages.pop('Bob')
91
>>> ages
{'Cathy': 38, 'Elsa': 21, 'Dan': 29}
>>>

# What if we wanted to extract a list of values from the dictionary?
>>> ages.values()
[38, 29, 21]
>>> 

# Or extract the keys into a list?
>>> ages.keys()
['Cathy', 'Dan', 'Elsa']
>>> 

# Or make a list of items?
>>> ages.items()
[('Cathy', 38), ('Dan', 29), ('Elsa', 21)]
>>> 

# Finally, here is one way to make a dictionary with a key value pair
# that uses strings instead of numbers
>>> fav_color = dict({('Alice', 'Green'), ('Bob', 'Blue'), ('Cathy', 'Yellow')})
>>> fav_color
{'Cathy': 'Yellow', 'Bob': 'Blue', 'Alice': 'Green'}
>>> 

# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

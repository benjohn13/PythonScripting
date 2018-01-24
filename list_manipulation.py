# You will encounter all kinds of data sets as a sysadmin. Lists are common
# and the ability to manipulate them will enable you to make sense of raw 
# data. Here are a couple of examples of list manipulation.

# Create a list variable
>>> my_list = [1, 2, 'c', 'd', 5.0]
>>> print(my_list)
[1, 2, 'c', 'd', 5.0]
>>>

# Want to know its length?
>>> len(my_list)
5
>>>

# How about display what is in the first index of the list
>>> my_list[0]
1
>>>

# The colon can be used in different ways. Here it will display 
# everything from start to finish
>>> my_list[:]
[1, 2, 'c', 'd', 5.0]
>>>

# Now display what is in the first index to the third 
>>> my_list[0:3]
[1, 2, 'c']
>>>

# Skip the first two indexes and show me everything else
>>> my_list[2:]
['c', 'd', 5.0]
>>>

# Display the first index and then jump two down the list
>>> my_list[::2]
[1, 'c', 5.0]
>>>

# Let's add something to the end of the list
>>> my_list.append(False)
>>>my_list
[1, 2, 'c', 'd', 5.0, False]
>>>

# The append method will only take one argument. So if you need to 
# add multiple items to the end of the list, you can use this operator
>>> my_list += [7, 8]
>>> my_list
[1, 2, 'c', 'd', 5.0, False, 7, 8]
>>>

# What if you wanted to remove items from your list and replace them 
# with something else?
>>> my_list [0:1] = ['a', 'b']
>>> my_list
['a', 'b', 'c', 'd', 5.0, False, 7, 8]
>>> 

# You could also call out the item you want to remove
>>> my_list.remove(False)
>>> my_list
['a', 'b', 'c', 'd', 5.0, 7, 8]
>>> 

# And you could change the size of the list when replacing data
>>> my_list [4:6] = ['e', 'f']
>>> my_list
['a', 'b', 'c', 'd', 'e', 'f']
>>> 

# You can also use the pop method to remove an item from a 
# list and return it. If no index is specified, pop removes 
# and returns the last item in the list
>>> my_list.pop()
'f'
>>> my_list
['a', 'b', 'c', 'd', 'e']
>>> 


# https://docs.python.org/2/tutorial/datastructures.html

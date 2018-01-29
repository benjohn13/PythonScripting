# Control Flow. Let's say we create a program for creating new 
# passwords and it tells the user something about it.

# Using if, elif and else statements
>>> password = 'pass1234'
>>>
>>> if len(password) >= 15:
...     print('Strong password!')
... elif len(password) == 14:
...     print('Your password length is average.')
... else:
...     print('That password is too weak.')
... 
That password is too weak.
>>> 

# Writing a while loop; you could use this for counting something
>>> banana = 0
>>> while banana < 10:
...     print('Add a banana')
...     banana += 1
... 
Add a banana
Add a banana
Add a banana
Add a banana
Add a banana
Add a banana
Add a banana
Add a banana
Add a banana
Add a banana
>>> 

# Here is a while loop for counting odd numbers
>>> count = 0
>>> while count < 10:
...     if count % 2 == 0:
...         count += 1  
...         continue
...     print("We are counting odd numbers %s" % count)
...     count += 1
We are counting odd numbers 1
We are counting odd numbers 3
We are counting odd numbers 5
We are counting odd numbers 7
We are counting odd numbers 9
>>> 

# Example of using a not statement
if not len("something") > 10:
...    print("It is not")
...
It is not

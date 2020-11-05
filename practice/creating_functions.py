# Creating a script that prompts the user for something to echo 
# it back. This is practice for creating functions.

#!/usr/bin/env python

def multi_echo(message, count):
    while count > 0:
        print(message)
        count -= 1

message = raw_input("Enter a message: ")
count = raw_input("Number of repeats [1]: ").strip()

if count:
    count = int(count)
else:
    count = 1

multi_echo(message, count)

# bin $ 
# bin $ sudo chmod u+x echo_mess 
# bin $ sudo echo_mess 
# Please enter a message: BlahBlah   
# Number of repeats [1]: 
# BlahBlah
# bin $ sudo echo_mess 
# Please enter a message: BlahBlah
# Number of repeats [1]: 1
# BlahBlah
# bin $ sudo echo_mess 
# Please enter a message: BlahBlah
# Number of repeats [1]: 5
# BlahBlah
# BlahBlah
# BlahBlah
# BlahBlah
# BlahBlah
# bin $ 

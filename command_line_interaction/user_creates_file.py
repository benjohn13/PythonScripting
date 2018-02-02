# Writing a script that will allow a user to make a file

#!/bin/python

def get_file_name(reprompt=False):
	if reprompt:
		print("Please enter a name for the file.")

	file_name = raw_input("Destination file name: ").strip()
	return file_name or get_file_name(True)

file_name = get_file_name()

print("Please enter your content. Entering an empty line will write content to %s\n" % file_name)

with open(file_name, 'w') as f:
	eof = False
	lines = []

	while not eof:
		line = raw_input()
	if line.strip():
	  	lines.append("%s\n" % line)
	else: 
	    eof = True

	f.writeline(lines)
	print("Lines written to %s" % file_name)
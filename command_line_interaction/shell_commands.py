# Writing a script called cmd that will run "ls -l" in the CLI when executed
# Note that in subprocess.call there is a '-z' (intentional bug)

#!/bin/python

import subprocess

code = subprocess.call(['ls', '-z'])
if code == 0:
	print("command finished successfully")
else:
	print("failed with code: %i" % code)

# Executing in terminal:
# ~ $ ./cmd
# ls: invalid option -- 'z'
# Try 'ls --help' for more information.
# failed with code: 2
# ~ $ 


# Now let's fix the code so that it will run ls -l in the CLI

#!/bin/python

import subprocess

code = subprocess.call(['ls', '-l'])
if code == 0:
	print("command finished successfully")
else:
	print("failed with code: %i" % code)

# Executing in terminal:
# ~ $ ./cmd
# total 12
# -rwxrw-r--. 1 user user 175 Jan 31 20:02 cmd
# drwxr-xr-x. 2 user user   6 Jan  7  2015 Desktop
# -rw-rw-r--. 1 user user 431 Aug  6  2015 VNCHOWTO
# -rw-------. 1 user user  68 Mar 18  2016 xrdp-chansrv.log
# command finished successfully
# ~$


# Same script as before but getting the output at the end this time
# Note the '-z' again for intentional bug

#!/bin/python

import subprocess

output = subprocess.check_output(['ls', '-z'])

print(output)

# Executing in terminal:
# ~ $ ./cmd
# ls: invalid option -- 'z'
# Try 'ls --help' for more information.
# Traceback (most recent call last):
#   File "./cmd", line 5, in <module>
#     output = subprocess.check_output(['ls', '-z'])
#   File "/usr/lib64/python2.7/subprocess.py", line 575, in check_output
#     raise CalledProcessError(retcode, cmd, output=output)
# subprocess.CalledProcessError: Command '['ls', '-z']' returned non-zero exit status 2
# ~ $ 


# Trying a different bug out (giving it file that does not exist)

#!/bin/python
 
import subprocess

output = subprocess.check_output("ls nofile.txt")

print(output)

# Executing in terminal:
# ~ $ ./cmd
# Traceback (most recent call last):
#   File "./cmd", line 5, in <module>
#     output = subprocess.check_output("ls nofile.txt")
#   File "/usr/lib64/python2.7/subprocess.py", line 568, in check_output
#     process = Popen(stdout=PIPE, *popenargs, **kwargs)
#   File "/usr/lib64/python2.7/subprocess.py", line 711, in __init__
#     errread, errwrite)
#   File "/usr/lib64/python2.7/subprocess.py", line 1327, in _execute_child
#     raise child_exception
# OSError: [Errno 2] No such file or directory
# ~ $ 


# With these errors in mind, let's add some code to handle them

#!/bin/python

import subprocess

try:
	output = subprocess.check_output(
		'ls nofile.txt', 
		stderr=subprocess.STDOUT
		)
except OSError as err:
	print("Caught OSError")
	output = err
except subprocess.CalledProcessError as err:
	print("Caught CalledProcessError")
	output = err

print(output)

# Executing in terminal:
# ~ $ ./cmd
# Caught OSError
# [Errno 2] No such file or directory
# ~ $ 


# Let's clean up the code now and see it run without bugs

#!/bin/python

import subprocess

try:
	output = subprocess.check_output(
		['ls', '-l'], 
		stderr=subprocess.STDOUT
		)
except OSError as err:
	print("Caught OSError")
	output = err
except subprocess.CalledProcessError as err:
	print("Caught CalledProcessError")
	output = err

print(output)

# Executing in terminal:
# ~ $ ./cmd
# total 12
# -rwxrw-r--. 1 user user 338 Jan 31 20:39 cmd
# drwxr-xr-x. 2 user user   6 Jan  7  2015 Desktop
# -rw-rw-r--. 1 user user 431 Aug  6  2015 VNCHOWTO
# -rw-------. 1 user user  68 Mar 18  2016 xrdp-chansrv.log
# ~ $ 
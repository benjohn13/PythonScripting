# bin $
# bin $ pwd
# /bin
# bin $ 
# bin $ sudo vim reverse-file
`````
#!/bin/python

import argparse 

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

with open(args.filename) as f:
	lines = f.readlines()
	lines.reverse()

	if args.limit:
		lines = lines[:args.limit]

	for line in lines:
		print(line.strip()[::-1])

`````
# :wq
# bin $
# bin $ sudo reverse-file nofile.txt
# Traceback (most recent call last):
#  File "/bin/reverse-file", line 12, in <module>
#    with open(args.filename) as f:
# IOError: [Errno 2] No such file or directory: 'nofile.txt'
# bin $ 
# bin $ sudo vim reverse-file

`````
#!/bin/python

import argparse

parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type=int, help='the number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

try :
    f = open(args.filename)
except IOError as err:
    print("Error: file not found")
else:
    with f:
        limit = args.limit
        lines = f.readlines()
        lines.reverse()
        
        if args.limit:
                lines = lines[:limit]
        
        for line in lines:
                print(line.strip()[::-1])

finally:
	print("\nWe're finished!\n")

# The "finally" block here is not really added value. Just demonstrates 
# where you could add some clean up code if needed. 

# https://docs.python.org/2/library/exceptions.html

`````
# :wq
# bin $
# bin $ sudo reverse-file nofile.txt
# Error: file not found
#
# We're finished!
#
# bin $ sudo reverse-file reverse-file 
# )"n\!dehsinif er'eWn\"(tnirp
# :yllanif
#
# )]1-::[)(pirts.enil(tnirp
# :senil ni enil rof
# 
# ]timil:[senil = senil
# :timil.sgra fi
# 
# )(esrever.senil
# )(senildaer.f = senil
# timil.sgra = timil
# :f htiw
# :esle
# )"dnuof ton elif :rorrE"(tnirp
# :rre sa rorrEOI tpecxe
# )emanelif.sgra(nepo = f
# : yrt
#
# )(sgra_esrap.resrap = sgra
#
# )'0.1 s)gorp(%'=noisrev ,'noisrev'=noitca ,'v-' ,'noisrev--'(tnemugra_dda.resrap
# )'daer ot senil fo rebmun eht'=pleh ,tni=epyt ,'l-' ,'timil--'(tnemugra_dda.resrap
# )'daer ot elif eht'=pleh ,'emanelif'(tnemugra_dda.resrap
# )'esrever ni elif a daeR'=noitpircsed(resraPtnemugrA.esrapgra = resrap
#
# esrapgra tropmi
# 
# nohtyp/nib/!#
#
# We're finished!
#
# bin $ 
# bin $ 
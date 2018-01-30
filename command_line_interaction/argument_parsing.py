# bin ~$ 
# bin ~$ pwd
# /home/user/bin
# bin ~$ sudo vim args

`````
#!/bin/python

import sys

print("First argument %s" % sys.argv[1])
`````
# :wq
# bin ~$ sudo args apples
# First argument apples
# bin ~$ 
# bin ~$ sudo args
# Traceback (most recent call last):
#   File '/home/user/bin/args', line 5, in <module>
#     print("First argument %s" % sys.argv[1])
# IndexError: list of index out of range
# bin ~$ 
# bin ~$ sudo vim args
`````
#!/bin/python

import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')
args = parser.parse_args()
`````
# :wq
# bin ~$ sudo args 
# usage: args [-h] filename
# args: error: too few arguments
# bin ~$ sudo args -h
# usage: args [-h] filename
# 
# positional arguments:
#   filename    the file to read
#
# optional arguments:
#   -h, --help  show this help message and exit
# bin ~$ 
# bin ~$ sudo mv args reverse-file
# bin ~$ sudo chmod u+x reverse-file
# bin ~$ sudo vim reverse-file
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
# bin ~$
# bin ~$ reverse-file ./reverse-file
# )]1-::[)(pirts.enil(tnirp
# :senil ni enil rof
# ]timil.sgra:[senil = senil
# :timil.sgra fi
# )(esrever.senil
# )(senildaer.f = senil
# :f sa )emanelif.sgra(nepo htiw
# )(sgra_esrap.resrap = sgra
# )'0.1 s)gorp(%'=noisrev ,'noisrev'=noitca ,'v-' ,'noisrev--'(tnemugra_dda.resrap
# )'daer ot senil fo rebmun eht'=pleh ,tni=epyt ,'l-' ,'timil--'(tnemugra_dda.resrap
# )'daer ot elif eht'=pleh ,'emanelif'(tnemugra_dda.resrap
# )'esrever ni elif a daeR'=noitpircsed(resraPtnemugrA.esrapgra = resrap
# esrapgra tropmi
# nohtyp/nib/!#
# bin ~$
# bin ~$ sudo reverse-file ./reverse-file --limit 5
# )]1-::[)(pirts.enil(tnirp
# :senil ni enil rof
# ]timil.sgra:[senil = senil
# :timil.sgra fi
# bin ~$
# bin ~$
#
# https://docs.python.org/2/howto/argparse.html
#
# https://docs.python.org/3/library/argparse.html

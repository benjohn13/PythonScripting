# Writing a script that can parse a file with over 479,000 words and find 
# specific (or partial) words that we give as input.


# bin $
# bin $ sudo yum install -y words
# Loaded plugins: fastestmirror
# Loading mirror speeds from cached hostfile
#  * base: mirrors.sonic.net
#  * epel: mirror.es.its.nyu.edu
#  * extras: mirrors.cmich.edu
#  * nux-dextop: mirror.li.nux.ro
#  * updates: mirror.math.princeton.edu
# Resolving Dependencies
# --> Running transaction check
# ---> Package words.noarch 0:3.0-22.el7 will be installed
# --> Finished Dependency Resolution
# Dependencies Resolved
# ==============================================================================
#  Package                        Arch                            Version       
# ==============================================================================
# Installing:
#  words                          noarch                          3.0-22.el7    
# Transaction Summary
# ==============================================================================
# Install  1 Package
# Total download size: 1.4 M
# Installed size: 4.7 M
# Downloading packages:
# words-3.0-22.el7.noarch.rpm                                 | 1.4 MB  00:00:00     
# Running transaction check
# Running transaction test
# Transaction test succeeded
# Running transaction
#   Installing : words-3.0-22.el7.noarch                                    1/1 
#   Verifying  : words-3.0-22.el7.noarch                                    1/1 
# Installed:
#   words.noarch 0:3.0-22.el7                                                                                                               
# Complete!
# bin $
# bin $ sudo vim contains

================================================================================
#!/bin/python

import argparse

parser = argparse.ArgumentParser(description='Search for words including partial words')
parser.add_argument('snippet', help='partial (or complete) string to search for in the file')

args = parser.parse_args()
snippet = args.snippet.lower()

words = open('/usr/share/dict/words').readlines()
matches = []

for word in words:
    if snippet in word.lower():
        matches.append(word)

print(matches)

================================================================================

# bin $
# bin $ sudo chmod u+x contains
# bin $ sudo contains Alice
# ['Alice\n', 'alice\n', 'Alicea\n', 'Alice-in-Wonderland\n', 'Aliceville\n', 
# 'calices\n', 'chalice\n', 'chaliced\n', 'chalices\n', 'Doralice\n', '
# enchalice\n', 'fortalice\n', 'malice\n', 'maliceful\n', 'maliceproof\n', 
# 'malices\n', 'Maryalice\n', 'salicetum\n']
# bin $
# bin $ # bin $ sudo vim contains

================================================================================
#!/bin/python

import argparse

parser = argparse.ArgumentParser(description='Search for words including partial words')
parser.add_argument('snippet', help='partial (or complete) string to search for in the file')

args = parser.parse_args()
snippet = args.snippet.lower()

# Removing the 'for' loop and empty 'matches' list  

words = open('/usr/share/dict/words').readlines()

print([word.strip() for word in words if snippet in word.lower()])

================================================================================

# bin $
# bin $ sudo contains turnip
# ['turnip', 'turnip-bearing', 'turnip-eating', 'turnip-fed', 'turnip-growing', 
# 'turnip-headed', 'turnip-leaved', 'turniplike', 'turnip-pate', 'turnip-pointed', 
# 'turnip-rooted', 'turnips', 'turnip-shaped', 'turnip-sick', 'turnip-stemmed', 
# 'turnip-tailed', 'turnipweed', 'turnipwise', 'turnipwood', 'turnipy', 'turnip-yielding']
# bin $
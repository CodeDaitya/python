#reading files

from sys import argv

script,filename=argv
txt=open(filename) #opening file using name unpacked from argv

print "Here's your file."
txt.read() #read the opened file

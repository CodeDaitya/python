from sys import argv
from os.path import exists

script,from_file,to_file=argv

print "Copying from file %s to file %s."%(from_file,to_file)

in_file=open(to_file)
indata=in_file.read()

print "Input file is %d bytes long."%len(indata)

#print "Does the output file exists?%r"%exists(to_file)
print "Ready, hit RETURN to continue, CTR-Z to abort.",
raw_input()

out_file=open(to_file,'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

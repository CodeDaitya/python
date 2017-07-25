print "Name of the file."
filename=raw_input(">")

txt=open(filename)

print "Here's your file."
txt.read()
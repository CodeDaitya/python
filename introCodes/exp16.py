filename=raw_input()
print "We are going to erase %r."%filename
print "If you don't want to do it, hit CTR-Z(^Z)."
print "If you do want to do it, hit ENTER."
raw_input("?")

print "Opening the file..."
target=open(filename,'w+')
target.read()

print "Truncating the file. Goodbye!"
target.truncate()
target.read()

print "Now I'm going to ask you three lines."

line1=raw_input("Line 1: ")
line2=raw_input("Line 2: ")
line3=raw_input("Line 3: ")

print "I'm going to write these lines to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.read()

print "And finally, we close it."
target.close()

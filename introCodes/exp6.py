#strings assigned to respective variables
x="There are %d type of people."%10 #assignment using formatting
binary="binary"
do_not="don't"
y="Those who know %s and those who %s."%(binary,do_not) #line 2

print x #print x
print y #print y

print "I said: %r"%x #%r formatting->print no matter what
print "I also said: %s"%y #normal string formatting

hilarious=False #assigning predefined keyword False
joke_evaluation="Isn't that joke so funny?! %r" #pre-formatting
print joke_evaluation%hilarious 

#defining new strings
w="This is the left side of..."
e="a string with a right side."

print w+e #concatinating strings
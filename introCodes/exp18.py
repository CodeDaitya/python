#this one is like your script with argv

def print_two(*args):
 arg1,arg2=args
 print "arg1: %r, arg2: %r"%(arg1,arg2)
 
#ok, that args is pointless, we can just do it this way
def print_two_again(arg1,arg2):
 print "arg1: %r, arg2: %r"%(arg1,arg2)
 
 #this takes only one argument
def print_one(arg1):
 print "arg1: %r"%arg1
 
#this takes no arguments
def print_none():
 print "I've got nothing."
 
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First")
print_none()

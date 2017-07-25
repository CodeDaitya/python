print "You enter a dark room with two doors. Do you go through door #1 or door #2?"
door=raw_input(">")

if door=="1":
    print "There is a giant bear here eating a cheese cake. What you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
	
    bear=raw_input(">")
    if bear=="1":
        print "Bear eats off your face. Good job!"
    elif bear=="2":
	    print "Bear eats off your leg. Good job."
    else:
        print "Well, doing %s is better. Bear runs away."%bear
		
elif door=="2":
    print "You stare into the ebdless abyss of Cthulhu's retina."
    print "1. Bleberries."
    print "2. Yellow jacket clothspin."
    print "3. Understading revolvers yelling melodies."
	
    insanity=raw_input(">")
    
    if insanity=="1" or insanity=="2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "Insanity rots your eyes into a pool of muck. Good job!"
else:
    print "You stumble around and fall on a knife and die. Good job!"
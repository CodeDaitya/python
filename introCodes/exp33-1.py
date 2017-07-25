def print_num(ul,inc):
    i=0
    numbers=[]
    while i<ul:
	    print "At the top i is %d."%i
	    numbers.append(i)
		
	    i+=inc
	    print "Numbers now: ",numbers
        print "At the bottom i is %d."%i
	
    for num in numbers:
	    print num
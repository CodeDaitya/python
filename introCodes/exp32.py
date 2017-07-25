the_count=[1,2,3,4,5]
fruits=['apples','oranges','pears','apricots']
change=[1,'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d"%number

#same as above
for fruit in fruits:
    print "A fruit of type: %s"%fruit
	
#also we can go through mixed lists too
for i in change:
    print "I got %r change"%i
	
#we can also build a list, first start with an empty one
elements=[]

#then use range function to do 0 to 5 count
for i in range(0,6):
    print "Adding %d to the list."%i
    #append is a function that list understands
    elements.append(i)
	
#now we can print them too
for i in elements:
    print "Element was: %d"%i
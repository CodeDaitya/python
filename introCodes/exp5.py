name="Zed A. Shaw"
age=35 #not a lie
height=74 #inches
height_cm=74*2.54 #centimeters
weight=180 #lbs
weight_kg=180*0.45 #kilograms
eyes="Blue"
teeth="White"
hair="Brown"

print "Let's talk about %s."%name
print "He's %d inches tall, i.e. %f centimeters."%(height,height_cm)
print "He's %d pounds, i.e. %f kilograms heavy."%(weight,weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair."%(eyes,hair)
print "His teeth are usually %s depending on the coffee."%teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d and %d, I get %d."%(age,height,weight,age+height+weight)
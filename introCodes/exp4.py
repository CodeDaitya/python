cars=100 #number of cars
sapce_in_car=4.0 #space in each car in floating point number
drivers=40 #number of drivers available
passengers=90 #number of passengers to be transported
cars_not_driven=cars-drivers #cars without driver
cars_driven=drivers #cars with driver
carpool_capacity=cars_driven*sapce_in_car #maximum number of passengers in a car
average_passenger_in_car=passengers/cars_driven #average passengers in each car

print "There are", cars,"cars available."
print "There are only", drivers, "drivers."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put atleast", average_passenger_in_car, "in each car."
road_rage.py is a traffic simulation program.  This can be run from the terminal
by calling python3 and using the necessary components found in the
requirements.txt file.

This program operates under the assumptions that:

    -Drivers want to go up to 120 km/hr.
    -The average car is 5 meters long.
    -Drivers want at least a number of meters equal to their speed in meters/second between them and the next car.
    -Drivers will accelerate 2 m/s up to their desired speed as long as they have room to do so.
    -If another car is too close, drivers will match that car's speed until they have room again.
    -If a driver would hit another car by continuing, they stop.
    -Drivers will randomly (10% chance each second) slow by 2 m/s.
    -This section of road is one lane going one way.
    -The program treats the road as circular, thus, cars exiting the road start again at the beginning.
      -This is to simulate a continuous stream of traffic.

A separate class file, Car_Simulator.py, is available. This class could be used to track,
monitor and separate any number of inanimate objects along a one dimentional highway.  
Ie. 30 cars down a simulated road.  The objects accelerate until they get near the object in
front of them, and then the slow to the same speed.  Objects can randomly
slow down and even come to a stop.  The user of this class needs to pass
in a list of objects ( cars ). 

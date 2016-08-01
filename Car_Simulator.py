# cars class

class CarSimulation:
    """ This class could be used to track, monitor and separate any number of
    inanimate objects along a one dimentional highway.  Ie. 30 cars done a
    simulated road.  The objects accelerate until they get near the object in
    front of them, and then the slow to the same speed.  Objects can randomly
    slow down and even come to a stop.  The user of this class needs to pass
    in a list of objects ( cars ). """
    def __init__(self, speed, accel, location):
        self.speed = speed
        self.accel = accel
        self.location = location


    def calc_averages(avg_speed,cars,num_cars):
        for each in cars:
            avg_speed += int(each[0])
        return avg_speed/num_cars


    # print them
    def check_distance(min_dist, cars, num_cars):
        for i in range((num_cars-1)):
            dist = cars[i+1][2] - cars[i][2]
            dist -= 4
            if dist < min_dist:
                if cars[i][0] > cars[i+1][0]:
                    cars[i][0] = cars[i+1][0]

            if dist == 1:
                cars[i][0] = 0
        return cars


    def update_car_speed(cars):
        for each in cars:
            each[0] += each[1]
            if each[0] > 33:
                each[0] = 33
        return cars


    # wait one second !!!!!!
    def update_car_position(cars):
        for each in cars:
            each[2] += each[0]
        return cars


    def switch_cars_positions(cars):
        # pass
        temp_holdr = cars[num_cars-1]
        count = (num_cars-1)
        while count > 0:
            cars[count] = cars[count-1]
            count -= 1
        cars[0] = temp_holdr
        cars[0][2] = 4
        return cars


    def check_valid_position(cars):
        if cars[num_cars-1][2] > 999:
            switch_car_positions()
        return cars


    def random_slowdown(cars):
        for each in cars:
            x = random.randint(0, 9)
            if x == 5:
                each[0] -= 4
                if each[0] < 0:
                    each[0] = 0
        return cars

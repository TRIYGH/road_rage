# W3D4 road_rage Project

import random

# car = []
#initialize cars
# for i in range(30):
#     car[i] = Car().car


car=[]  #[0,1,2]
car.append([0,2,5])
car.append([0,2,19])
car.append([0,2,26])
# car[0] = [0,2,5]   # speed, accel, loc
# car[1] = [0,2,19]
# car[2] = [0,2,26]


def print_them():
    # print(car[0], car[1], car[2])
    # input()
    print("\n"*65)

# print them
def check_distance(min_dist):
    for i in range(2):
        dist = car[i+1][2] - car[i][2]
        dist -= 4
        if dist < min_dist:
            car[i][0] = car[i+1][0]
            car[i][2] -= 10

        if dist == 1:
            car[i][0] = 0
            car[i][2] -= 10


#wait one second !!!!!!
def update_car_position():
    for each in car:
        each[0]+=each[1]
        each[2]+=each[0]


def random_slowdown():
    for each in car:
        x = random.randint(0,9)
        if x == 5:
            each[0] -= 2   #IF you change this to each[1] it accels like crazy


while True:
    print_them()
    check_distance(5)
    update_car_position()
    random_slowdown()

#==========
    # position on road is 5 thru 1000

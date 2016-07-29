#W3D4  road project

import random

car = []
#initialize cars
for i in range(30):
    car.append([0,2,(12+(7*i))])                 # [ speed, accel, loc ]

num_cars = len(car)


def print_them():
    print("\n"*65)
    spaces = car[0][2]
    print(' '*spaces, end='')                   #print FIRST car
    print('0'*6, end='')

    for i in range(1,num_cars):
        spaces = car[i][2] - car[i-1][2] - 5    #print spaces
        print(' '*spaces, end='')
        if i < 10:
            print(str(i)*6, end='')
        else:                                   #print car x
            print(str(i)*3, end='')

    spaces = car[29][2] - car[28][2] - 5    #print spaces
    print(' '*spaces, end='')
    print('30'*3)

    input()


# print them
def check_distance(min_dist):
    for i in range((num_cars-1)):
        dist = car[i+1][2] - car[i][2]
        dist -= 4
        if dist < min_dist:
            if car[i][0] > car[i+1][0]:
                car[i][0] = car[i+1][0]
            # car[i][2] -= 10

        if dist == 1:
            car[i][0] = 0
            # car[i][2] -= 10


def update_car_speed():
    for each in car:
        each[0]+=each[1]
        if each[0] > 33:
            each[0] = 33


#wait one second !!!!!!
def update_car_position():
    for each in car:
        each[2]+=each[0]


def switch_car_positions():
    # pass
    temp_holdr = car[num_cars-1]
    count = (num_cars-1)
    while count > 0:
        car[count] = car[count-1]
        count -= 1
    car[0] = temp_holdr
    car[0][2] = 4



def check_valid_position():
    if car[num_cars-1][2] > 999:
        switch_car_positions()


def random_slowdown():
    for each in car:
        x = random.randint(0,9)
        if x == 5:
            each[0] -= 4   #IF you change this to each[1] it accels like crazy
            if each[0] < 0:
                each[0] = 0


while True:
    print_them()
    check_distance(5)
    update_car_speed()
    update_car_position()
    check_valid_position()
    random_slowdown()

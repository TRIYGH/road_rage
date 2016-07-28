# W3D4 road_rage Project

import random


car=[]  #[0,1,2]
car.append([0,2,12])
car.append([0,2,19])
car.append([0,2,26])


def print_them():
    # print(car[0], car[1], car[2])
    # input()
    print("\n"*65)
    spaces = car[0][2]
    print(' '*spaces, end='')
    print("D###D", end='')
    spaces = car[1][2] - car[0][2]
    print(' '*spaces,"D###D", end='')
    spaces = car[2][2] - car[1][2]
    print(' '*spaces,"D###D", end='')
    input()



# print them
def check_distance(min_dist):
    for i in range(2):
        dist = car[i+1][2] - car[i][2]     # speed, accel, loc
        dist -= 4
        if dist < min_dist:
            car[i][0] = car[i+1][0]
            # car[i][0] -= 10
        if dist == 1:
            car[i][0] = 0
            # car[i][2] -= 10


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

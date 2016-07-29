from Car import Car
import random

# car = []
#initialize cars
# for i in range(30):
#     car[i] = Car().car


car=[]  #[0,1,2]
car.append([0,2,12])
car.append([0,2,19])
car.append([0,2,26])
num_cars = len(car)

# car[0] = [0,2,5]   # speed, accel, loc
# car[1] = [0,2,19]
# car[2] = [0,2,26]


def print_them():
    print(car[0], car[1], car[2])
    input()
    # print("\n"*65)
    # spaces = car[0][2]
    # print(' '*spaces, end='')
    # print("00000", end='')
    # spaces = car[1][2] - car[0][2] - 5
    # print(' '*spaces,"11111", end='')
    # spaces = car[2][2] - car[1][2] - 5
    # print(' '*spaces,"22222",car, end='')
    # input()


# print them
def check_distance(min_dist):
    for i in range((num_cars-1)):
        dist = car[i+1][2] - car[i][2]     # speed, accel, loc
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
            each[0] -= 2   #IF you change this to each[1] it accels like crazy


while True:
    print_them()
    check_distance(5)
    update_car_speed()
    update_car_position()
    check_valid_position()
    random_slowdown()

#==========
    # position on road is 5 thru 1000

ferari = Car()

# W3D4  road project

import numpy as np
import matplotlib.animation as animation
import seaborn
import statistics as st
import random
import matplotlib.pyplot as plt


cars = []
diff_bt_cars = []
speeds = []
avg_speed = 0
p = []
z = []

# initialize cars
for i in range(30):
    cars.append([0, 2, (12+(7*i))])       # [ speed, accel, loc ]

num_cars = len(cars)


def animate(i=0):
    main()
    p = [int(car[0]) for car in cars]
    z = [int(car[2]) for car in cars]
    points = list(zip(z, p))
    paths.set_offsets(points)
    return paths,


def plot_it(x, y):
    plt.title('Car Traffic Simulation (# of cars = 30)')
    plt.xlabel('Distance bt Cars')
    plt.ylabel('Velocity (km/h)')
    plt.xlim((0, 100))
    plt.ylim((0, 34))
    plt.scatter(x, y, marker='s', cmap='set1', alpha=0.5)
    plt.show()


def plot_them():
    for i in range(1, num_cars):
        diff_bt_cars.append(cars[i][2] - cars[i-1][2] - 4)
        speeds.append(cars[i][0])
        # avg_speed_list(avg_speed_ofeaccar, after acceleration period)
        #
        # Distance_traveled = 0


def averages_graph(avgs_list):
    plt.title('Average Speeds')
    plt.hist(avgs_list)
    plt.show()


def std_dev(avgs_list):
    plt.hist(avgs_list)
    mean = st.mean(avgs_list)
    stdev = st.stdev(avgs_list)
    ymin, ymax = plt.ylim()

    plt.vlines(mean, ymin, ymax, color='red')
    plt.vlines([mean - 2 * stdev, mean - stdev, mean + stdev, mean + 2 * stdev],
               ymin, ymax, color='red', linestyles='dashed')
    plt.show()


def print_them():
    print("\n"*65)
    spaces = cars[0][2]
    print(' '*spaces, end='')                   # print FIRST car
    print('0'*6, end='')

    for i in range(1, num_cars):
        spaces = cars[i][2] - cars[i-1][2] - 5    # print spaces
        print(' '*spaces, end='')
        if i < 10:
            print(str(i)*6, end='')
        else:                                   # print car x
            print(str(i)*3, end='')

    spaces = cars[29][2] - cars[28][2] - 5    # print spaces
    print(' '*spaces, end='')
    print('30'*3)

    # input()


def calc_averages(avg_speed):
    for each in cars:
        avg_speed += int(each[0])
        # print(each[0])
    # input("enter")
    return avg_speed/30


# print them
def check_distance(min_dist):
    for i in range((num_cars-1)):
        dist = cars[i+1][2] - cars[i][2]
        dist -= 4
        if dist < min_dist:
            if cars[i][0] > cars[i+1][0]:
                cars[i][0] = cars[i+1][0]
            # car[i][2] -= 10

        if dist == 1:
            cars[i][0] = 0
            # car[i][2] -= 10


def update_car_speed():
    for each in cars:
        each[0] += each[1]
        if each[0] > 33:
            each[0] = 33


# wait one second !!!!!!
def update_car_position():
    for each in cars:
        each[2] += each[0]


def switch_car_positions():
    # pass
    temp_holdr = cars[num_cars-1]
    count = (num_cars-1)
    while count > 0:
        cars[count] = cars[count-1]
        count -= 1
    cars[0] = temp_holdr
    cars[0][2] = 4


def check_valid_position():
    if cars[num_cars-1][2] > 999:
        switch_car_positions()


def random_slowdown():
    for each in cars:
        x = random.randint(0, 9)
        if x == 5:
            each[0] -= 4   # IF you change this to each[1] it accels like crazy
            if each[0] < 0:
                each[0] = 0


inital_acceleration_period = True
loops = 0
avg_speed_list = []

    # while loops < 100:
    #     loops += 1
    #     if loops > 25:
    #         inital_acceleration_period = False
    #
    #     # print_them()
    #
    #     if inital_acceleration_period == False:
    #         avg_speed_list.append(calc_averages(avg_speed))
    #         avg_speed = 0
def main():
    # plot_cars(car)
    check_distance(5)
    update_car_speed()
    update_car_position()
    check_valid_position()
    random_slowdown()

    # p = [int(_[0]) for _ in car]
    # z = [int(_[2]) for _ in car]

fig, ax = plt.subplots(figsize=(20, 10))

plt.title('Car Traffic Simulation (# of cars = 30)')
plt.xlabel('Distance traveled (m)')
plt.ylabel('Velocity (km/h)')
plt.xlim((0, 1000))
plt.ylim((0, 50))
paths = ax.scatter(z, p, s=20, marker='s', cmap='set1', alpha=1)

ani = animation.FuncAnimation(fig, animate, frames=None, init_func=None, fargs=None, blit=False, interval=100)
plt.show()


# plot_them()
# input("ENTER")
# print(sum(avg_speed_list))
#
# averages_graph(avg_speed_list)
#
# std_dev(avg_speed_list)

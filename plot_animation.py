import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import seaborn

class Animate:

    def init():
        scatter.set_data([], [])
        return scatter

    def animate(i):
        x = [car[2] for _ in car]
        y = [car[0] for _ in car]
        scatter.set_data(x, y)
        return scatter

    # def fig():


    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=200, interval=20, blit=False)


    plt.title('Car Traffic Simulation (# of cars = 30)')
    plt.xlabel('Distance traveled (m)')
    plt.ylabel('Velocity (km/h)')
    plt.xlim((0, 1000))
    plt.ylim((0, 50))
    plt.scatter(x, y, marker='s', cmap='set1', alpha=0.5)
    plt.show()


#     def main():
#     numframes = 100
#     numpoints = 10
#     color_data = np.random.random((numframes, numpoints))
#     x, y, c = np.random.random((3, numpoints))
#
#     fig = plt.figure()
#     scat = plt.scatter(x, y, c=c, s=100)
#
#     ani = animation.FuncAnimation(fig, update_plot, frames=xrange(numframes),
#                                   fargs=(color_data, scat))
#     plt.show()
#
# def update_plot(i, data, scat):
#     scat.set_array(data[i])
#     return scat,
#
# main()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn

# class Animate:
#
#     def init():
#         scatter.set_data([], [])
#         return scatter
#
#     def animate(i):
#         x = [car[2] for _ in car]
#         y = [car[0] for _ in car]
#         scatter.set_data(x, y)
#         return scatter
#
#     # def fig():
#
#
#     # call the animator.  blit=True means only re-draw the parts that have changed.
#     anim = animation.FuncAnimation(fig, main(), init_func=init,
#                                    frames=200, interval=20, blit=False)


x = [1, 2, 3]
y = [1, 2, 3]

fig, ax = plt.subplots()

plt.title('Car Traffic Simulation (# of cars = 30)')
plt.xlabel('Distance traveled (m)')
plt.ylabel('Velocity (km/h)')
plt.xlim((0, 1000))
plt.ylim((0, 50))
paths = ax.scatter(x, y, marker='s', cmap='set1', alpha=1)


def animate(i):
    x[0] += 0.5
    x[1] += 0.55
    x[2] += 0.1
    y[0] += 0.51
    y[1] += 0.5
    y[2] += 0.1
    points = list(zip(x, y))
    paths.set_offsets(points)
    return paths,


ani = animation.FuncAnimation(fig, animate, interval=60)
plt.show()

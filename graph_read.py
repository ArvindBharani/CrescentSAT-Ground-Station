import matplotlib
import matplotlib.pyplot as pyplot
import matplotlib.animation as animation
from matplotlib import style
from firebase import firebase
from multiprocessing import Process

firebase = firebase.FirebaseApplication('https://flight-planer-crescentsat.firebaseio.com')

matplotlib.use("TkAgg")
style.use("dark_background")

fig = pyplot.figure()
axl = fig.add_subplot(111)


def animate(i):
    graph_data = open('input_graph.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    axl.clear()
    axl.plot(xs, ys)
    pyplot.ylabel('ALTITUDE')
    pyplot.xlabel('TEMPERATURE')

ani = animation.FuncAnimation(fig, animate, interval=1000)

pyplot.show()


import alive as alive
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pandas as pd
from random import randint
data = pd.read_csv("https://raw.githubusercontent.com/DavidSanchez2002/CSV/main/USA_cars_datasets.csv")
x = []
y = []
fig, ax = plt.subplots()
def animate(i):
    pt = randint(0,data.price.count()) # grab a random integer to be the next y-value in the animation
    p= data.price[i]
    x.append(i)
    y.append(p)

    ax.clear()
    ax.plot(x, y)
    ax.set_xlim([0,30])
    ax.set_ylim([0,data.price.max()])


ani = FuncAnimation(fig, animate, frames=data.price.count(), interval=500, repeat=False)
plt.show()


#Model the number of rabbits from a starting population and each successive generation
#population model: x_(n+1) = rx_n(1-x_n)
#x=rabbit population, as a percentage of the carrying capacity. Cannot be over 1.
#r=growth rate, 0-4
#n=year

#Find out how to put graphs in python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button, Slider

initial_pop = .3
growth_rate = 2.6

#x_1 = r*x*(1-x)

def set_points(r,p):
    x=[]
    y=[]
    for i in range(10000):
        x.append(i)
        y.append(r*p*(1-p))
        p = y[-1]
    return x, y

init_x, init_y = set_points(growth_rate, initial_pop)

fig, ax = plt.subplots()
ax.plot(init_x[:100],init_y[:100])
fig.subplots_adjust(bottom=0.35)

#Growth Rate Slider
axgrow = fig.add_axes([0.25, .2, 0.65, 0.03])
grow_slider = Slider(
    ax=axgrow,
    label ='Growth rate',
    valmin=0,
    valmax=4,
    valinit=growth_rate
)

#Initial Population Slider
axpop = fig.add_axes([0.25, 0.1, 0.65, 0.03])
pop_slider = Slider(
    ax=axpop,
    label = 'Initial Population',
    valmin = 0,
    valmax = 1,
    valinit = initial_pop
)

#Updates the graph based on the new slider position
def update_graph(val):
    growth_rate = grow_slider.val
    initial_pop = pop_slider.val
    ax.clear()
    ax.set_xlabel('Time')
    ax.set_ylabel('Population')
    ax.set_title("Rabbit Population Over Time")
    x, y = set_points(growth_rate, initial_pop)
    ax.plot(x[:100],y[:100])


#Graph logistics
grow_slider.on_changed(update_graph)
pop_slider.on_changed(update_graph)

#Graph Labels
ax.set_xlabel('Time')
ax.set_ylabel('Population')
ax.set_title("Rabbit Population Over Time")

#Second Graph
##the growth rate (x-axis) vs where the population settles / the limit of the population (y)
##interval for growth rate: .01
#plt.figure(2)
fig2, ax2 = plt.subplots()

def graph(x):
    """Gets y values from growth rate, then adds to scatter plot"""
    x2 = x
    y2 = []
    p2 =.7

    for i in range(1000):
        y2.append(x*p2*(1-p2))
        p2 = y2[-1]

    for i in range(len(y2)):
        y2[i] = y2[i] = round(y2[i], 2)

    y2=list(set(y2[500:]))

    for i in range(len(y2)):
        plt.scatter(x2,y2[i], s=2)

for i in range(0,400,1):
    graph(i/100)

#Graph Labels
ax2.set_xlabel('Growth Rate')
ax2.set_ylabel('Population Limit')
ax2.set_title("Population Limits at Different Growth Rates")

plt.show()
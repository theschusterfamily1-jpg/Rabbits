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
    for i in range(100):
        x.append(i)
        y.append(r*p*(1-p))
        p = y[-1]
    return x, y

init_x, init_y = set_points(growth_rate, initial_pop)

fig, ax = plt.subplots()
ax.plot(init_x,init_y)
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

# The function to be called anytime a slider's value changes

def update_graph(val):
    growth_rate = grow_slider.val
    initial_pop = pop_slider.val
    ax.clear()
    x, y = set_points(growth_rate, initial_pop)
    ax.plot(x,y)


grow_slider.on_changed(update_graph)
pop_slider.on_changed(update_graph)



#Graph Labels
ax.set_xlabel('Time')
ax.set_ylabel('Population')
ax.set_title("Population Over Time")

plt.show()


#Graph the population model starting with a specific population and growth rate of 0, rising to 4

#the two graphs should be:
##the growth rate vs population over time
##the growth rate vs where the population settles / the limit of the population
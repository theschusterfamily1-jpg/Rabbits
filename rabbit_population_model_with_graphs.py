#Model the number of rabbits from a starting population and each successive generation
#population model: x_(n+1) = rx_n(1-x_n)
#x=rabbit population, as a percentage of the carrying capacity. Cannot be over 1.
#r=growth rate, 0-4
#n=year

#Find out how to put graphs in python
import matplotlib.pyplot as plt
import numpy as np

initial_pop = .4

x = []
y = []
#x_1 = r*x*(1-x)

for i in range(100):
    x.append(i)
    y.append(2.6*initial_pop*(1-initial_pop))
    initial_pop = y[-1]

fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_xlabel('Time')
ax.set_ylabel('Population')
ax.set_title("Population Over Time")

plt.show()

#Find out how to communicate the population model to python
#y=rx(1-x)
#set y to a variable that feeds back into the equation as the next value of x?

#Prompt the user for initial population (fraction of 1)
#Graph the population model starting with a specific population and growth rate of 0, rising to 4

#the two graphs should be:
##the growth rate vs population over time
##the growth rate vs where the population settles / the limit of the population
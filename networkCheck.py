import random
from getspeed import *

amount_of_tests = 5

chartData = []

for i in range(10):
    chartData.append(0)

def update():
    del(chartData[0])
    average = 0
    for i in range (amount_of_tests):
        average += downloadsp()
    print (average)
    chartData.append(average)

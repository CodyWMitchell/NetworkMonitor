import random, sys
from getspeed import *

amount_of_tests = 5

chartData = []

for i in range(1000):
    chartData.append(0)

def update():
    del(chartData[0])
    sum = 0
    for i in range (amount_of_tests):
        sum += downloadsp()
    print("AVERAGE SPEED:",sum/amount_of_tests)
    chartData.append(sum/amount_of_tests)
    sys.stdout.flush()
    update()

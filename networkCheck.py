import random, sys
from getspeed import *

amount_of_tests = 5 # Number of Tests Executed

chartData = []

for i in range(500): # Number of data points
    chartData.append(0)

def update(): # Get average speed and then add that update to the table, continuously runs
    del(chartData[0])
    sum = 0
    for i in range (amount_of_tests):
        sum += downloadsp() # Get Download Speed Average
    print("AVERAGE SPEED:",sum/amount_of_tests)
    chartData.append(sum/amount_of_tests) # Add to Chart Data
    sys.stdout.flush()
    update() # Run again!

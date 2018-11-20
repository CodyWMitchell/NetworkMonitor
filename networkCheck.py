import random

chartData = []

for i in range(10):
    chartData.append(random.randint(0,1750))

def update():
    del(chartData[0])
    chartData.append(random.randint(0,400))

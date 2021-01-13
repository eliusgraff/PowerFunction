#MyPowerFunction.py
import csv
import sys
from time import perf_counter_ns

#recursve POW function returning base^(exponent-1)
def RecursiveFunction(base, exponent):
    if exponent == 0:
        return 1

    return base * RecursiveFunction(base, exponent-1)

base = 3.14159265359
exponent = 1
total = 1

#python auto-caps this, so lets set it so we surely overflow stack!!
sys.setrecursionlimit(1000000)

#this is where we are writing our data
with open('datafile.csv', 'w', newline='') as CSVfile:
    writeToMe = csv.writer(CSVfile)
    writeToMe.writerow(["exponent", "recursive time", "iterative time"])

    while True :
        
        #start timer1
        iterativeTime = perf_counter_ns()
        for i in range(1, exponent+1):
            total *= base
        iterativeTime = perf_counter_ns() - iterativeTime
        #end timer1
        
        #start timer2
        recursiveTime = perf_counter_ns()
        RecursiveFunction(base, exponent)
        recursiveTime = perf_counter_ns() - recursiveTime
        #stop timer2
        
        #write times and numbers to CSV file
        writeToMe.writerow([ exponent, recursiveTime, iterativeTime])
        total = 1

        exponent += 1   #move on to the next exponent
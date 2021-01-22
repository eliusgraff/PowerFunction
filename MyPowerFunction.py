#MyPowerFunction.py
import csv
import sys
from time import perf_counter_ns

#recursve POW function returning base^(exponent-1)
def RecursiveFunction(base, exponent):
    if exponent == 0:
        return 1

    return base * RecursiveFunction(base, exponent-1)

#iterative POW function using for loop to multiply base by itself n times in a loop
def IterativeFunction(base, exponent):
    total = 1

    for i in range(1, exponent+1):
            total *= base

    return total


#start of 'main' program
base = 3.14159265359
exponent = 1

#python auto-caps this, so lets set it so we surely overflow stack!!
sys.setrecursionlimit(200000)

#this is where we are writing our data
with open('datafile.csv', 'w', newline='') as CSVfile:
    writeToMe = csv.writer(CSVfile)
    writeToMe.writerow(["exponent", "recursive time", "iterative time"])

    while True :
        
        #start timer1
        iterativeTime = perf_counter_ns()
        IterativeFunction(base, exponent)
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

        exponent += 5   #since we take so many points lets just do every 5
#MyPowerFunction.py
import csv
import sys
from time import perf_counter_ns

def RecursiveFunction(base, exponent):
    if exponent == 0:
        return 1

    return base * RecursiveFunction(base, exponent-1)

base = 3.14159265359
exponent = 1
total = 1

sys.setrecursionlimit(1000000)

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
        
        writeToMe.writerow([ exponent, recursiveTime, iterativeTime])
        total = 1

        #write times and numbers to CSV file
        exponent += 1
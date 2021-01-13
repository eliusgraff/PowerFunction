#MyPowerFunction.py
import csv
from time import perf_counter_ns

def RecursiveFunction(base, exponent):
    if exponent == 0:
        return 1

    return base * RecursiveFunction(base, exponent-1)

base = 3.14159265359
exponent = 1
total1 = 1
total2 = 1

with open('datafile.csv', 'w', newline='') as CSVfile:
    writeToMe = csv.writer(CSVfile)
    writeToMe.writerow(["exponent", "recursive time", "iterative time"])
    while True :
        iterativeTime = perf_counter_ns()
        #start timer1
        
        for i in range(1, exponent+1):
            total1 *= base
        #end timer1
        iterativeTime = perf_counter_ns() - iterativeTime

        

        recursiveTime = perf_counter_ns()
        #start timer2
        total2 = RecursiveFunction(base, exponent)
        #stop timer2
        recursiveTime = perf_counter_ns() - recursiveTime

        writeToMe.writerow([ exponent, recursiveTime, iterativeTime, total1, total2])
        total1 = 1

        #write times and numbers to CSV file
        exponent += 1
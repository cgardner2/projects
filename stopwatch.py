#! user/bin/env Python3
#Stopwatch.py - a simple stopwatch program

import time

#display program instructions
print("press ENTER to begin. Press ENTER again to hit the stopwatch \n"
      " Press Ctrl-C to quit")

input() # press Enter to begin
print("Started.")
start_time = time.time() #gets first laps start time
last_time = start_time
lapNum =1

#Starts tracking laps
try:
    while True:
        input()
        lap_time = round(time.time()-last_time,2)
        total_time = round(time.time()-start_time,2)
        print("Lap #%s: %s (%s)" %(lapNum,total_time,lap_time), end="")
        lapNum +=1
        last_time = time.time() #resets lap time
except KeyboardInterrupt:
    #handles control-c interruption message
    print("\n Done!")
# Exercise 8
## Objective: create a function timer(num); when run it should count down from "num" seconds, while printing each iteration number
import time
def timer(num, timer_secounds = 30):
    while num < 0:
        num -= 1
        time.sleep(timer_secounds)
        print(num)
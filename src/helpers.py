# Helper functions
import time

def type_print(string, delay = 0.06):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)

# BUILD
# function that will check if the passed in time is greater than 24. If it is, get it back down to proper time and update the day
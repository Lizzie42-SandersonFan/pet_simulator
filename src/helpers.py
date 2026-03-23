# Helper functions
import time

def type_print(string, delay = 0.06):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)

# BUILD
# function that will check if the passed in time is greater than 24. If it is, get it back down to proper time and update the day
def check_time(time):
    if time < 24:
        time = time % 24
        # Returning 1 because it will tell me to add one to the day
        return 1
    elif time < 0:
        # This should not happen. Returning 0
        return 0
    else:
        time = time
        return 0
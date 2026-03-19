# Helper functions
import time

def type_print(string, delay = 0.06):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)
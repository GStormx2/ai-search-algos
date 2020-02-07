import time
import sys

class MyTime:
    def __init__(self):
       self.complete = False
       self.second = 0
    
    def start_timer(self):
        while not self.complete:
            sys.stdout.write(f" Elapsed Time: {self.second} seconds\r ")
            self.second = self.second + 1
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rComplete!\n")
    def set_complete(val):
        self.complete = val
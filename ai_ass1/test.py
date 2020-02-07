import time
import sys
# making changes here
complete = False
second = 0
minute = 0
hour = 0
while not complete:
    sys.stdout.write(f" Elapsed Time: {second}\r ")
    second = second + 3
    sys.stdout.flush()
    time.sleep(1)    
sys.stdout.write("\rComplete!       \n")
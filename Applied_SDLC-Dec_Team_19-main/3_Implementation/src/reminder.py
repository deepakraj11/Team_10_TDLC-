import time
from src import workoutplan as w
def reminder():
    w.printf("What shall I remind you about?")
    text = str(input())
    w.printf("In how many minutes?")
    local_time = float(input())
    local_time = local_time * 60
    time.sleep(local_time)
    w.printf(text)

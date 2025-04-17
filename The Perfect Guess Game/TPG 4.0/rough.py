import time
import threading

def countdown(seconds) :
    for i in range(seconds, 0, -1):
        print(f"\rTime Remaining: {i:2}s", end="")
        #The :2 means “make sure it’s at least 2 characters wide,” so 9 becomes ' 9'.
        time.sleep(1)

    print("\nTime's up!")

timer_thread = threading.Thread(target=countdown, args=(10,))
#args() is given in iterables, if u have one arg then use (10,) not (10)--> cuz that's int not an iterable
timer_thread.start()

def greet():
    print("\nHey man")
greet_thread = threading.Thread(target=greet)
greet_thread.start()

timer_thread.join()
print("Programme ends") #So now this prints AFTER time_thread ends


import time
  
# function to countdown
def countdown(time_sec):
    
    print('Starts in:')
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        time_sec -= 1
    print("Run!!")
  

time_sec = int(input("Enter the time in seconds: "))

countdown(time_sec)
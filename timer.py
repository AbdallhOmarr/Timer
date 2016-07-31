import time
import os
import math
import winsound

clear=lambda: os.system('cls')
while True:
        
    def countdown(count):
        while count>0:
            count-=1
            print("Time remaining in mins:",math.floor(count/60),"and in secs:",count)

            time.sleep(1)
            clear()
            
            
            
    def co(abort):
        while True:
            if abort == 0 :
                count=0
            
    tmins=int(input("Enter time in mins"))
    tsecs=tmins*60

    countdown(tsecs)   
    print("Time over")
    winsound.Beep(1000,1000)

    input("New time tracking, press enter")

import time
import pygame
import msvcrt

userinput=int(input("Enter the time:"))
for i in range(userinput,0,-1):
    second=i%60
    minute=int(i/60)%60
    hour=int(i/3600)%24

    print(f"{hour:02}:{minute:02}:{second:02}",end="\r")
    time.sleep(1)

print("TIMES UP!")

import time

userinput=int(input("Enter the time:"))
for i in range(userinput,0,-1):
    print(i)
    time.sleep(1)

print("TIMES UP!")
    
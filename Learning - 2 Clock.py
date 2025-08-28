import time 
t= int(input("Enter the time: \n"))
for i in range(t,0,-1):
    s=i%60
    m=int(i/60)%60
    h=int(i/3600)%24
    day=int(i/86400)
    print(f"{day:02}:{h:02}:{m:02}:{s}")
    time.sleep(1)
else:
    print("Wrong")
print("Suprise")
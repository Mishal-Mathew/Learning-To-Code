import time 
import threading

def walking_the_dog(name):
    print("Walking the dog....")
    time.sleep(5)
    print(f"You walked {name}")

def get_mail():
    time.sleep(3)
    print("You get the mail")

def take_out_trash():
    time.sleep(2)
    print("You took the trash out")

thread1 = threading.Thread(target = walking_the_dog , args = ("Momo",))#Use 1 comma if only one argument used
thread1.start()                                                        #so as to not confuse it as string instead of tuple
thread1.join()            # Waits for the thread1 to finish

chore2 = threading.Thread(target = get_mail)
chore2.start()

chore3 = threading.Thread(target = take_out_trash)
chore3.start()
                            #join function start after the start()
chore2.join()                # Multiple join() act as one join() i.e they wait for both of the functions,I think
chore3.join()

time.sleep(1)
print("You have completed all the chores")



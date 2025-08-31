#py -m pip install pygame
import datetime
import time
import pygame

def alarm_clock(alarm_time):
    music = "Learning projects\\Claim To Fame - The Grey Room _ Clark Sims.mp3"
    running = True
    while running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)

        if current_time == alarm_time:
            running= False
            print("Wake Up!")
            pygame.mixer.init()
            pygame.mixer.music.load(music)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
        
def main():
    
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    #alarm_time = datetime.datetime.strptime(alarm_time,"%H:%M:%S").time()
    current_time=datetime.datetime.now().strftime("%H:%M:%S")

    if alarm_time.isalnum():
        print("Please enter a valid time in HH:MM:SS")

    elif alarm_time <= current_time:
        print("Alarm time should not have passed") 
    
    else:
        alarm_clock(alarm_time)



if __name__ == "__main__":
    main()
#py -m pip install pygame
import datetime
import time
import pygame

def alarm_clock(alarm_time):
    music = "Learning projects\\Claim To Fame - The Grey Room _ Clark Sims.mp3"
    running = True
    while running:
        current_time = datetime.datetime.now()
        current_time = current_time.time()
        print(current_time.strftime("%H:%M:%S"))
        time.sleep(1)

        if current_time == alarm_time:
            running = False
            print("Wake Up!")
            pygame.mixer.init()
            pygame.mixer.music.load(music)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
        
def main():

    try:
        alarm_time = input("Enter the alarm time (HH:MM:SS): ")
        alarm_time = datetime.datetime.strptime(alarm_time,"%H:%M:%S").time()
        current_time = datetime.datetime.now().time()

        if alarm_time <= current_time:
            print("The alarm time must not have passed")
        
        else:
            alarm_clock(alarm_time)
    except ValueError:
        print("Please enter a valid time")

    except Exception as e:
        print("Something went wrong",e)    


if __name__ == "__main__":
    main()
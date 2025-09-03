import datetime
import time
import pygame

def alarm_clock(alarm_time):
    music = "Testing programs\Claim To Fame - The Grey Room _ Clark Sims.mp3"
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
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    alarm_clock(alarm_time)

if __name__ == "__main__":
    main()
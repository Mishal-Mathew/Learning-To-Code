#py -m pip install pygame
import time 
import datetime
import pygame

def alarm(a_time):

    running = True
    music_path = "Rain Over Kyoto Station - The Mini Vandals.mp3"

    while running:

        c_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(c_time)
        time.sleep(1)

        if c_time == a_time:
            print("WAKE UP!")
            running= False
    
    pygame.mixer.init()
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy:
        time.sleep(1)


if __name__ == '__main__':
    
    a_time = input("Enter the time (HH:MM:SS): ")
    c_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    if a_time < c_time:
        print("Invalid time")
    
    else:
        try:
            a_time = datetime.datetime.strptime(a_time,"%H:%M:%S").time()
            alarm(a_time)
        except ValueError:
            print("Please enter a time in HH:MM:SS format")
        except exceptions:
            print("Something went wrong!")

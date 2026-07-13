# ----------------------Digital alarm clock---------------------------

# importing required libraries
import time
import datetime
import pygame

# main function
def main():

    print("\n********************* Digital Alarm **********************")
    alarm_time = input("Enter alarm time(HH:MM:SS) : ")
    print(f"Alarm is set for : {alarm_time}")
    
    sound = "alarm.mp3"
    
    while True:

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        if alarm_time == current_time:
            print("**********************************************************")
            print("Wake up!!!!")
            print("**********************************************************")

            pygame.mixer.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            break

        elif alarm_time < current_time:

            print("**********************************************************")
            print(f"Current Time : {current_time}")
            print(f"oops!!, {alarm_time} is already passed")
            print("**********************************************************")
            break

        else:
            print(current_time)
            time.sleep(1)

# Code will be exicuted only if program is directly
if __name__ == "__main__":
    main()
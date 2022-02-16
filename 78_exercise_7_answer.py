# Healthey Programmer

# 9 am - 5 pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone
# Physical activity - physical.mp3 - every 45 min - ExDone - log


from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylog.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musiconloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45*60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('water.mp3', 'drank')
            init_water = time()
            log_now("Drank water at")

        if time() - init_eyes > eyessecs:
            print("Eye Exercise time. Enter 'doneeyes' to stop the alarm.")
            musiconloop('water.mp3', 'doneeyes')
            init_eyes = time()
            log_now("Eye Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical Activity time. Enter 'donephy' to stop the alarm.")
            musiconloop('water.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical Activity at")
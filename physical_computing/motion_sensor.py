from gpiozero import MotionSensor, LED
from signal import pause
from time import sleep

pir = MotionSensor(4)
led = LED(3)
while True:
    pir.when_motion = led.on
    print("Start Moving")
    sleep(0.5)
    pir.when_no_motion = led.off
    sleep(0.5)
    pause()

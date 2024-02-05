from gpiozero import Button, LED, TrafficLights, Buzzer
from time import sleep

button = Button(2)
leds = TrafficLights(4, 22, 27)
buzzer = Buzzer(10)

while True:
    leds.blink()
    buzzer.beep()
    button.wait_for_press()
    leds.off()
    buzzer.off()
    button.wait_for_release()
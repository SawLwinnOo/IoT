from gpiozero import Button, LED, TrafficLights, Buzzer
from time import sleep

button = Button(2)
leds = TrafficLights(4, 22, 27)
buzzer = Buzzer(10)


while True:
    button.wait_for_press()
    buzzer.beep()
    leds.amber.on()
    sleep(1)
    buzzer.off()
    leds.green.on()
    sleep(1)
    leds.red.on()
    sleep(1)
    leds.off()

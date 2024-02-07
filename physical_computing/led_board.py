from gpiozero import LEDBoard
from time import sleep

leds = LEDBoard(2, 3, 17, 4, 22)

while True:
    for led in leds[3:]:  # leds 3 and onward
       led.on()
       sleep(0.2)
       leds.off()

    for led in leds[:2]:  # leds 0 and 1
       led.on()
       sleep(0.2)
       leds.off()

    for led in leds[::2]:  # even leds (0, 2, 4...)
       led.on()
       sleep(0.2)
       leds.off()

    for led in leds[1::2]:  # odd leds (1, 3, 5...)
       led.on()
       sleep(0.2)
       leds.off()
    for led in leds:
       led.on()
       sleep(0.1)
       led.off()

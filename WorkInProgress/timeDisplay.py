import time
import colorsys

#import rainbowhat


RAINBOW_BRIGHTNESS = 255
clockOn = True

'''
@rainbowhat.touch.A.press()
def touch_a(channel):
    global clockOn
    clockOn = False


def set_rainbow(temp):
    temp = max(temp, T_COLD)
    temp = min(temp, T_WARM)

    temp -= T_COLD
    temp /= float(T_WARM - T_COLD)

    hue = (1.0 - temp) * abs(HUE_WARM - HUE_COLD) / 360.0

    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]

    rainbowhat.rainbow.set_all(r, g, b, brightness=0.1)
    rainbowhat.rainbow.show()
'''

print("Let's display some numbers")

numberThing = 4

print("one", 2, "three", numberThing)

showThing = "one " + str(2) + " three " + str(numberThing)

print(showThing)

'''
while clockOn:
	temperature = rainbowhat.weather.temperature()
    set_rainbow(temperature)

    rainbowhat.display.print_float(temperature)
    rainbowhat.display.show()

    time.sleep(0.1)




rainbowhat.display.clear()
rainbowhat.display.show()
'''

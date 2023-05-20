from machine import Pin
from time import sleep
from Displays import LCDDisplay
from CompositeLights import TrafficLight

class Light:
    def __init__(self, pin, name):
        self.pin = pin
        self.name = name
        self.led = Pin(self.pin, Pin.OUT)
        self.off()  # Turn off the LED initially
    
    def on(self):
        self.led.on()
    
    def off(self):
        self.led.off()
    
    def __str__(self):
        return f"{self.name} (Pin {self.pin})"

# Create instances of the lights connected to GPIO pins
red_led = Light(0, "Red LED")
yellow_led = Light(1, "Yellow LED")
green_led = Light(2, "Green LED")

# Create an instance of the traffic light with the LED instances
traffic_light = TrafficLight(red_led, yellow_led, green_led)

# Create an instance of the LCD display
display = LCDDisplay(sda=20, scl=21, i2cid=0)

# Function to display text on the LCD display
def display_text():
    if red_led.led.value() == 1:
        display.showText("Stop")
    elif yellow_led.led.value() == 1:
        display.showText("Caution")
    elif green_led.led.value() == 1:
        display.showText("Go")
    else:
        display.showText("")

# Traffic light sequence
red_led.on()
display_text()
sleep(2)

red_led.off()
display_text()
sleep(2)

yellow_led.on()
display_text()
sleep(2)

yellow_led.off()
display_text()
sleep(2)

green_led.on()
display_text()
sleep(2)

green_led.off()
display_text()

# Clear the display
display.showText("")









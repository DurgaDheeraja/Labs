from machine import Pin
from time import sleep
from Displays import LCDDisplay
from Button import Button

class PedestrianCrossing:
    def __init__(self):
        self.button_pin = 25  # GPIO pin connected to the button
        self.pull_type = Pin.PULL_DOWN  # Specify the pull type
        self.display_sda = 20  # I2C SDA pin connected to the display
        self.display_scl = 21  # I2C SCL pin connected to the display
        self.button = Button(self.button_pin, self.pull_type, buttonhandler=self)
        self.display = LCDDisplay(sda=self.display_sda, scl=self.display_scl)
        self.button_pressed = False

    def run(self):
        while True:
            if self.button_pressed:
                self.display.showText("DONT WAIT")
            else:
                self.display.showText("WAIT")
            
            # Sleep for a short interval
            sleep(0.1)
    
    def buttonPressed(self, name):
        if name == self.button.getName():
            self.button_pressed = True

    def buttonReleased(self, name):
        if name == self.button.getName():
            self.button_pressed = False

if __name__ == "__main__":
    crossing = PedestrianCrossing()
    crossing.run()


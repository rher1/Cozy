import RPi.GPIO as GPIO
import time
import board
import busio
import digitalio
import adafruit_max31855
from sys import exit

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

def heating():
    GPIO.output(17, False)
    GPIO.output(27, True)
    GPIO.output(22, False)
    GPIO.output(23, True)
    GPIO.output(6, False)
    GPIO.output(13, True)
    GPIO.output(19, False)
    GPIO.output(26, True)
    GPIO.output(16, False)
    print("Now Heating...")

def cooling():
    GPIO.output(17, True)
    GPIO.output(27, False)
    GPIO.output(22, True)
    GPIO.output(23, False)
    GPIO.output(6, True)
    GPIO.output(13, False)
    GPIO.output(19, True)
    GPIO.output(26, False)
    GPIO.output(16, True)
    print("Now Cooling...")

# User Input
desired_temp = int(input("Enter your desired temperature: "))

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)

max31855=adafruit_max31855.MAX31855(spi, cs)

try:
    while True:
        tempC = max31855.temperature
        tempF = tempC * 9 / 5 + 32
        print('Temperature: {} C {} F '.format(tempC, tempF)
        time.sleep(0.05)
        if tempF <= desired_temp:
            heating()
        else:
            cooling()
finally:
    GPIO.cleanup()
    exit()

import RPi.GPIO as GPIO
import time
import board
import busio
import digitalio
import adafruit_max31855
from sys import exit

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

def heating():
    GPIO.output(11, False)
    GPIO.output(13, True)
    GPIO.output(15, False)
    GPIO.output(16, True)
    GPIO.output(31, False)
    GPIO.output(33, True)
    GPIO.output(35, False)
    GPIO.output(37, True)
    GPIO.output(36, True)
    print("Now Heating...")

def cooling():
    GPIO.output(11, True)
    GPIO.output(13, False)
    GPIO.output(15, True)
    GPIO.output(16, False)
    GPIO.output(31, True)
    GPIO.output(33, False)
    GPIO.output(35, True)
    GPIO.output(37, False)
    GPIO.output(36, False)
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
        print('Temperature: {} C {} F '.format(tempC, tempF))
        time.sleep(0.05)
        if tempF <= desired_temp:
            heating()
        else:
            cooling()
finally:
    GPIO.cleanup()
    exit()

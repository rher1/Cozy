import RPi.GPIO as gpio
import time
import board
import busio
import digitalio
import adafruit_max31855

def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(0, GPIO.OUT)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(25, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)

def heating():
    init()
    GPIO.output(0, False)
    GPIO.output(2, True)
    GPIO.output(3, False)
    GPIO.output(4, True)
    GPIO.output(22, False)
    GPIO.output(23, True)
    GPIO.output(24, False)
    GPIO.output(25, True)
    GPIO.output(27, True)
    GPIO.cleanup()


def cooling():
    init()
    GPIO.output(0, True)
    GPIO.output(2, False)
    GPIO.output(3, True)
    GPIO.output(4, False)
    GPIO.output(22, True)
    GPIO.output(23, False)
    GPIO.output(24, True)
    GPIO.output(25, False)
    GPIO.output(27, False)
    GPIO.cleanup()

spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)

max31855=adafruit_max31855.MAX31855(spi, cs)

while True:
    tempC = max31855.temperature
    tempF = tempC * 9 / 5 + 32
    print('Temperature: {} c {} F '.format(tempC, tempF))
    time.sleep(0.05)
    if tempF <= desired_temp:
        heating()
    else:
        cooling()
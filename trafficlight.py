
# pi@DietPi-1:~ $ cat trafficlight.py
import RPi.GPIO as GPIO
import sys

if sys.argv[1] in ['red','Red','RED','r','R']:
    color = 9
elif sys.argv[1] in ['yellow','Yellow','y','Y','YELLOW']:
    color = 10
elif sys.argv[1] in ['green','Green','g','G','GREEN']:
    color = 11

# Reset all the pins to LOW
GPIO.setmode(GPIO.BCM)
GPIO.setup(9,GPIO.OUT)
GPIO.output(9, False)
GPIO.setup(10,GPIO.OUT)
GPIO.output(10,False)
GPIO.setup(11,GPIO.OUT)
GPIO.output(11,False)

#Pin Setup
GPIO.setmode(GPIO.BCM) #Brodcom pin-numbering scheme.
GPIO.setup(color, GPIO.OUT) # Red LED pin set as output.
# Set Pin High

if sys.argv[2] in ['True','true','t','T','TRUE','1']:
    GPIO.output(color, True)
else:
    GPIO.output(color, False)


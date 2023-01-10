#Librerie
import RPi.GPIO as GPIO
from time import sleep

#SetMode

GPIO.setmode(GPIO.BOARD)

#Motore 1
PWR1=2
ENA1=33
IN1=31
IN2=29
GND=39
GPIO.setup(ENA1, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
PMWA = GPIO.PMW(ENA1,100)
PMWA.start(0)
#Motore 2
PWR2=2
ENA2=32
IN3=18
IN4=16
GND=34
GPIO.setup(ENA2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
PMWB = GPIO.PMW(ENA2,100)
PMWB.start(0)

#Motor 1 va
PWMA.ChangeDutyCycle(30)
sleep(5)
GPIO.output(IN1,GPIO.HIGH)
sleep(5)
GPIO.output(IN2,GPIO.LOW)

#Motor 2 va
PWMB.ChangeDutyCycle(30)
sleep(5)
GPIO.output(IN3,GPIO.LOW)
sleep(5)
GPIO.output(IN4,GPIO.HIGH)

GPIO.cleanup()
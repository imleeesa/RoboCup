import RPi.GPIO as GPIO

class pinocchio_wheels:
    def __init__(self, ENA, IN1, IN2, ENB, IN3, IN4):
        self.ENA = ENA
        self.IN1 = IN1
        self.IN2 = IN2
        self.ENB = ENB
        self.IN3 = IN3
        self.IN4 = IN4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(self.ENA, GPIO.OUT)
GPIO.setup(self.IN1, GPIO.OUT)
GPIO.setup(self.IN2, GPIO.OUT)
PWMA = GPIO.PWM(self.ENA ,100)

GPIO.setup(self.ENB, GPIO.OUT)
GPIO.setup(self.IN3, GPIO.OUT)
GPIO.setup(self.IN4, GPIO.OUT)
PWMB = GPIO.PWM(self.ENA ,100)

def go():
    PWMA.ChangeDutyCycle(100)
    GPIO.output(self.IN1,GPIO.HIGH)
    GPIO.output(self.IN2,GPIO.LOW)

    PWMB.ChangeDutyCycle(100)
    GPIO.output(self.IN3,GPIO.HIGH)
    GPIO.output(self.IN4,GPIO.LOW)

    pass

def stop():
    PWMA.ChangeDutyCycle(0)
    GPIO.output(self.IN1,GPIO.LOW)
    GPIO.output(self.IN2,GPIO.LOW)

    PWMB.ChangeDutyCycle(0)
    GPIO.output(self.IN3,GPIO.LOW)
    GPIO.output(self.IN4,GPIO.LOW)

    pass

def backwards():
    PWMA.ChangeDutyCycle(100)
    GPIO.output(self.IN1,GPIO.LOW)
    GPIO.output(self.IN2,GPIO.HIGH)

    PWMB.ChangeDutyCycle(100)
    GPIO.output(self.IN3,GPIO.LOW)
    GPIO.output(self.IN4,GPIO.HIGH)    

    pass

def right():
    PWMA.ChangeDutyCycle(0)
    GPIO.output(self.IN1,GPIO.LOW)
    GPIO.output(self.IN2,GPIO.LOW)

    PWMB.ChangeDutyCycle(100)
    GPIO.output(self.IN3,GPIO.LOW)
    GPIO.output(self.IN4,GPIO.HIGH)    

    pass

def left():
    PWMA.ChangeDutyCycle(100)
    GPIO.output(self.IN1,GPIO.LOW)
    GPIO.output(self.IN2,GPIO.HIGH)

    PWMB.ChangeDutyCycle(0)
    GPIO.output(self.IN3,GPIO.LOW)
    GPIO.output(self.IN4,GPIO.LOW)    

    pass
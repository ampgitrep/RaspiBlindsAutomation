import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import pytz

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)
pwm=GPIO.PWM(8, 20)


tz_LA = pytz.timezone('America/Los_Angeles')
now = datetime.now(tz_LA)
current_time = now.strftime("%H:%M:%S")

def new_angle(angle):
    duty = (angle / 18) + 2
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    pwm.ChangeDutyCycle(0)

def move_motors(angle):
  pwm.start(0)
  GPIO.output(8, True)
  new_angle(angle)
  GPIO.output(8, False)
  pwm.stop()
  GPIO.cleanup()
  
def move_motors_up():
  move_motors(90)
  
def move_motors_down():
  move_motors(10)
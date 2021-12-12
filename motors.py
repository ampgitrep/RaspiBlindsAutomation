import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import pytz



tz_LA = pytz.timezone('America/Los_Angeles')
now = datetime.now(tz_LA)
current_time = now.strftime("%H:%M:%S")

def move_motors_up():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(8, GPIO.OUT)
  pwm=GPIO.PWM(8, 20)
  pwm.start(0)
  def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(8, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(8, False)
    pwm.ChangeDutyCycle(0)
  SetAngle(90)
  pwm.stop()
  GPIO.cleanup()
  
def move_motors_down():
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(8, GPIO.OUT)
  pwm=GPIO.PWM(8, 20)
  pwm.start(0)
  def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(8, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(8, False)
    pwm.ChangeDutyCycle(0)
  SetAngle(10)
  pwm.stop()
  GPIO.cleanup()
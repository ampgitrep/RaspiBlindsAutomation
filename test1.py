import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import pytz


def move_motors():
  GPIO.setmode(GPIO.BOARD)
  sleep(2)
  print("get ready to blast off")
  tz_LA = pytz.timezone('America/Los_Angeles')
  now = datetime.now(tz_LA)
  current_time = now.strftime("%H:%M:%S")

  print(current_time)
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

  def moveMotor():
    SetAngle(90)
    SetAngle(10)
    SetAngle(90)
    SetAngle(10)
    SetAngle(90)
    SetAngle(10)
    SetAngle(90)
    SetAngle(10)
    SetAngle(90)
    SetAngle(10)
    SetAngle(90)
    SetAngle(10)
  moveMotor()
  pwm.stop()
  GPIO.cleanup()

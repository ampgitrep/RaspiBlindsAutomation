import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
print("please enter your name")
name = input()
print("hello",name)
sleep(2)
print("get ready to blast off")

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
pwm.stop()
GPIO.cleanup()

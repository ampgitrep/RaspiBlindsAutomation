import RPi.GPIO as GPIO
import time

def read_sensor():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(10, GPIO.IN)         #Read output from PIR motion sensor
  while True:
    i=GPIO.input(10)
    time.sleep(0.3)
    if i==1:               #When output from motion sensor is HIGH
      print("motion detected")
      time.sleep(3)
  return i

    
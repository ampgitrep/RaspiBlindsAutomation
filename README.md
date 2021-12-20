# RaspiBlindsAutomation
python script to control the blinds with raspberry pi

## Purpose
 - The purpose of this project is to automate my living room blinds to rise during daylight hours and shut during the night. 
 
 ### Tools used to bulid this project
  - A simple HTTP server is run on a Raspberry pi 2 through Python
  - Python is used to interface with the GPIO pins on the raspberry pi which control the motors, and will read the sensors (sensors tell us when to stop running motors)
  - HTML for the webpage
  - Bulma CSS for stylization
  - 5v hobby servo motor
#### Instructions
 - The first thing you need to do is mount a servo motor with the arm attached to the draw strings of a set of venetian blinds. When activated, the servo motor will pull the cord to open and close the blinds.
 - install the latest version of Raspian (or raspbian lite for headless pi) on your rpi. https://www.raspbian.org/
 - Once installed, make sure everything is up to date.
 - SSH into your raspberry pi 
 - Most standard servo motors have three wires - a brown, a red, and an orange.
 - the brown wire is ground, red is 5v, and orange is pwm signal.
 - on your raspberry pi, enter pinout into the command line to see what GPIO pins are free.
 - for my project I chose pin 8 for signal, and a 5v and gnd line close by. Just be sure that you properly connect the red wire to a 5v line and the brown wire to a ground line or you could damage the motor and the pi. which ever pin you choose for your signal, be sure to go into motors.py and change the 8 in: 

GPIO.setup(8, GPIO.OUT)
pwm=GPIO.PWM(8, 20)

to whatever pin you choose.
- download the code and cd into the directory of the download. 
-enter python3 simple-server.py in the command line to start the server
- go yourpislocalip:8000 on your browser and there you have it! from your browser you can control the blinds!

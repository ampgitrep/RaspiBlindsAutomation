import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
import pytz





class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        query_components = parse_qs(urlparse(self.path).query) 
        next_name = 0
        if 'increment' in query_components:
         next_name = next(myiter)
        elif 'move_motors_up' in query_components:
          move_motors_up()
        elif 'move_motors_down' in query_components:
          move_motors_down() 
        html = f"<html><head></head><body> <form method=get action=?increment>Hello {list[next_name]} <input type=hidden name=increment value=true><input type=submit value=Increment></input></form> <form method=get action=?move_motors_up>Move blinds up! <input type=hidden name=move_motors_up value=true><input type=submit value=up></input></form> <form method=get action=?move_motors_down>Move blinds down! <input type=hidden name=move_motors_down value=true><input type=submit value=down></input></form></body></html>"
        self.wfile.write(bytes(html, "utf8"))
          
        
        return 
list = ["alex", "phoenix", "jack", "lucy"]

tz_LA = pytz.timezone('America/Los_Angeles')
now = datetime.now(tz_LA)
current_time = now.strftime("%H:%M:%S")

class increment_index():
  def __iter__(self):
    self.index = 0
    return self
  
  def __next__(self):
    next_index = self.index
    if next_index < len(list):
      self.index += 1
    else:
      self.index = 0
      next_index = self.index
    return next_index
myclass = increment_index()
myiter = iter(myclass)

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
# Create an object of the above class

handler_object = MyHttpRequestHandler

PORT = 8001

my_server = socketserver.TCPServer(("", PORT), handler_object)

# Start the server
my_server.serve_forever()
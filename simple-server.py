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
        if self.path == '/':
          self.path = 'webpage.html'
          return http.server.SimpleHTTPRequestHandler.do_GET(self)
                
        query_components = parse_qs(urlparse(self.path).query) 
        
        if 'move_motors_up' in query_components:
          move_motors_up()
          self.path = 'webpage.html'
          return http.server.SimpleHTTPRequestHandler.do_GET(self)
        elif 'move_motors_down' in query_components:
          move_motors_down()
          self.path = 'webpage.html'
          return http.server.SimpleHTTPRequestHandler.do_GET(self)
  
        html = f"<html><head></head><body><form method=get action=?move_motors_up>Move blinds up! <input type=hidden name=move_motors_up value=true><input type=submit value=up></input></form><form method=get action=?move_motors_down>Move blinds down! <input type=hidden name=move_motors_down value=true><input type=submit value=down></input></form></body></html>"
        self.wfile.write(bytes(html, "utf8"))
          
        return 


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
# Create an object of the above class

handler_object = MyHttpRequestHandler

PORT = 8001

my_server = socketserver.TCPServer(("", PORT), handler_object)

# Start the server
my_server.serve_forever()
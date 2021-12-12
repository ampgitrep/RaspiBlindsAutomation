import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs
import motors
import sensors

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        if self.path == '/':
          self.path = 'webpage.html'
          return http.server.SimpleHTTPRequestHandler.do_GET(self)                
        query_components = parse_qs(urlparse(self.path).query) 
        
        if sensors.read_sensor == 1:
          print("sensors read")
          
        if 'move_motors_up' in query_components:
          motors.move_motors_up()
          self.path = 'webpage.html'
          return http.server.SimpleHTTPRequestHandler.do_GET(self)
        elif 'move_motors_down' in query_components:
          motors.move_motors_down()
          self.path = 'webpage.html'
          return http.server.SimpleHTTPRequestHandler.do_GET(self)
  
        
          
        return 


# Create an object of the above class

handler_object = MyHttpRequestHandler

PORT = 8000

my_server = socketserver.TCPServer(("", PORT), handler_object)

# Start the server
my_server.serve_forever()
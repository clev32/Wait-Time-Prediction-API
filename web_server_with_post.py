#!/usr/bin/python
#create an API for Jetblue to add to their website to calculate wait times
from http.server import BaseHTTPRequestHandler,HTTPServer
from jetblue3 import jet_blue_lines
import json


#BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
	#get flight information from postman
	#send the information to the jet_blue_lines function to calculate the wait times
	#return the calculations as a json dictionary to be incorporated into Jetblue's website 
	def do_POST(self):
		
		content_len = int(self.headers.get('Content-Length'))
		post_body = json.loads(self.rfile.read(content_len).decode("utf-8"))
		response = jet_blue_lines(post_body["num_flights"],post_body["flight_occupancy"],post_body["kiosk_check_in"],post_body["luggage_check_in"],post_body["tsa"],post_body["non_luggage"])
		result = (json.dumps(response))
		print(result)
		self._set_headers()
		self.wfile.write(result.encode('utf-8'))
		

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print ('Started httpserver on port ') , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()


except KeyboardInterrupt:
	print ('^C received, shutting down the web server')
	server.socket.close()



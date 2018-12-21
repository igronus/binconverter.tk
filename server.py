#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
#import cgi
import urlparse
from bitstring import BitArray

PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()

		# Send the html message
		#self.wfile.write("Hello World !")

		# form = cgi.FieldStorage()
		o = urlparse.urlparse(self.path)
		form = urlparse.parse_qs(o.query)
		#self.wfile.write(form.getvalue("foo"))

		
		key1 = 'bin'
		key2 = 'type'
		if key1 in form and key2 in form:
			#BitArray(bin=form[key1][0]).int
			#self.wfile.write(form[key1][0])
			# self.wfile.write(BitArray(bin=form[key1][0]).uint)
			#self.wfile.write(BitArray(bin=form[key1][0]).{form[key2][0]})
			self.wfile.write(getattr(BitArray(bin=form[key1][0]), form[key2][0]))
		else:
			self.wfile.write('syntax: /?bin=1001&type=uint')

		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming http requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()

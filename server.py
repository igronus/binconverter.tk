#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urlparse
from bitstring import BitArray
import re

PORT_NUMBER = 8080


#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()

		o = urlparse.urlparse(self.path)
		form = urlparse.parse_qs(o.query)
		
		key1 = 'bin'
		key2 = 'type'
		if key1 in form and key2 in form:
			binary_number = form[key1][0]
			binary_type = form[key2][0]

			# TODO
			# re.match(r"^(0|1)+$", binary_number)

			try:
				result = getattr(BitArray(bin=binary_number), binary_type)
			except Exception, e:
				self.wfile.write(str(e))
			else:
				self.wfile.write(result)
		else:
			syntax_msg = "Syntax: /?bin=(1|0)+&type=(float|int|uint)"
			self.wfile.write(syntax_msg)

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

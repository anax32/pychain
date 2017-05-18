from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
import threading
import json
import re

HOSTNAME = "localhost"
PORT = 8080

class RESTHandler (BaseHTTPRequestHandler):
  def do_HEAD (self):
    self.send_response (200)
    self.send_header ("Content-type", "text/html")
    self.end_headers ()

  def do_GET (self):
    for c in self.server.callbacks:
      req_type = c.request_type
      req_path = c.request_path

      if re.match (req_type, "GET") != None and re.match (req_path, self.path) != None:
        self.send_response (200)
        self.send_header ("Content-type", "application/json")
        self.end_headers ()
        self.wfile.write (c ())
        return

    self.send_response (404)
    self.end_headers ()

class RESTServer (HTTPServer):
  def __init__ (self, conn_settings, req_handler, callbacks):
    HTTPServer.__init__ (self, conn_settings, req_handler)
    self.callbacks = callbacks

class RESTController ():
  def run (self, callbacks):
    httpd = RESTServer ((HOSTNAME, PORT), RESTHandler, callbacks)

    print ("starting server at " + HOSTNAME + ":" + str (PORT))

    try:
      httpd.serve_forever ()
    except KeyboardInterrupt:
      pass

    httpd.server_close ()

    print ("server stop")


# decorator definitions
def request_type (arg):
  def ret_fn (fn):
    fn.request_type = arg
    return fn
  return ret_fn

def request_path (arg):
  def ret_fn (fn):
    fn.request_path = arg
    return fn
  return ret_fn

# request callbacks
@request_type(".")
@request_path("^/$")
def server_status ():
  # return a list of possible queries
  return json.dumps ({"/blocks": "list of blocks"})

@request_type("GET")
@request_path("/blocks")
def request_blocks ():
  blks = {"blocks": [{"block":1,"id":10}]}
  return json.dumps (blks)

# entry point
if __name__ == "__main__":
  r = RESTController ()

  r.run ([server_status, request_blocks])

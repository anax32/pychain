import nose
from nose.tools import *

from multiprocessing import Process
import requests

from conn import RESTController, server_status, request_blocks

SERVER = "http://localhost:8080"

class Conn_Tests:
  @classmethod
  def setup_class (cls):
    cls.server = RESTController ()
    cls.process = Process (target = cls.server.run, args = ([server_status, request_blocks], ))
    cls.process.start ()

  @classmethod
  def teardown_class (cls):
    cls.process.terminate ()
    cls.process.join ()

  def test_server_created (self):
    assert_true (self.__class__.process.is_alive ())

  def test_server_get_root (self):
    r = requests.get (SERVER)
    assert_equal (r.status_code, 200)

  def test_server_get_root_json (self):
    r = requests.get (SERVER)
    j = r.json ()
    assert_equal (len (j), 1)
    assert_true ("/blocks" in j)

  def test_server_get_blocks (self):
    r = requests.get (SERVER + "/blocks")
    assert_true (r.status_code, 200)

  def test_server_get_blocks (self):
    r = requests.get (SERVER + "/blocks")
    j = r.json ()
    assert_equal (len (j), 1)
    assert_true ("blocks" in j)
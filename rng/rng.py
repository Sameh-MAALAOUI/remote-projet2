from flask import Flask, Response
import os
import socket
import time

app = Flask(__name__)
hostname = socket.gethostname()
urandom = os.open("/dev/urandom", os.O_RDONLY)

@app.route("/")
def index():
  return "RNG running on {}\n".format(hostname)

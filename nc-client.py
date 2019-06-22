# Netcat replacement

import socket
import sys
import getopt
import threading
import subprocess

# Define global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

# Show usage of the function if arguments are not provided
def usage():
  print("BHP Net Tool")
  print("")
  print("Usage: nc-client.py -t target_host -p port")
  print("-l --listen    - listen on [host]:[port] for incoming connection")
  print("-e --execute=file-to-run   - execute the given file upon receiving a connection")

  sys.exit(0)

def main():
  global listen
  global port
  global execute
  global command
  global upload_destination
  global target

  if not len(sys.argv[1:]):
    usage()

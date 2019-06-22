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

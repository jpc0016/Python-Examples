#!/usr/bin/python3
import sys
from time import sleep

try:
  print("\n\nSending good vibes to " + sys.argv[1] + "\n")
  
  for i in range (0,20):
    
    sys.stdout.write("[" + i*"=" + (19-i)*" " + "> \r" )
    sys.stdout.flush()
    sleep(1)
    #print("[" + i*"=" + (19-i)*" " + ">")
    
  print("\n\nGood vibes sent!  \o/")
  
except:
  print("\n\nWho do I send these good vibes to..... :( \n")



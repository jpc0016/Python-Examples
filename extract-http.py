#!/usr/bin/env/python

###############################################
# Extracts data from HTTP packets
###############################################

# dpkt currently supports Python 2.7 only
import sys
import socket
import dpkt
import datetime


# Open pcap specified in command line
f = open(sys.argv[1], "r")
pcap = dpkt.pcap.Reader(f)

# File with HTTP output
new = "contents-http.txt"


with open(new, "w") as new_file:
        for ts, buf in pcap:
            eth = dpkt.ethernet.Ethernet(buf)

            ip = eth.data
            tcp = ip.data

            # Examine HTTP content
            if tcp.dport == 80 and len(tcp.data) > 0:
                # display source and destination IP addresses
                new_file.write("Source IP: " + socket.inet_ntoa(ip.src) + "\n")
                new_file.write("Destination IP: " + socket.inet_ntoa(ip.dst) + "\n")
                http = dpkt.http.Request(tcp.data)
                # extract HTTP fields
                new_file.write("Method: " + http.method + "\n")
                if http.uri > 0:
                    new_file.write("URI: " + http.uri + "\n")
                new_file.write("Version: " + http.version + "\n")
                #new_file.write("User-Agent" + http.headers['user-agent'] + "\n")
                new_file.write("\n\n")

            # Extract HTTP Response information
            if tcp.sport == 80 and len(tcp.data) > 0:
                # display source and destination IP addresses
                new_file.write("Source IP: " + socket.inet_ntoa(ip.src) + "\n")
                new_file.write("Destination IP: " + socket.inet_ntoa(ip.dst) + "\n")
                #response = dpkt.http.Response(tcp.data)
                # extract fields
                #new_file.write("Version: " + response.version + "\n")
                #new_file.write("Status: " + response.status + "\n")
                #new_file.write("Reason: " + response.reason + "\n")
                new_file.write("\n\n")


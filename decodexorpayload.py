#!/usr/bin/python

from scapy.all import *
import sys

# Get input and output files from command line
if len(sys.argv) < 2:
        print "Usage: decodexorpayload.py [input pcap file]"
        sys.exit(1)

# Assign variable names for input and output files
infile = sys.argv[1]

def many_byte_xor(buf, key):
    buf = bytearray(buf)
    key = bytearray(key)
    key_len = len(key)
    for i, bufbyte in enumerate(buf):
        buf[i] = bufbyte ^ key[i % key_len]
    return str(buf)

def process_packets():
    pkts = rdpcap(infile)
    cooked=[]
    for p in pkts:
        # You may have to adjust the payload depth here:
        # i.e. p.payload.payload.payload
        pkt_payload = str(p.payload.payload)
        pkt_offset = str(p.payload.payload)[:3]
	pkt_header = str(p)[:40]
        if pkt_payload and pkt_offset:
              pmod=p
              # You may have to adjust the payload depth here:
              # p.payload.payload=many_byte_xor(pkt_payload, pkt_offset)
              # temp = str(p.payload.payload)
              temp = many_byte_xor(pkt_payload, pkt_offset)
              temp1 = pkt_header + temp
              pmod = bytearray(temp1)
              cooked.append(pmod)

    wrpcap("dump.pcap", cooked)

process_packets()

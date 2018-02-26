from collections import defaultdict
import argparse

senders = defaultdict(int)

def processLine(line):
    if (line.startswith("From: ")):
        # Remove "From: " from the beginning of the string
        senderOnly = line[6:]
        # Strip newlines 
        senderEmail = senderOnly.strip()

        senders[senderEmail] += 1

with open(r"C:\Users\Brian\Downloads\takeout-20180225T203630Z-001 (1)\Takeout\Mail\inbox.mbox", encoding="utf8") as mboxFile:
    for line in mboxFile:
        processLine(line)
    
    total = 0
    for sender, count in senders.items():
        total += count 

        if (count > 10):
            print ((str(sender) + " - " + str(count)).encode("utf8"))

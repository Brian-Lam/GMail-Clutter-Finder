"""
MBox-Reader

This Python script analyzes an mbox file, exported from GMail, to find
your most common email senders. I wrote this to clear out my GMail storage
space as it was hitting 50%. 

Brian Lam
"""

from collections import defaultdict
import argparse

# Defaultdict to store sender data and count of emails
senders = defaultdict(int)

# Set up command line arguments
argParser = argparse.ArgumentParser()
argParser.add_argument("filepath", type=str, help="Location of mbox file")
argParser.add_argument("n", type=int, nargs="?", default=10, help="The amount of emails"
    "that need to be received from a sender for them to be display in results")

args = argParser.parse_args()

# Retrieve command line arguments from parser
mboxFilePath = args.filepath
resultCutoff = args.n

def processLine(line):
    if (line.startswith("From: ")):
        # Remove "From: " from the beginning of the string
        senderOnly = line[6:]
        # Strip newlines 
        senderEmail = senderOnly.strip()
        # Increment count for this sender
        senders[senderEmail] += 1

with open(mboxFilePath, encoding="utf8") as mboxFile:
    for line in mboxFile:
        processLine(line)
    
    total = 0
    for sender, count in senders.items():
        total += count 

        if (count > resultCutoff):
            print ((str(sender) + " - " + str(count)))

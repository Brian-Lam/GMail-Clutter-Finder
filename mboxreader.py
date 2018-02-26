"""
MBox-Reader

This Python script analyzes an mbox file, exported from GMail, to find
your most common email senders. I wrote this to clear out my GMail storage
space as it was hitting 50%, deleting promotional email newsletters.

Brian Lam
"""

from collections import defaultdict
import argparse
import heapq

# Defaultdict to store sender data and count of emails
senders = defaultdict(int)

# Store most common senders in a max heap for quick retrieval. To ease
# the burden of the n*lg(n) total insertion time, only senders with counts
# greater than the cutoff will be inserted.
resultHeap = []

# Set up command line arguments
argParser = argparse.ArgumentParser()
argParser.add_argument("filepath", type=str, help="Location of mbox file")
argParser.add_argument("n", type=int, nargs="?", default=10, help="The amount of emails"
    "that need to be received from a sender for them to be display in results")

# Retrieve command line arguments from parser
args = argParser.parse_args()
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

def processSender(sender, count):
    # Add sender to results list if they are above the count cutoff
    if (count > resultCutoff):
        resultHeap.append((count, sender))

def processResults():
    # Iterate through the senders list
    for sender, count in senders.items():
        if (count > resultCutoff):
            processSender(sender, count)
    
    # Max heapify the list
    heapq._heapify_max(resultHeap)

def outputResults():
    # Pop results from maxheap, showing most popular sender first
    while len(resultHeap) > 0:
        count, sender = heapq._heappop_max(resultHeap)
        print(sender + " - " + str(count))

with open(mboxFilePath, encoding="utf8") as mboxFile:
    # Process each line in the mbox file. An mbox file can be large, but the
    # "for x in container" pattern will allow us to iterate over the file
    # without storing the entire file in memory.
    for line in mboxFile:
        processLine(line)
    
    processResults()
    outputResults()
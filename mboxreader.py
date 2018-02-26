"""
MBox-Reader

This Python script analyzes an mbox file, exported from GMail, to find
your most common email senders. I wrote this to clear out my GMail storage
space as it was hitting 50%, deleting promotional email newsletters.

Brian Lam
"""

from collections import defaultdict
from tkinter import *
from tkinter import ttk
import heapq

# Defaultdict to store sender data and count of emails
senders = defaultdict(int)

# Store most common senders in a max heap for quick retrieval. To ease
# the burden of the n*lg(n) total insertion time, only senders with counts
# greater than the cutoff will be inserted.
resultHeap = []


# Retrieve command line arguments from parser
mboxFilePath = ""
resultCutoff = 50

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
        # # print(sender + " - " + str(count))

"""
GUI Initialization 
"""
root = Tk()
root.title("GMail Clutter Finder")

content = ttk.Frame(root)
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

directionsLabel = ttk.Label(content, text="Here are some directions. TODO")
fileLabel = ttk.Label(content, text="mbox file path:")

content.grid(column=0, row=0)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

filePath = StringVar()
root.mainloop()

# # with open(mboxFilePath, encoding="utf8") as mboxFile:
# #     # Process each line in the mbox file. An mbox file can be large, but the
# #     # "for x in container" pattern will allow us to iterate over the file
# #     # without storing the entire file in memory.
# #     for line in mboxFile:
# #         processLine(line)
    
# #     processResults()
# #     outputResults()


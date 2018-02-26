"""
MBox-Reader

This Python script analyzes an mbox file, exported from GMail, to find
your most common email senders. I wrote this to clear out my GMail storage
space as it was hitting 50%, deleting promotional email newsletters.

Brian Lam
"""

from collections import defaultdict
import os.path
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import heapq
import webbrowser

class MBoxReader():
    def __init__(self):
        # Defaultdict to store sender data and count of emails
        self.senders = defaultdict(int)

        # Store most common senders in a max heap for quick retrieval. To ease
        # the burden of the n*lg(n) total insertion time, only senders with counts
        # greater than the cutoff will be inserted.
        self.resultHeap = []


        # Retrieve command line arguments from parser
        self.mboxFilePath = ""
        self.resultCutoff = 50

        self.initializeGraphicalUserInterface()

    def processLine(self, line):
        if (line.startswith("From: ")):
            # Remove "From: " from the beginning of the string
            senderOnly = line[6:]
            # Strip newlines 
            senderEmail = senderOnly.strip()
            # Increment count for this sender
            self.senders[senderEmail] += 1

    def processSender(self, sender, count):
        # Add sender to results list if they are above the count cutoff
        if (count > self.resultCutoff):
            self.resultHeap.append((count, sender))

    def processResults(self):
        # Iterate through the senders list
        for sender, count in self.senders.items():
            self.processSender(sender, count)
        
        # Max heapify the list
        heapq._heapify_max(self.resultHeap)

    def outputResults(self):
        self.step1Label.grid_remove()
        self.step2Label.grid_remove()
        self.fileButton.grid_remove()

        step4Label = ttk.Label(self.content, text="Results", cursor="hand2", wraplength=350)
        step4Label.grid(column=0, row=0, columnspan=3, rowspan=2, padx=5, pady=5)

        resultsText = Text(self.content, width=60, height=30)
        resultsText.grid(column=0, row=1, columnspan=3, rowspan=2, padx=5, pady=5)
        

        # Pop results from maxheap, showing most popular sender first
        while len(self.resultHeap) > 0:
            count, sender = heapq._heappop_max(self.resultHeap)
            senderEmail = sender[sender.find("<")+len("<"):sender.rfind(">")]
            resultsText.insert(END, senderEmail + " - " + str(count) + "\n")


    # Process the mbox file if it exists
    def readFile(self):
        if not os.path.isfile(self.mboxFilePath):
            return

        with open(self.mboxFilePath, encoding="utf8") as mboxFile:
            # Process each line in the mbox file. An mbox file can be large, but the
            # "for x in container" pattern will allow us to iterate over the file
            # without storing the entire file in memory.
            for line in mboxFile:
                self.processLine(line)
            
            self.processResults()
            self.outputResults()

    # Open the web browser to download mbox file
    def openBrowserToDownloadMbox(self, event):
        webbrowser.open_new("https://takeout.google.com/settings/takeout")
        

    """
    GUI Setup
    """
    # Setup file browser
    def browseMboxPath(self):
        Tk().withdraw() 
        global mboxFilePath
        self.mboxFilePath = filedialog.askopenfilename(initialdir="/",title="Select MBox file", filetypes=[("Mailbox Archive","*.mbox")])
        self.readFile()

    # GUI Initialization
    def initializeGraphicalUserInterface(self):
        root = Tk()
        root.title("GMail Clutter Finder")
            
        #Setup frame
        self.content = ttk.Frame(root)
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(0, weight=1)

        # Setup widgets
        self.step1Label = ttk.Label(self.content, text="Step 1: Click here to download your GMail inbox (.mbox)", cursor="hand2", wraplength=350)
        self.step1Label.pack()
        self.step1Label.bind("<Button-1>", self.openBrowserToDownloadMbox)

        self.step2Label = ttk.Label(self.content, text="Step 2: Got your mbox file? Cool, let's find it. It's in that zip file you got, under Takeout\Mail.", \
            wraplength=350)
        self.fileButton= Button(root, text="Find your .mbox file", command=self.browseMboxPath)

        # Place widgets
        self.content.grid(column=0, row=0)

        self.step1Label.grid(column=0, row=0, padx=5, pady=5)

        self.step2Label.grid(column=0, row=5, padx=5, pady=5)
        self.fileButton.grid(column=0, row=7)

        root.mainloop()

"""
Program start
"""
if __name__=="__main__":
    MBoxReader()
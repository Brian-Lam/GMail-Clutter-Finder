# MBox-Reader
My GMail inbox has been filling up after being used for the past few years. I didn’t want to pay for extra storage, so I’ve been clearing out old newsletters and promotional emails to reduce clutter.

Finding the emails to delete was a pretty manual process. I had a few hours to spare, so I wrote a program to find the email addresses that sent this clutter.

## Requirements
```
pip install cx_Freeze
```
This is a script that was written in Python 3.6.4. It shold work with Python 3.0+. It uses tkinter to create the GUI, and cx_freeze to compile to an executable.

## FAQ
**Does this collect any private information?**

No, I couldn’t care less about your mail. 

**Brian, this looks ugly as hell**

Yeah. 

**When I download it, my browser says it's not commonly downloaded and may be dangerous**

Hahaha I know 

## Nerdy stuff
* This started off as a command line program, but I figured this could help people who didn’t know how to use the command line. So I spent a couple hours learning a few libraries to port this into a real, usable program. You know, like, with buttons.
* Since an mbox file can be huge, it’s important not to load the whole file into memory. To avoid excessive memory consumption, only one line from the mbox file is read at a time.
* A defaultdict is used to store every sender’s email count. A maxheap is then used to build a sorted list of most common email senders, running in nlog(n) time. To relieve burden during the heapify process, only senders with an email count above a cutoff (currently 50) will be sent into the heap.
* This was my first time using a GUI library with Python and creating an exe from it. The documentation for tkinter and cx_freeze were fantastic, so learning them was much smoother than I thought it would be.
* The program’s zip file is about 37MB. This is awfully large for such a small program. That’s because cx_freeze pulls the entire tkinter framework into the build. I don’t feel like fixing that right now.

## How do I get an MBox file?
To get a dump of your entire GMail inbox, go to https://takeout.google.com/settings/takeout

## Author
[Brian Lam](http://www.brianlam.me)

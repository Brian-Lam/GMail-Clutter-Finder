# MBox-Reader
This Python script analyzes an mbox file, exported from GMail, to find your most common email senders. I wrote this to clear out my GMail storage space as it was hitting 50%. 

## Requirements
This is a script that was written in Python 3.6.4. It shold work with Python 3.0+ 

## Usage
```
usage: mboxreader.py [-h] filepath [n]

positional arguments:
  filepath    Location of mbox file
  n           The amount of emailsthat need to be received from a sender for
              them to be display in results
```

**Example**

To view only senders that have sent over 20 emails to you:

``` python mboxreader.py file/to/gmail/dump/mail.mbox -n 20 ```

## How do I get an MBox file?
To get a dump of your entire GMail inbox, go to https://takeout.google.com/settings/takeout

## Author
[Brian Lam](http://www.brianlam.me)
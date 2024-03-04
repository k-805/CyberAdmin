#!/usr/bin/env python

print("File1__name__=%s" %__name__)

if __name__ == "__main__" :
    print("File1 is being ran directly")
else :
    print("File1 is being imported")
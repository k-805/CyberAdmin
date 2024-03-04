#!/usr/bin/env python

import File1

print("File2__name__=%s" %__name__)

if __name__ == "__main__" :
    print("File2 is being ran directly")
else :
    print("File2 is being imported")
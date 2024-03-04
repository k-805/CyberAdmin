#!/usr/bin/env python

class Dog: 
    kind = 'canine'             # class variable shared by all instantces
    def __init__(self, name):
        self.name = name        # instance variable unique to each instance

def main(): 
    d = Dog("Luna")
    e = Dog("Fido")

    print(d.kind)   #shared by all dogs
    print(e.kind)
    print(e.name)   # unique to each
    print(d.name)

if __name__ == "__main__":
    main()
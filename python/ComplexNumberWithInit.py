#!/usr/bin/env python

# When a class defined an __init__() method, the class instantiation 
# automatically invokes __init__() for the newly created class instance

class ComplexNumber: 
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

def main():
    c = ComplexNumber(3.99, -10.2)
    print(c.r, c.i)
    print(c.r)
    print(c.i)

if __name__ == "__main__":
    main()
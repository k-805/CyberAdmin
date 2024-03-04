#!/usr/bin/env python

class MyClass: 
    str = "A simple string in my class"
    i = 12345

    def f(self):
        return "hello world from f()"
# MyClass.s, MyClass.i, MyClass.f are valid attribute references
# returning a string, int and function object

def main():
    print("hello world from main, in MyClass.py")

    # instantiate an instance of MyClass
    x = MyClass()
    print(x.str)
    print(x.i)

    # call immediate x.f
    print(x.f())

    #x.f a method object, so we can store cand call later
    xf = x.f

    print(xf())


if __name__ == "__main__":
    main()

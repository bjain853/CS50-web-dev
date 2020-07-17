'''
A decorator is a higher level function that returns a modified function 
'''
def announce(f):
    def wrapper():
        print("About to run a function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello World!!")

hello()

#decoratedFunc = announce(hello)
#decoratedFunc()
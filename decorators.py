def announce(f):
    def wrapper():
        print("System is about to run a function.....")
        f()
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, Mom!")

hello()

def sum(x):
    def wrapper():
        print("System is about to apply sum....")
        x()
        print("Sum Calculation Done.")
    return wrapper

@sum
def num():
    print( 5 + 5 )

num()
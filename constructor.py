def greet(fx):
    def mfx(*args, **kwargs):
        print("Hello")
        fx(*args, **kwargs)
        print("Welcome")
    return mfx

@greet
def hello():
    print("Good Morning")

@greet
def add(x,y):
    print (x+y)

hello()
# greet(hello)()
print("\n")

add(5,6) 

x=3 #global scope

def fine():
    x=4 #enclosed scope
    print(x)
    def shoo():
        print(x)
    y=5 #local scope
    print(y)
    shoo()
fine()
print(x)

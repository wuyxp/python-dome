def hello():
    print("hello")

def hello(name):
    print ("hello "+name)

def hello(p):
    print ("hello\nyour name: "+p['name'] +"\nyour age: "+ str(p['age']))

def hello(name='wuyang'):
    print('hello '+name)

def hello():
    return "hello"

def hello(names):
    for name in names:
        print ("hello: "+name)

def hello(*names):
    print (names)
hello('www')
hello('a','b','c')

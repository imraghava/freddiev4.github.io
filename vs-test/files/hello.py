class Hello():

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print('Hello, {}!'.format(self.name))
        
h = Hello("World")
h.sayHello()
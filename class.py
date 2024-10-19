class Fruits:
    def __init__(self,price,shape,name):
        self.price=price
        self.shape=shape
        self.name=name
    def display(self):
        print(f"my favourite fruit is {self.name} its {self.shape} in shape and cost {self.price}")

# create instance of a class(object)

myobj=Fruits(20,"oval","banana")
myobj.display()


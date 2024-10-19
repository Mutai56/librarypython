class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def display(self):
        print(f"My name is  {self.name} and am of age  {self.age} years and am a {self.gender}")

# create instance of a class(object)

myobj=Person("Joyce",40,"Female")
myobj.display()


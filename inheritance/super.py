class Human:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
    def description(self):
        print(f"My name is {self.name},I am a {self.gender} and I am {self.age} yrs old")
    def dance(self):
        print("I can dance")
#create a new class that inherits from the parent
class Girl(Human):
    def dance(self):
        print("I like classical dance")
    def activity(self):
        super().dance() #this will call the dance method of the parent class
x=Girl("Tina","Female",21)
x.description()
x.activity()

#super is basically used to call the method from the parent class anywhere in the child class.



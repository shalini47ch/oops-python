class Human:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def description(self):
        return f"Hey,my name is {self.name},I am a {self.gender} and I am {self.age} years old"
#now creating a new class that inherits from the parent
class Boy(Human):
    def schoolname(self,myschool):
        return f"My school name is {myschool}"
x=Boy("Rohan",21,"Male")
print(x.description())
print(x.schoolname("HPS"))


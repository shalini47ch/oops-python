class Human:
    species="Homo Sapiens" #class attribute
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    #creating some instance methods
    def speak(self):
        return f"Hello I am {self.name}"
    def dish(self,favoritefood):
        return f"I love eating {favoritefood}"
#now creating objects for the classes
x=Human("Bob",18,"Male")
print(x.name)
print(x.speak()) #here we are calling the methods
print(x.dish("momos"))


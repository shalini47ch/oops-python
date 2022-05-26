class Human:
    species="Homo Sapiens"
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
x=Human("Miney",21,"Female") #these are the objects and here the memory is allocated
y=Human("Miley", 22, "Female")

print(x.species) #species is the class attribute so it doesn't even change for different instances
print(y.species)
print(x.name) #name,age and gender are instance attributes so they change for different class instances
print(y.gender)
#printing the name,gender and age for both the instances created
print(f"Hi my name is {x.name}.I am {x.age} years old.")
print(f"Hi my name is {y.name}.I am {y.age} years old.")
#_ represents protected and __ represents private
class Employee:
    def __init__(self,name,id,salary):
        #keep the name as public
        self.name=name
        #keep the id as protected
        self._id=id
        #keep the salary as private
        self.__salary=salary 
    def getsalary(self):
        print("The salary is {self.__salary}")
x=Employee("ABC",11234,56000)
print(x.name)
print(x._id)
print(x.__salary) #this will give an error as it is part of private
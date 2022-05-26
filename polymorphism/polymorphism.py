class Monkey:
    def color(self):
        print("The monkey is yellow colored")
    def eats(self):
        print("The monkey eats bananas")
class Rabbit:
    def color(self):
        print("The rabbit is white colored")
    def eats(self):
        print("The rabbits eat carrot")
x=Monkey()
y=Rabbit()
for z in(x,y):
    z.color()
    z.eats()
'''
We are using only one variable to iterate over two objects it follows the rule of polymorphism

'''
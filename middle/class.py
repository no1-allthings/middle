class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def say(self, to_name):
        print('hi '+to_name + '야 나는 '+self.name+' '+str(self.age)+'살')

class Police(Person):
    def arrest(self, to_arrest):
        print(to_arrest+' 넌 체포되었다')


p1=Person('미자',20)
p2=Police('우양',30)

p2.arrest('최군')

p1.say('김양')
p2.say('황양')
# class Person:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def say(self, to_name):
#         print('hi '+to_name + '야 나는 '+self.name+' '+str(self.age)+'살')
#
# class Police(Person):
#     def arrest(self, to_arrest):
#         print(to_arrest+' 넌 체포되었다')
#
#
# p1=Person('미자',20)
# p2=Police('우양',30)
#
# p2.arrest('최군')
#
# p1.say('김양')
# p2.say('우양')

# class Animal:
#     def __init__(self):
#         self.kinds = input('종류입력: ')
#         self.name = input('동물이름: ')
#     def introduce(self):
#         print(self.kinds+'의 이름은 '+self.name+' 이다')
# li=[]
# for i in range(3):
#     li.append(Animal())
#
# for i in li:
#     i.introduce()

# class Sj:
#     def __init__(self):
#         self.kor=90
#         self.__eng=80
#         self.mat=85
#     def show(self):
#         print(self.__eng)
#
#     def get_s(self):
#         return self.__eng
#
#     def set_s(self, eng):
#         self.__eng=eng
#
#
# s=Sj()
# print(s.kor)
# s.show()
# s.set_s(100)
# print(s.get_s())
#print(s.eng) # 직접 변수에 접근뫃하게 했음


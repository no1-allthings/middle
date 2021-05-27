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
# print(s.eng) # 직접 변수에 접근뫃하게 했음

# class Ppp:
#     def __init__(self):
#         self.name = '란미'
#         self.age = 45
#
# class Kor(Ppp):
#     def say(self):
#         print('안녕')
#
# class Ame(Ppp):
#     def __init__(self):
#         super().__init__()
#         self.lang = '영어'
#     def say(self):
#         print('hello')
#
# pp = Ppp()
# kk = Kor()
# aa = Ame()
#
# print(pp.name)
# print(aa.age)
# print(kk.name, aa.age, )
#
# kk.say()
# aa.say()

# class P:
#     def __init__(self):
#         self.x = int(input('x:'))
#         self.y = int(input('y: '))
#     def dis(self):
#         pass
#
# class R(P):
#     def __init__(self):
#         super().__init__()
#         self.w = int(input('w: '))
#         self.h = int(input('h: '))
#     def dis(self):
#         print('사각',self.x,self.y,self.w,self.h)
#
# class C(P):
#     def __init__(self):
#         super().__init__()
#         self.r = int(input('r: '))
#     def dis(self):
#         print('원형', self.x ,self.y, self.r)
#
# def main():
#     l=[]
#     while True:
#         s = input('1.사각형, 2.원형, 3.조회, 4.졸료')
#         if s == '1':
#             l.append(R())
#         if s == '2':
#             l.append(C())
#         if s == '3':
#             for i in l:
#                 i.dis()
#         if s == '4':
#             break
#     print('프로그램 종료')
# main()

# class PP:
#     def __init__(self, sp):
#         self.li=[]
#         self.li.append(sp)
#     def di(self):
#         print(self.li)
# p1=PP('우우')
# p1.di()
# p2=PP('콜라')
# p2.di()
# p3=PP('커피')
# p3.di()
# p1=PP('사이다')
# p1.di()

class PP:
    li=[]
    def __init__(self, sp):
        PP.li.append(sp)
    def di(self):
        print(PP.li)
p1=PP('우우')
p1.di()
p2=PP('콜라')
p2.di()
p3=PP('커피')
p3.di()
p1=PP('사이다')
p1.di()


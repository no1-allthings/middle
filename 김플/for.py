n=[1,2,3]
for i in n:
    print(i)
    n=[4,5,6]
print(n)

print(id(n))
n.append(6)
print(n)
print(id(n))
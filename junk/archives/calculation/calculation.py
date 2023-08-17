import math

def per(a, b, c):
    return sum((a,b,c))

print("уведіть першу сторону трикутника:")
a = int(input())
print("уведіть другу сторону трикутника:")
b = int(input())
print("уведіть третю сторону трикутника:")
c = int(input())
print(per(a, b, c))

def pl(a,b,c):
    p = (a+b+c)*0.5
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))  # по формулі Герона
    print (s)
    return s
print(pl(a,b,c))
# print(2*3)
# print(2**3)
# print(10/2)
# print(10//2)
# print(10*2+2)
# print(10+2*2)

# print("West Chester")
# print("West")
# print(" I'm here")
# print(''' aaa " ' ' ''')
# print(/n)

# name="Chester"
# d=len(name)
# print(d)
# print(len(name))

# name="university"
# print(name[1]) # n
# print(name[0]) # u
# print(name[len(name)])

# random numbers
# import random
# m=random.randint(-10, 10)
# print(m)

# import random
# # randomOdd=random.randint(1, 100)//2==0
# # print(randomOdd)

# m = random.randint(-10, 10)
# print("m:", (2*m) + 1)

# name="abcd"
# print(name[0],name[1],name[2],name[3],sep="")
# print(name[3],name[2],name[1],name[0],sep="*")

word="given"
for i in range(1, 5):
    print("*", end="")

print("\n")

for i in range(5):
    print(".",end="")

print("\n")

for i in range(1,10,2):
    print(i,end="")

print("\n")

# name="Chester"
# d=len(name)
# print(d)

# print("\n")

# for m in range(0, d):
#     print(name[m])

# print("\n")

name="Chester"
d=len(name)
# print(d)
for m in range(len(name)-1,-1,-1):
    print(name[m])

print("\n")

# import random
# for m in range(0,5): #0,1,2,3,4
#     r=random.randint(-100,100)
#     print(r)

# myfile=open('testingreading.txt','r')
# line=myfile.readline()
# print(line)
# myfile.close()

# myfile=open('testingreading.txt','r')
# outfile=open('testingwriting.txt','w')

# line=myfile.readline()
# while(line !=""):
#     outfile.write(line)
#     line=myfile.readline()
# myfile.close()
# outfile.close()

# Mylist=[1,-2,100,54,"AAA"]
# print(Mylist)

# Mylist=[1,-2,100,0,-2,-2]
# print(max(Mylist))
# print(min(Mylist))
# print(len(Mylist))

# Mylist.sort()
# print(Mylist)

# Mylist.remove(-2) # removes 1st instance only
# print(Mylist)

# print(Mylist.index(100))
# print(Mylist.index(-2))

# print(sum(Mylist))

# Mylist.remove(-2)
# print(Mylist)

# Mylist=[1,-2,100,0,-2,-2]
# while(-2 in Mylist):
#     Mylist.remove(-2)

# print(Mylist)

Mylist=[1,-1,0,100,100]
Mylist.insert(1,"AAA") # insert at index 1

print(Mylist)
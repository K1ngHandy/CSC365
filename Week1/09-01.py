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

# M=[1,-2,100,54,"AAA"]
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

# Mylist=[1,-1,0,100,100]
# Mylist.insert(1,"AAA") # insert at index 1

# print(Mylist)

# Mylist.append("123") # add to end of list
# print(Mylist)

# alist=[1,2,3]
# blist=[6,7,8,9]
# alist.extend(blist)
# print(alist)

# randomList=[]
# import random
# i = 1
# # generate a list containing 10 random nums
# for m in range(0,10):
#     r=random.randint(-10,10)
#     randomList.append(r)

# print(randomList)

# myList=[]
# Enum=0
# Onum=0
# for m in randomList:
#     r=random.randint(-10,10)
#     if (m%2==0):
#         Enum=Enum+1
#     else:
#         Onum=Onum+1
#     myList.append(r)

# print(myList)
# print(Enum,"****",Onum)

# counter=0
# inputFile=open('testingreading.txt','r')
# line=inputFile.readline()

# while (line !=""):
#     counter=counter+1
#     line=inputFile.readline()

# print(counter)

# counter=0
# total=0
# numFile=open('newFile.txt','r')
# line=numFile.readline()
# maxi=int(line)

# while (line !=""):
#     total=int(line)+total
#     counter=counter+1

#     if(int(line)>maxi):
#         maxi=int(line)

#     line=numFile.readline()
# print(counter)
# print(total)
# print(total/counter)
# print(maxi)

# MyList=[]
# import random
# pos=0
# neg=0
# for m in range(0,5):
#     r=random.randint(-10,10)
#     if (r>0):
#         pos=pos+1
#     else:
#         neg=neg+1
#     MyList.append(r)

# print(MyList)
# print(pos,"****",neg)

counter=0
total=0
inputFile=open('numFile.txt','r')
line=inputFile.readline()
maxi=int(line)

while (line !=""):
    total=int(line)+total
    counter=counter+1
    line=inputFile.readline()
avg=total/counter
print(avg)

Mavg=0
Lavg=0
inputFile=open('numFile.txt','r')
line=inputFile.readline()
while(line !=""):
    if(int(line)>avg):
        Mavg=Mavg+1
    else:
        Lavg=Lavg+1
        line=inputFile.readline()
print(Mavg,"****",Lavg)
inputFile.close()

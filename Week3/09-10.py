# import sklearn
# from sklearn.metrics.pairwise
# import cosine_similarity

#
# import random
# import matplotlib.pyplot as plt

# def dice():
#     return random.randint(1,6)
# n=range(100, 10000, 10)
# avgs=[]

# for m in n:
#     result=[]
#     for i in range(m):
#         result.append(dice())

#     avgs.append(sum(result)/(m))

# plt.plot(n, avgs)
# plt.xlabel("Trials")
# plt.ylabel("")
# plt.show()

#
# import random
# import numpy as np
# x=np.array([3, 6, -8])
# print(x)

# generate random numbers
# import numpy as np
# user = np.array([5, 1, 3])
# music = np.random.randint(5, size=(3, 1000)) + 1
# print(user.shape)
# print(music.shape)
# print(music[:, :5])

# import time
# for n in (10000, 100000, 1000000):
#     music = np.random.randint(5, size=(3, n)) + 1
#     now=time.time()
#     np.dot(user, music)
#     print(time.time() - now, "seconds to run", n, "music items")

#     scores = np.dot(user, music)
#     print(scores[:10])
#     print("\n********\n")
# print(music[:, :10])

#
# import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt

# results = []
# for n in range(1, 10000):
#     nums = np.random.randint(low=1, high=100, size=n)
#     mean = nums.mean()
#     results.append(mean)

# df=pd.DataFrame({'means': results})
# print(df.head())
# print(df.tail())
# df.plot()
# plt.xlabel("")
# plt.ylabel("Avg. of samples")
# plt.show()

# law of large numbers (incomplete)
# import random
# from matplotlib import pyplot as plt

# def dice():
#     return random.randint(1, 6)
# n=range(100, 10000, 10)

# probability of getting 6
# import random
# import matplotlib.pyplot as plt

# def dice():
#     return random.randint(1, 6)

# trials=range(10, 10001, 10)
# prob = []

# for n in trials:
#     count = 0

#     for i in range(n):
#         if dice() == 6:
#             count = count + 1

#     prob.append(count / n)

# plt.plot(trials, prob)
# plt.axhline(1/6, color="red")

# plt.xlabel("Number of trials")
# plt.ylabel("Prob. of getting 6")
# plt.show()

# coin
# import random
# import matplotlib.pyplot as plt

# def coin():
#     return random.choice("H", "T")

# trials=range(10, 10001, 10)
# prob = []

# for n in trials:
#     heads = 0

#     for i in range(n):
#         if coin() == 6:
#             heads = heads + 1

#     prob.append(heads / n)

# plt.plot(trials, prob)
# plt.axhline(1/6, color="red")

# plt.xlabel("Number of trials")
# plt.ylabel("Prob. of getting 6")
# plt.show()

# mode, max, standard dev.
# import numpy as np
# import statistics as st
# print(st.mode([2, 15, 17, 14, 15, 15]))
# print(np.max([11, 15, 17, 14, 14]))
# print(np.std([11, 15, 17, 14, 14]))

#
# import matplotlib.pyplot as plt
# import numpy as np
# Grades = np.random.normal(100, 20, 500)

# Titanic
import pandas
File=pandas.read_csv('Titanic.csv')
File=File[['Survival', 'Sex']]
print(File)

num = File.shape[0]
print("***", num)

PS = (File.Survival == 1).sum()
print(PS)
PNS = 1 - PS

PM = (File.Sex == 'M').sum() / num
print(" Prob. of Male", PM)
PF = 1 - PM
print(" Prob. of Female", PF)

NW = File[File.Sex == 'F'].shape[0]
print("Total female", NW)


#
import pandas
File=pandas.read_csv('Titanic.csv')
File=File[['Survival', 'Class']]
print(File)

num = File.shape[0]
print("***", num)

PS = (File.Survival == 1).sum()
print(PS)

PNS = 1 - PS
P3C = (File.Class == 3).sum() / num
print(" Prob. of being on 3rd class", P3C)

N3C = File[File.Class == 3].shape[0]
print("Total 3rd class", N3C)

C3S = File[(File.Class == 3) & (File.Survival == 1)].shape[0]
PC3S = C3S /N3C
print("Probability of surviving in 3rd class: ", PC3S)

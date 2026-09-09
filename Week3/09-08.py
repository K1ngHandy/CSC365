import pandas as pd

# s=[1, 12, 3, 2, 12]
# print(set(s))
# s=pd.Series([1, 2, 2, 4, 3])
# print(s)
# print(s.count())
# print(s.value_counts())

# s=pd.Series(["Ann", "Liz", "Bob", "Dave"])
# print(s)
# print(s.count())
# print(s.value_counts())

# s=pd.Series([10, 20, 20, 30, 40, 40, 40])
# print("Count: ", s.count())
# print("Mean: ", s.mean())
# print("Median: ", s.median())
# print("Minimum: ", s.min())
# print("Maximum: ", s.max())
# print("Sum: ", s.sum())

# print("Frequency: ")
# print(s.value_counts())
# print("Mode", s.mode()) # mode adds index for repeating values

# import matplotlib.pyplot as plt
# x=(1, 2, 3, 4, 5, 6, 7, 8)
# y=(0, 50, 100, 50, -50, 0, 100, -50)
# plt.plot(x, y, marker='d', linestyle=":", color="r", linewidth=2.1)
# plt.show()

# pie chart
# import matplotlib.pyplot as plt
# File=pd.read_csv('Titanic.csv')
# New=File['Name'].value_counts()
# New.plot(kind='pie')
# plt.xlabel('Name')
# plt.ylabel('Class')
# plt.title('Titanic')
# plt.show()
# print(File.groupby("Sex")["Age"].mean())
# print(File.groupby("Sex")["Age"].max())
# print(File.groupby("Sex")["Age"].min())
# print(File.groupby("Sex")["Age"].count())

# # similarity
def similarity(user1, user2):
    common=len(user1 & user2)
    total = len(user1 | user2)

    return(common / total)

users = {
    "Ann": {"Target", "Gap", "Old Navy"},
    "Bob": {"Target", "Walmart", "Wegmans"},
    "Charlie": {"Target", "Gap", "Wegmans"},
    "David": {"Target", "Gap", "Old Navy", "Wegmans"}
}

target = users["Ann"]

for name, stores in users.items():
    if name != "Ann":
        score=similarity(target, stores)
        print(name, score)


doc1="Python is useful for data science"
doc2="Python is popular for data analysis in science"

A=set(doc1.lower().split())
B=set(doc2.lower().split())
Jaccard=len(A & B) / len(A | B)
print("Jaccard")
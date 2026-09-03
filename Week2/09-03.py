import pandas as pd

my_list = {"scores": [100,20,-20,50],
        "names": ["AAA", "ZZZ", "bb", "qqqq"]
        }
df=pd.DataFrame(my_list)
print(df)
print(df.describe())
print(df.head()) # first 5 data points
print(df.tail())
print(df["scores"].unique())

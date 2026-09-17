# HW-2
# Stephen Handy
# 0796861

# imports
import pandas
import matplotlib.pyplot as plt
import numpy as np

# dataset
File = pandas.read_csv('HW/dataset_2.csv')
File = File.dropna(axis = 1, how = 'all')

# 1
# print(File)

# 2
print("Total Customers: ", File.shape[0])

# 3


# 4
frequency_count = File['visit_frequency'].value_counts()

plt.figure(figsize=(8, 5))
plt.barh(frequency_count.index, frequency_count.values)

plt.xlabel('Number of Purchases')
plt.ylabel('Visit Frequency')
plt.title('Frequency of Visits to Purchases Made')

plt.show()

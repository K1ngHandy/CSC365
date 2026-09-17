# HW-2
# Stephen Handy
# 0796861

# dataset
import pandas
File = pandas.read_csv('HW/dataset_2.csv')
File = File.dropna(axis = 1, how = 'all')

print(File)

print("Number of Customers: ", File.shape[0])

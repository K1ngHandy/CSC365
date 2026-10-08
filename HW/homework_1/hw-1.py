import numpy
from scipy import stats

# 1. The following data gives the speed of cars (miles per hour) on I-95. Find the mode: 75, 100, 95, 120, 45, 75, 45, 95, 75.
list1 = {"speeds": [75, 100, 95, 120, 45, 75, 45, 95, 75]}
mode1 = stats.mode(list1["speeds"], keepdims=False)

print("Mode: ", mode1.mode) # 75

# 2. The following are the ages (in years) of students in a class. Find the mean age of students: 23,21,25,24,20.
list2 = {"ages": [23, 21, 25, 24, 20]}
mean2 = numpy.mean(list2["ages"])

print("Mean: ", mean2) # 22.6

# 3. The following data gives the memory usage (in megabytes) of different applications on a cell phone. Find the median: 110, 90, 200, 250, 280.
list3 = {"megabytes": [110, 90, 200, 250, 280]}
med3 = numpy.median(list3["megabytes"])

print("Median: ", med3) # 200.0

print() # line break

# 4. Is it possible for a quantitative data set to have no median, no mode, and no mean? Give one example for each case and explain why.
samples = {"no_median": [], "no_mode": [3, 6, 9, 12], "no_mean": []}

median4 = numpy.median(samples["no_median"])
print("There will always be a median as this is the middle of dataset, unless this dataset is empty: ", median4) # RuntimeWarning: Mean of empty slice, nan

print() # line break

mode4 = stats.mode(samples["no_mode"], keepdims=False)
print("There is no mode when all data points are unique, and 0th index may be displayed instead: ", mode4.mode) # 3

print() # line break

mean4 = numpy.mean(samples["no_mean"])
print("There is no mean when a dataset is empty: ", mean4) # nan

print() # line break

# 5. Suppose the average amount of money spent on shopping by 10 persons during a given week is $200. Find the total amount of money spent on shopping by these 10 people.
avg = 200
persons = 10
total = avg * persons
print("Total: ", total) # 2000

# 6. The following data gives the number of spam emails received by 5 students during the last week. Find the variance and standard deviation: 20,10,25,35,50.
list6 = {"spam_emails": [20, 10, 25, 35, 50]}
A={"A": [10,2,3,4,5,6,7,8,9,10]}

variance = numpy.var(list6["spam_emails"])
standard = numpy.std(list6["spam_emails"])

print("Variance: ", variance) # 186.0
print("Standard Dev: ", standard) # 13.638181696985855

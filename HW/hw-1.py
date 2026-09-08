import numpy
from scipy import stats

# 1 - mode
list1 = {"speeds": [75, 100, 95, 120, 45, 75, 45, 95, 75]}
mode1 = stats.mode(list1["speeds"], keepdims=False)

print("Mode: ", mode1.mode)

# # 2 - mean
list2 = {"ages": [23, 21, 25, 24, 20]}
mean2 = numpy.mean(list2["ages"])

print("Mean: ", mean2)

# 3 - median
list3 = {"megabytes": [110, 90, 200, 250, 280]}
med3 = numpy.median(list3["megabytes"])

print("Median: ", med3)

# 4 - no median, no mode, no mean
list4 = {"sample": []}
print("Sample: ", list4["sample"])

# 5 - total spent
avg = 200 # $200
persons = 10
total = avg * persons
print("Total: ", total)

# 6 - variance and standard deviation
list6 = {"spam_emails": [20, 10, 25, 35, 50]}
A={"A": [10,2,3,4,5,6,7,8,9,10]}

variance = numpy.var(list6["spam_emails"])
standard = numpy.std(list6["spam_emails"])

print("Variance: ", variance)
print("Standard Dev: ", standard)

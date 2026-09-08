import numpy
# from scipy import stats

# 1 - mode
# list1 = {"speeds": [75, 100, 95, 120, 45, 75, 45, 95, 75]}
# mode1 = stats.mode(list1["speeds"])
# print("mode: ", mode1.mode)

# # 2 - mean
list2 = {"ages": [23, 21, 25, 24, 20]}
mean2 = numpy.mean(list2["ages"])
print("mean: ", mean2)

# 3 - median
list3 = {"megabytes": [110, 90, 200, 250, 280]}
med3 = numpy.median(list3["megabytes"])
print("median: ", med3)

# 4 - no median, no mode, no mean
# list4 = {"": []}

# 5 - total spent
# list5 = {"": []}

# 6 - variance and standard deviation
list6 = {"spam_emails": [20, 10, 25, 35, 50]}

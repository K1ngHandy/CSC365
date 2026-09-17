# import matplotlib.pyplot as plt
# import numpy as np

# friends = [109, 1017, 1127, 418, 625, 957, 89, 950, 946, 797, 981, 125, 1000, 1013, 1005, 1011, 1009, 1012, 1014, 1015]
# y_pos = range(len(friends))

# m = np.mean(friends)
# s = np.std(friends)
# z = [(x - m) / s for x in friends]

# plt.figure()
# plt.bar(y_pos, z, color = 'lightcoral')

# plt.axhline(1, color = 'green', linestyle = '--', label = '+1 Std')
# plt.axhline(1, color = 'green', linestyle = '--', label = 'Mean')
# plt.axhline(1, color = 'green', linestyle = '--', label = '-1 Std')

# plt.xlabel("Person Index")
# plt.ylabel("Z-score")

# plt.legend()
# plt.show()

#
# import pandas as pd
# import matpllotlib.pyplot as plt

# Tiktok = [10, 0, 11, 13, 14, 12, 12, 14, 8, 5]
# work = [30, 89, 40, 20, 30, 35, 30, 20, 90, 85]

# df = pd.DataFrame({'Hours_on_Tiktok': Tiktok, 'Hours_performance': work})
# df.plot(x = "Hours_on_Tiktok", y = 'Work_performance', kind = 'scatter')

# # ...
# plt.show()

import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt

friends = [109, 1017, 1127, 418, 625, 957, 89, 950, 946, 797, 981, 125, 1000, 1013, 1005, 1011, 1009, 1012, 1014, 1015]
happiness = [0.8, 0.6, 0.9, 0.5, 0.7, 0.4, 0.3, 0.6, 0.8, 0.5, 0.7, 0.2, 0.9, 0.6, 0.8, 0.7, 0.5, 0.6, 0.8, 0.9]

df = pd.DataFrame({'friends': friends, 'happiness': happiness})
print(df.head())

df_scaled = pd.DataFrame(preprocessing.scale(df[['friends']]), columns=['friends_scaled'])
df_scaled['happiness'] = df['happiness']
print(df_scaled.head())

df_scaled.plot(kind='scatter', x='friends_scaled', y='happiness')

plt.show()
print(df.corr())


w1s = df_scaled[(df_scaled['friends_scaled'] <= 1) & (df_scaled['friends_scaled'] >= -1)]
p1 = w1s.shape[0] / df_scaled.shape[0]
print(p1)

#
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats

# np.random.seed(1)
# long_breaks = stats.poisson.rvs(mu = 60, size = 3000)
# short_breaks = stats.poisson.rvs(mu = 15, size = 6000)

# breaks = np.concatenate((long_breaks, short_breaks))

# pd.Series(long_breaks).hist(bins = 30, edgecolor = "black")
# plt.xlabel("Value")
# plt.ylabel("Density")
# plt.title("Histogram of Simulated Long Breaks")
# plt.show()

# pd.Series(breaks).hist(bins = 30, edgecolor = "black")
# plt.xlabel("Value")
# plt.ylabel("Density")
# plt.title("Histogram of Simulated Short Breaks")
# plt.show()

# pd.Series(short_breaks).hist(bins = 30, edgecolor = "black")
# plt.xlabel("Value")
# plt.ylabel("Density")
# plt.title("Histogram of Simulated Breaks")
# plt.show()

# print(breaks.mean())
# sample_breaks = np.random.choice(a = breaks, size = 10)
# print(breaks.mean() - sample_breaks.mean())

#
# import random

# races = (["white"] * 2000 + ["black"] * 1000 + ["hispanic"] * 1000 + ["asian"] * 3000 + ["other"] * 3000)

# for race in set(sample):
#     print(race, ":", sample.count(race))


# plt.show()

#
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy import stats

# np.random.seed(1)
# long_breaks = stats.poisson.rvs(mu = 60, size = 3000)
# short_breaks = stats.poisson.rvs(mu = 15, size = 6000)

# breaks = np.concatenate((long_breaks, short_breaks))

# pd.Series(long_breaks).hist(bins = 30, edgecolor = "black")
# plt.xlabel("Value")
# plt.ylabel("Density")
# plt.title("Histogram of Simulated Long Breaks")
# plt.show()

# pd.Series(breaks).hist(bins = 30, edgecolor = "black")
# plt.xlabel("Value")
# plt.ylabel("Density")
# plt.title("Histogram of Simulated Short Breaks")
# plt.show()

# pd.Series(short_breaks).hist(bins = 30, edgecolor = "black")
# plt.xlabel("Value")
# plt.ylabel("Density")
# plt.title("Histogram of Simulated Breaks")
# plt.show()

# point_estimates = []:
# # ...

# print(breaks.mean())
# sample_breaks = np.random.choice(a = breaks, size = 10)
# print(breaks.mean() - sample_breaks.mean())

#
# import random
# import math
# import numpy as np
# from scipy import stats

# long_breaks = stats.poisson.rvs(mu = 60, size = 3000)
# short_breaks = stats.poisson.rvs(mu = 15, size = 6000)

# breaks = np.concatenate((long_breaks, short_breaks))

# sample_size = 100
# sample = np.random.choice(a = breaks, size = sample_size)

# sample_mean = sample.mean()
# sample_stdev = sample.std()
# standard_error = sample_stdev / math.sqrt(sample_size)

# Conf = stats.t.interval(0.95, df = sample_size - 1, loc= sample_mean)
# ...

#
# import math
# import numpy as np
# from scipy import stats

# long_breaks = stats.poisson.rvs(mu = 60, size = 3000)
# short_breaks = stats.poisson.rvs(mu = 15, size = 6000)
# breaks = np.concatenate((long_breaks, short_breaks))

# def makeConfidenceInterval():
#     sample_size = 100
#     sample = np.random.choice(a = breaks, size = sample_size)

#     sample_mean = sample.mean()
#     sample_stdev = sample.std(ddof = 1)
#     standard_error = sample_stdev / math.sqrt(sample_size)

#     return stats.t.interval(0.95, df = sample_size - 1, loc = sample_mean)

# ci = makeConfidenceInterval()
# print(ci)

# times_in_interval = 0

# for i in range(10000):
#     interval = makeConfidenceInterval()
#     if interval[0] <= breaks.mean() <= interval[1]:
#         times_in_interval += 1



#
# for confidence in (0.5, 0.8, 0.85, 0.9, 0.95, 0.99):
#     times_in_interval = 0
#     for i in range(10000):
#         interval = makeConfidenceInterval()
#         if interval[0] <= breaks.mean() <= interval[1]:
#             times_in_interval += 1
#     print(confidence, ":", times_in_interval / 10000)

# #
# long_breaks_in_engineering = stats.poisson.rvs(mu = 60, size = 100)
# short_breaks_in_engineering = stats.poisson.rvs(mu = 15, size = 300)
# engineering_breaks = np.concatenate((long_breaks_in_engineering, short_breaks_in_engineering))

# # print(breaks.mean())
# print(engineering_breaks.mean())
# t_statistic, p_value = stats.ttest_1samp(a = engineering_breaks, popmean = b)

# print(t_statistic)
# print(p_value)

#
# from scipy import stats
# import numpy as np

# observed = [10, 17, 18, 3]
# expected = [15, 16, 14, 3]
# chi_squared, p_value = stats.chisquare(f_obs = observed, f_exp = expected)

# print(chi_squared, p_value)

# observed = np.array([[10, 17])

#
# from scipy import stats
# import numpy as np

# data = [10, 9, 10, 10, 9, 10, 9]
# population_mean = 9.5

# mean = np.mean(data)
# print("Sample Mean:", mean)
# print("Population Mean:", population_mean)

#
# from scipy import stats
# import numpy as np

# data = [10, 9, 10, 10, 9, 10, 9]
# mean = np.mean(data)

# n = len(data)
# std = np.std(data, ddof = 1)

# confidence = 0.95
# t = stats.t.ppf((1 + confidence) / 2, df = n - 1)
# margin_of_error = t * (std / np.sqrt(n))
# confidence_interval = (mean - margin_of_error, mean + margin_of_error)

#
import numpy as np
from scipy.stats import chi2_contingency

data = np.array([[30, 20], [15, 35]])

chi2, p, dof, expected = chi2_contingency(data)

print("Chi-square", chi2)
print("P-value", p)
print("Expected:\n", expected)

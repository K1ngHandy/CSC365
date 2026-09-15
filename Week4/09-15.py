#
# import pandas as pd
# import matplotlib.pyplot as plt
# drinks = pd.read_csv('drinks.csv')
# drinks.continent.value_counts().plot(kind = 'bar', title = 'Countries per')
# plt.xlabel('Continent')
# plt.ylabel('Count')
# plt.show()

#
# import pandas as pd
# import matplotlib.pyplot as plt
# drinks = pd.read_csv('drinks.csv')
# drinks.groupby('continent').beer_servings.mean().plot(kind = 'bar')
# plt.xlabel('Continent')
# plt.show()

#
# import pandas as pd
# import matplotlib.pyplot as plt
# drinks = pd.read_csv('drinks.csv')
# drinks.boxplot(column = 'beer_servings', by = 'continent')
# plt.show()

#
# data_list = ["apple", "", None, "banana", "orange", None, ""]
# cleaned_list = [x for x in data_list if x and str(x).strip()]
# print(cleaned_list)

#
# import pandas as pd
# import numpy as np
# df = pd.DataFrame({
#     "name":["Alice", "", "Bob", None, "Charlie"],
#     "age":[25, None, 30, None, 22],
#     "city":["New York", "  ", "Los Angelos", "Chicago", None]
# })
# df_cleaned = df.dropna(how = 'all')

#
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy import stats

# np.random.seed()

# WCU = stats.
# ...

#
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy import stats

# np.random.seed()

# WCU_poisson = stats.poisson.rvs(mu=60, size=50)
# WCU_binom = stats.binom.rvs(n = 20, p = 0.6, size = 50)

# plt.boxplot(
#     [WCU_poisson, WCU_binom]p
# )

# plt.xlabel('Value')
# plt.title('Poisson vs Binomial Dist.')

# plt.show()
# ...

#
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

np.random.seed() # random number generator

WCU_poisson = stats.poisson.rvs(mu=70, size=50)
WCU_binom = stats.binom.rvs(n = 100, p = 0.7, size = 50)

plt.boxplot(
    [WCU_poisson, WCU_binom],
    orientation = 'horizontal',
    label = ['Poisson', 'Binomial']
)

plt.axvline(70, color='red', linestyle = '--', label = 'Expected Value = 70')
plt.xlabel('Value')
plt.title('Poisson vs Binomial: Same Expected Value')
plt.legend()

plt.show()

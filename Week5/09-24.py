# import numpy as np
# import matplotlib.pyplot as plt

# x = np.random.rand(100)
# y = 4 + 3 * x + np.random.rand(100) * 0.5

# plt.scatter(x, y)
# plt.show()

#
# import numpy as np
# import matplotlib.pyplot as plt

# hours = np.array([1, 2, 3, 4, 5, 6])
# scores = np.array([50, 55, 65, 70, 80, 85])

#
# import numpy as np
# import matplotlib.pyplot as plt

# pageSpeeds = np.random.normal(3.0, 1.0, 100)
# purchaseAmount = np.random.normal(50, 30, 100)

# plt.scatter(pageSpeeds, purchaseAmount)
# plt.xlabel("Page Speeds")
# plt.ylabel("Purchase Amount")
# plt.show()

#
# trainX = pageSpeeds[:80]
# testX = pageSpeeds[80:]

# trainY = purchaseAmount[:80]
# testY = pageSpeeds[80:]

# plt.scatter(trainX, trainY)
# plt.show()

#
# x = np.array(trainX)
# y = np.array(trainY)
# p4 = np.poly1d(np.polyfit(x, y, 4))

# xp = np.linspace(0, 7, 100)
# axes = plt.axes()
# axes.set_xlim([0, 7])
# axes.set_ylim([0, 200])
# plt.scatter(x, y)
# plt.plot(xp, p4(xp), c = 'r')
# plt.show()

#
# import numpy as np
# import matplotlib.pyplot as plt

# hours = np.array([1, 2, 3, 4, 5, 6])
# scores = np.array([50, 55, 65, 70, 80, 85])

# plt.scatter(hours, scores)
# plt.xlabel("Study Hours")
# plt.ylabel("Exam Score")
# plt.show()
# from sklearn.linear_model import LinearRegression

# model = LinearRegression()
# model.fit(hours.reshape(-1, 1), scores)

# print("Intercept:", model.intercept_)
# print("Slope:", model.coef_[0])
# predicted_scores = model.predict(hours.reshape(-1, 1))

# plt.scatter(hours, scores)
# plt.plot(hours, predicted_scores, color='red')
# plt.xlabel("Study Hours")
# plt.ylabel("Exam Score")
# plt.show()

#
# import padas as pd
# import matplotlib.pyplot as plt
# import requests
# import seaborn as sns
# import io

# url = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/bikeshare.csv"
# response = requests.get(url)
# bikes = pd.read_csv(io.StringIO(response.text))
# print(bikes.head())
# bikes.plot(kind = 'scatter', x)

#
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error

# df = pd.read_csv("train.csv", parse_dates = ['datetime'], index_col = 'datetime')

# print(df.head())
# print(df.describe())

# plt.figure(figsize=(12, 4))
# df['count'].plot()
# plt.title("Bike Rentals Over Time")
# plt.ylabel("Number of Bikes")
# plt.show()

#
# features = ['season', 'holiday', 'workingday', 'temp', 'humidity', 'windspeed']
# X = df[features]
# y = df['count']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
# model = LinearRegression()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# mse = mean_squared_error(y_test, y_pred)
# print("Mean Squared Error:", mse)

# plt.figure(figsize = (8, 6))
# plt.scatter(y_test, y_pred, alpha = 0.5)
# plt.xlabel("Actual Bike Rentals")
# plt.ylabel("Predicted")
# plt.title("Actual vs Predicted Bike Rentals")
# plt.show()

#
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error

# true = [9, 6, 7, 6]
# pred = [8, 7, 7, 12]
# from sklearn import metrics
# import numpy as np
# print('MAE:', metrics.mean_absolute_error(true, pred))
# print('MSE:', metrics.mean_squared_error(true, pred))
# print('RMSE:', np.sqrt(metrics.mean_squared_error(true, pred)))

#

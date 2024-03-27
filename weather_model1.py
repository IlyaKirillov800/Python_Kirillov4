import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Загрузка данных
weather_data = pd.read_csv("weather_data.csv")

# Проверка типов данных
print(weather_data.info())

# Построение регрессионной модели
X = weather_data[['Temperature', 'Humidity']]
y = weather_data['FeelsTemperature']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Визуализация данных по каждой паре параметров и линии регрессии
sns.pairplot(weather_data, x_vars=['Temperature', 'Humidity'], y_vars='FeelsTemperature', kind='reg')
plt.show()

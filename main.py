import matplotlib.pyplot as plt
import pandas as pd

# Покажу график

dataset = pd.read_csv('new.csv')
pr = dataset[['price']]
pr.plot(kind='line', y='price', color='pink')
plt.show()

# Видим, что наименьшее значение находится перед наибольшим, если купим на на минимуме, а продадим на максимуме, то мы
# получим наибольшую прибыль. Так и сделаю:

# Вычислим максимум - минимум

cost1 = min(pr['price'])
cost2 = max(pr['price'])

ind1 = dataset[['price']].idxmin()
ind2 = dataset[['price']].idxmax()
print('дата покупки ', *dataset['date'].iloc[ind1], ' дата продажи ', *dataset['date'].iloc[ind2], ' изменение ',
      cost2 - cost1)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Пример данных (в реальном проекте можно загрузить CSV)
data = {'values': [10, 20, 15, 30, 25, 40, 35]}
df = pd.DataFrame(data)

# Анализ данных
mean_value = np.mean(df['values'])
max_value = np.max(df['values'])
min_value = np.min(df['values'])
median_value = np.median(df['values'])
std_value = np.std(df['values'])

print(f"Среднее значение: {mean_value}")
print(f"Максимальное значение: {max_value}")
print(f"Минимальное значение: {min_value}")
print(f"Медиана: {median_value}")
print(f"Стандартное отклонение: {std_value}")

# Построение графика
plt.plot(df['values'], label='Данные')
plt.title('График значений')
plt.xlabel('Индекс')
plt.ylabel('Значения')
plt.legend()
plt.savefig('plot.png')
plt.show()
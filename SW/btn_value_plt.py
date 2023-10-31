import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')

x_data = []
y_data = []

for row in df:
    x, y = row.split(',')
    x_data.append(float(x))
    y_data.append(float(y))


plt.plot(x_data, y_data)

plt.xlabel('U[V]')
plt.ylabel('t[ms]')
plt.title('BTN Graph')

plt.show()
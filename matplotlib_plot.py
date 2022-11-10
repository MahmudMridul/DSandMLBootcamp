import matplotlib.pyplot as plt
import pandas as pd
import random

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

sales = pd.read_excel('sales.xlsx')

# y = sales.groupby('Year').sum()['R032']
# x = sales['Year'].unique()
# # plt.plot(x, y, linestyle='dotted')
# # plt.bar(x, y, color='skyblue')
# plt.title('Sales of R032 each year')
# plt.show()

y = sales.groupby('Month').sum()['R032']
# x = sales['Month'].unique()
# x.sort()
# plt.plot(x, y)
# plt.pie(y)
# plt.title('Month wise sales of R032')
plt.show()


import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
data = [10, 20, 30]
arr = np.array(data)
d = {'a' : 10, 'b' : 20, 'c' : 30}

#print(pd.Series(data=data))
#print(pd.Series(data=data, index=labels))
#print(pd.Series(d))

ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4], ['USA', 'Germany', 'Italy', 'Japan'])

#print(ser1['USA'])
print(ser1 + ser2)

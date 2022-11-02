import numpy as np
# provides linear algebra functionality

arr = np.array([num for num in range(20)])
print(arr)

matrix = np.array([[num for num in range(1,4)], [num for num in range(4,7)], [num for num in range(7,10)]])
print(matrix)

# returns numbers between (0,10]
print(np.arange(0,10))

# reshapes
print(np.arange(0, 10).reshape(5,2))

# returns max element
print(np.arange(0,10).max())

# returns max element's index
print(np.arange(0,10).argmax())

# returns min element
print(np.arange(0,10).min())

# returns min element's index
print(np.arange(0,10).argmin())

print(np.zeros(5))

print(np.zeros((5,5)))

print(np.ones(5))

print(np.ones((5,5)))

# returns a numpy array of size 10 where elements are evenly distributed between (0, 5)
print(np.linspace(0,5,10))

# returns an idnetity matrix
print(np.eye(5))

# returns 5 random numbers between [0, 1]
print(np.random.rand(5))

# returns a 3,3 matrix elements are between [0, 1]
print(np.random.rand(3,3))

# returns 10 random integers between (1,100]
print(np.random.randint(1,100,10))




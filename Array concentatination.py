### Array concentatination

import numpy as np

array_1 = np.array([[1, 2], [3, 4,]])
array_2 = np.array([[5,6]])

print("x","\n" ,array_1 )
print("y","\n" ,array_2 )

np.concatenate((array_1 , array_2),axis=0)
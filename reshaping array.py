


# reshaping array

# Creating a 2D array
array_2rd = np.array([[1, 2, 3, 4, 5], [6, 7, 8,9,10],[11,12,13,14,15]])
print("2nd dimension")
print("2rd array","\n",array_2rd)
print("array_2d , NDim #", array_2rd.ndim)
print("array_2d , shape #", array_2rd.shape)
print("array_2d , size #", array_2rd.size)
print("array_2d , Datatype #", array_2rd.dtype)
print("\n")

# reshaping
print("reshape array","\n",array_2rd.reshape(5,3))

#Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21
import numpy as np
arr= np.arange(10,22)
reshaped=arr.reshape((3,4))
print(reshaped)
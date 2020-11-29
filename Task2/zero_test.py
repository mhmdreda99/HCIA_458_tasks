#Write a NumPy program to test whether none of the elements of a given array is zero

import numpy as np 
arr= np.array([34, 56, 89, 23, 69, 980, 567]) 

print(arr) 
#check for zero
print(np.all(arr)) 
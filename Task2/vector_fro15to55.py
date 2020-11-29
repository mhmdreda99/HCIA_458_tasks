#Write a NumPy program to create a vector with values ranging 
# from 15 to 55 and print all values except the first and last

import numpy as np
vect = np.arange(15,55)
print("creating vector in range of 15 to 55:\n")
print(vect)
print("\nAll values except the first and last of the said vector:\n")
print(vect[1:-1])
  
# Input height from user
print("Input the height you would like:", end = " ")
h = int(input())

s = h - 1

for f in range(h):
# Nested loop to print space every line and reduce its number per line
    for j in range(s):
        print(end = " ")
    s = s - 1
  
# Nested loop to print '#' every line
    for i in range(0, f+1): 
          
            # printing stars, we add a space using end = " " 
        print("#", end=" ")
    print("\r")
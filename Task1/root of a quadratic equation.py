# Take Inputs: 

a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))
#get the roots
d = (b*b - 4*a*c)**0.5
x1 = (-b + d)/(2*a)
x2 = (-b - d)/(2*a)
print('\r\nthe root of a quadratic equation ARE:')
print('x1: {0}'.format(x1))
print('x2: {0}'.format(x2))



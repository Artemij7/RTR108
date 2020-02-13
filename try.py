x=int(input('Please, enter number: '))
y=int(input('Please, enter second number: '))
if 0 < x and x < 10:
    print('x is positive single-digit number.')

if x > 0 :
    print('x is positive')
if x < 0 :
    pass
if x%2 == 0 :
    print ('x is even')
else :
    print('x is odd')
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

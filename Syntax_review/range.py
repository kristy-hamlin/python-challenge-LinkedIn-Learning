
print('Count backwards from 20 to 10 in steps of 2 --------')

start = 20
stop = 10
increment = -2

if increment < 0:
    for i in range(start, stop - 1, increment):
        print(i)
elif increment > 0:
    for i in range(start, stop + 1, increment):
        print(i)
else:
    print('increment cannot = 0. Enter valid input.')

print('Count from 0 to 10 in steps of 2 --------')

start = 0
stop = 10
increment = 2

if increment < 0:
    for i in range(start, stop - 1, increment):
        print(i)
elif increment > 0:
    for i in range(start, stop + 1, increment):
        print(i)
else:
    print('increment cannot = 0. Enter valid input.')

print('Count backward form 30 to 0 in steps of 5 -------')

start = 30
stop = 0
increment = -5

if increment < 0:
    for i in range(start, stop - 1, increment):
        print(i)
elif increment > 0:
    for i in range(start, stop + 1, increment):
        print(i)
else:
    print('increment cannot = 0. Enter valid input.')

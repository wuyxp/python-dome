for value in range(1,5):
    print value

number = list(range(1,10,2))
print number

number = [range(1,10,3)]
print number

number = range(1,10,4)
print number

squares = []
for value in range(1,6,1):
    squares.append(value**2)
print squares

new_squares = [value**2 for value in range(1,6,1)]
print new_squares
operations = ['--x', 'x++', 'x++']
x = 0

for i in range(len(operations)):
    if operations[i] == '--x' or operations[i] == 'x--':
        x =  x-1
    elif operations[i] == '++x' or operations[i] == 'x++':
        x = x+1
print(x)
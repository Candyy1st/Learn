x = ['1st', '2nd', '3rd']
y = ['Aplha', 'Bravo', 'Charlie']

a = 0
b = 0

for i in x:
    for j in y:
        print(x[a], y[b])
        a += 1
        b += 1
        break
    # a += 1
    # b += 1
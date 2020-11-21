file = open('file.txt','w') # Open and Write the file
x = ['black', 'blue']
for item in x:
    file.write(item + '\n')
file.close()

file = open('file.txt', 'r') # Open and Read the file
x = file.read()

print(x)
import re
file_name = input('Please insert your file name: ')
try:
    file_open = open(file_name)
except:
    print("File doesn't exsit:")
    exit()
sum = 0
counter = 0
for lines in file_open:
    numbers = re.findall('[0-9]+',lines)
    for number in numbers:
        sum = sum + int(number)
        counter = counter + 1
        print(int(number))
print('Sum:',sum)
print('Counter:',counter)

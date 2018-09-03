import re

x = open(input("Enter File: \n")).read()
y = re.findall('[0-9]+', x)
sum = 0
for i in y:
    sum += float(i)
print(sum)

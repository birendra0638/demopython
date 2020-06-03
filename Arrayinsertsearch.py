#Demonstarte the concept of array
from array import *
userInArr = array('i',[])
arrLength = int(input("Enter length of the array"))
print(arrLength)

for i in range(arrLength):
    arrValue = int(input("Enter the value for array"))
    userInArr.append(arrValue)
print(userInArr)


searchInput = int(input("Enter value to search"))
count=0
for i in userInArr:
    if i == searchInput:
        print(count)
        break
    count += 1
else:
    print("element not found")


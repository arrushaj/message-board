from cs50 import get_int

number = get_int("Number: ")

length = len(str(number))

total = 0
checksum = 0
j = 1
for i in range(0, length, 2):
    digit = int()

j = 2
for k in range(1, length, 2):
    digit = number % (10^j)
    checksum = checksum + total + digit
    j = j + 2

print(checksum)
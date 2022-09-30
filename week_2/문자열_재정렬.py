import sys

string = list(sys.stdin.readline().rstrip())
numbers = [str(i) for i in range(0, 10)]

string.sort()

number = 0
while string[0] in numbers:
    number += int(string.pop(0))

print("".join(string) + str(number))


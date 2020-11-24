count = 0
first = input("Please enter lower bound: ") 
last = input("Please enter upper bound: ")
first = int(first)
last = int(last)
n = first
while n <= last:
    if n % 5 == 0:
        count = count + 1
    elif n % 3 == 0:
        count = count + 1
    n = n + 1
print("Value divisbile by 3 or 5:", count)

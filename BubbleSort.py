import time
start = time.time()

list1 = [1, 6, 54, 67, 78, 3, 24]

while True:
    sorted = True
    for n in range(0, len(list1)-1):
        if list1[n] > list1[n+1]:
            list1[n], list1[n+1] = list1[n+1], list1[n]
            print(list1)
end = time.time()
print(end - start)

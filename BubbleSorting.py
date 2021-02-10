#BubbleSortingAlgorithm

n = int(input("Enter n: ").strip())
a = list(map(int, input().strip().split(' ')))


count = 0
for i in range(n):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j + 1]= a[j + 1],a[j]
            """temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp"""
            count += 1
print(a)
print("Array is sorted in",count,"swaps.")
print("First Element:", a[0])
print("Last Element:", a[-1])
#6
#45 25 12 3 9 5
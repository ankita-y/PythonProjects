#Binary search in python
def search(arr,low,high,x):
    if high >= low:
        #divided the list into equal part
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        #if element is smaller than mid element then it will definately present in left subarray
        elif arr[mid]>x:
            return search(arr,low,mid-1,x)
        #if element is larger than mid element then it will definately present in right subarray
        else:
            return search(arr,mid+1,high,x)
    else:
        return -1


arr = [12,58,10,20,30,98,11,5,78,85]
x = 58
arr.sort()
print(arr)
print(search(arr,0,(len(arr)-1),x))

a = [0, 1, 2, 3]
print(a[-1])
for a[-1] in a:
    print(a[-1])
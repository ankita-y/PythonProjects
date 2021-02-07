#Linear search in python - it traverse from index 0 and search for the number in the list

def search(arr,n):
    for i in range(len(arr)):
        if arr[i] == n:
            return i
    return -1

#Traverse through tuple items
def search_tuple(tup,n):
    for i in range(len(tup)):
        if tup[i] == n:
            return i
    return -1

arr = [10,20,65,36,98,45,78,101]
tup = (12,25,63,'sacin',25,'Ritu')
print(search(arr,65))
print(search(arr,98))
print(search(arr,95))
print(search(tup,63))
print(search(tup,'sacin'))

#Time complexity of linear search is o(n)*




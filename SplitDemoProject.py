fname = input("Enter file name:")
fh = open(fname)
lst1 = list()
lst2 = list()
for line in fh:
    lst1 = line.split()
    for word in lst1:
        if word not in lst2:
            lst2.append(word)

lst2.sort()
print(lst2)

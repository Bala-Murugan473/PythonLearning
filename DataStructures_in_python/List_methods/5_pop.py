# remove and return the item from at the given position,
# if no index mentioned, it removes and return the last element
# we can also use reverse index
l = [1,2,3,4]
l.pop(1)
print(l)

# if the given index is not present, Index Error will occur
l.pop(8)
print(l)

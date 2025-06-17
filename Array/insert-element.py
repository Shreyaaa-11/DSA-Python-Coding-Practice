arr = [1,2,3,4,5]

def insert_element(arr, index, successor):
  for i in range(index, len(arr)):
    arr[index], successor = successor, arr[index]
  arr.append(successor)

print("Array before insertion:", arr)
insert_element(arr,3,6)
print("Array after insertion:", arr)

#Approach:
# Start swapping from the given index to the end of the list.
# Swap current element with successor
# arr[index] gets the new value, successor holds the old one to pass ahead
# After loop, the last original element is stored in successor
    # Append it to the end of the list to preserve all elements
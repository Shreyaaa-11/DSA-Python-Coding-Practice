def search_element(arr, element):
  for i in range(len(arr)):
                 if arr[i] == element:
                  return i
  return -1

arr = [1, 2, 3, 4, 5]
element = 3

print("Array searched:", arr)
print("Element searching for:", element)
print("Searched index is:", search_element(arr, element))
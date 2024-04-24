def insertion_sort(arr):
 for i in range(1, len(arr)):
  key = arr[i]
  j = i - 1
  
  # Move elements of the sorted part to make space for the key
  while j >= 0 and key < arr[j]:
   arr[j + 1] = arr[j]
   j -= 1
 
   # Insert the key into its correct position
   arr[j + 1] = key

# Example usage:
arr = [27, 34, 88, 1, 99, 77, 9, 8, 47, 66]
print("Original array:", arr)
# Perform insertion sort
insertion_sort(arr)
print("Sorted array:", arr)

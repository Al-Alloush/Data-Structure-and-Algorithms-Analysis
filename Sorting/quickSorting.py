
def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            # Switching between the values
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)
 

def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # start sorting the array, at the first time is one part, later after the function 
        # partition return the new value for the pivot to use it in sorting the entier part that 
        # generate from the previous partition
        pivot = partition(arr, low, high)
 
        # Separately sort elements before partitin to two part and after partition
        # the part 1
        quick_sort(arr, low, pivot-1)
        # part 2
        quick_sort(arr, pivot+1, high)
 
 
# Driver code to test above
arr = [6, 7, 9, 17, 4, 10]
arrLingth = len(arr)
quick_sort(arr, 0, arrLingth-1)
print("Array after sorted:"+ str(arr))
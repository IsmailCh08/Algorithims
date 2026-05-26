
def binary_Search(arr, number):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high+low) // 2
        if number == arr[mid]:
            return arr[mid]
        elif number > arr[mid]:
            low = mid + 1
        elif number < arr[mid]:
            high = mid - 1 
    return "not in list"



print(binary_Search([1,2,3,5,7,8,9], ))

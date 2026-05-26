
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
        else:
            print('Your number is not in the array')
    return None

print(binary_Search([1,2,3,5,8,7,9], 1))

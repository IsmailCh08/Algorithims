
def binary_Search(arr, number):
    low = 0
    high = len(arr) - 1
    guess = high // 2
    while low <= high:
        if number == arr[guess]:
            print('{arr[guess]} is your number ')
        elif number > arr[guess]:
            high += 1
        elif number < arr[guess]:
            low += 1
        else:
            print('Your number is not in the array')

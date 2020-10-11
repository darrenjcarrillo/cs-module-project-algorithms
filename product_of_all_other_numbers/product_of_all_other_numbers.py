'''
Input: a List of integers
Returns: a List of integers
'''

import math


def product_of_all_other_numbers(arr):
    # Your code here
    # loop over array
    # Multiply every element to each other starting at index 1
    # then multiply each element this time starts at index 0 then skipping index 1.
    new_arr = []
    start_of_arr = []

    for i in range(len(arr)):
        # assign start_of_arr to array starting at index 0
        start_of_arr = arr[0:]
        # print(start_of_arr)
        # popped all elements starting on first element in the old array on every loop
        start_of_arr.pop(i)
        # print(start_of_arr)
        # append start_of_arr elements to new_arr and calculate the product of all elements on every loop
        new_arr.append(math.prod(start_of_arr))

    return new_arr


print(product_of_all_other_numbers([1, 7, 3, 4]))


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8,
           9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(
        f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

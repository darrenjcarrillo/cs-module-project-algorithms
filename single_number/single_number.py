'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # # Your code here
    # create variable to store the single number
    num = 0
    # print(f'This is old num --> {num}')
    # loop over array
    for i in arr:
        # print(f'This is item {i}')
        # using count() in the array to look for the single number
        if arr.count(i) <= 1:
            # print(f'This is num inside of the loop-->{num}')
            # print(f'This is Item inside if statement {i}')
            # assign i to num
            num = i
            # print(f'Newest num {num}')
    return num


print(single_number([1, 1, 2, 3, 3]))

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")


# if the input number does not have a copy/or same number return the number that does not have a copy/same number

### PLAN ###
# loop over the array
# compare each elements to each other
# return the number that does not have a copy.

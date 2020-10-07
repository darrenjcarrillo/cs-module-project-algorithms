'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):
    # # Your code here
    dupe_num = set()

    for i in arr:
        if i not in dupe_num:
            dupe_num.add(i)
        else:
            dupe_num.remove(i)

    return dupe_num


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

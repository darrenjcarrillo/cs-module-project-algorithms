'''
Input: a List of integers
Returns: a List of integers
'''


def moving_zeroes(arr):
    # Your code here
    # loop over array
    # for each integer compare to zero if it is move to end of the array
    # if not move to front of the array.
    # popped_element = 0

    # for i in range(len(arr)):
    #     if arr[i] == 0:
    #         # print(f'This is i', arr[i])
    #         arr[i] = popped_element
    #         # print(f'popped', popped_element)
    #         arr.pop(i)
    #         arr.append(popped_element)
    # return arr

    new_arr = []

    for i in arr:
        # print(f'i', i)
        if i != 0:
            # insert numbers other than zero in the new_arr array
            new_arr.insert(0, i)
            # print(f'new_arr', new_arr)
        else:
            # after every loop if its zero append to end or new_arr array.
            new_arr.append(0)
    return new_arr


print(f'moving zeroes {moving_zeroes([1, 0, 2, -2, 0, 3])}')

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

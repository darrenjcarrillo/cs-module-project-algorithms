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
    #         arr[i] = popped_element
    #         arr.pop(i)
    #         arr.append(popped_element)
    # return arr

    popped_element = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            # print(f'This is i', arr[i])
            arr[i] = popped_element
            popped_element = arr[i]
            # print(f'popped', popped_element)
            arr.pop(i)
            arr.append(popped_element)
    return arr


print(f'moving zeroes {moving_zeroes([1, 0, 2, -2, 0, 3])}')

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    # Your code here
    cookies = n
    total = 0

    if cookies > 3:
        total += eating_cookies(n-3)
        total += eating_cookies(n-2)
        total += eating_cookies(n-1)
        return total

    elif cookies == 3:
        return 4
    elif cookies == 2:
        return 2
    else:
        return 1


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")

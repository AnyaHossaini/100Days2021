"""
Author: Anya Hossaini
Date: 12.15.2020

Problem: Find the sum of all the multiples of 3 or 5 below 1000.
Coding Language: Python
"""
if __name__ == '__main__':
    result = 0

    # Starts at 0 and ends at 1000
    for i in range(0, 1000):
        # if the reminder is 0 then add to the result value
        if i % 3 == 0 or i % 5 == 0:
            result += 1

    # Prints out the result
    print(result)



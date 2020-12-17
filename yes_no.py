"""

Author: Anya Hossaini
Date: 12.15.2020-12.16.2020

Problem: Write a code that receives an array of numbers or strings, goes one by one through it while taking one value
out, leaving one value in, taking, leaving, and back again to the beginning until all values are out.
It's like a circle of people who decide that every second person will leave it, until the last person is there.
So if the last element of the array is taken, the first element that's still there, will stay.
The code returns a new re-arranged array with the taken values by their order.
The first value of the initial array is always taken.

Coding Language: Python

"""

import itertools as it


import itertools as it


def yes_no(arr):

    copyArr = arr[:]
    newArr = []

    taking = it.cycle([True, False])
    while copyArr:
        oddEle = []
        evenEle = []

        for x in copyArr:
            if next(taking):
                oddEle.append(x)
            else:
                evenEle.append(x)
        newArr += oddEle
        copyArr = evenEle
    return newArr


if __name__ == '__main__':

    # Creates an empty array
    setArr = []

    # Receives input from user --> Converts it to an int
    ArrLen = input("Enter number of elements in array: ")
    ArrLen = int(ArrLen)

    # If the user inputs an invalid number
    while ArrLen <= 0:
        print("Invalid number")
        ArrLen = input("Enter number of elements in array: ")
        ArrLen = int(ArrLen)

    # Ask user to input elements for the array they created
    for i in range(0, ArrLen):
        IndexArr = input("Input element: ")
        setArr.append(IndexArr)

    print(yes_no(setArr))











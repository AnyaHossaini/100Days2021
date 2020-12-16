"""
Author: Anya Hossaini
Date: 12.15.2020

Problem: Complete the solution so that it returns true if the
first argument(string) passed in ends with the 2nd argument (also a string).

Coding Language: Python
"""


def solution(string, ending):

    return string.endswith(ending)


if __name__ == '__main__':
    firststr = input("Enter first string: ")
    secondstr = input("Enter second string: ")
    print(solution(firststr, secondstr))

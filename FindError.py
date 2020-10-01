'''
Author = Zeeshan
Date = 11:14:2020
Purpose = To create a program to find the wrong element of the table of a number
'''


import random

def falseMultiplication(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] * random.randint(1, 10)
    return table

def isCorrect(table, number):
    for i in range(1,11):
        if table[i-1] != i * number:
            return i-1
    return None
if __name__ == "__main__":
    # print(falseMultiplication(7))
    number = int(input("Enter a number:\n"))
    myTable = falseMultiplication(number)
    print(myTable)
    wrongIndex = isCorrect(myTable, number)
    print(f"The table is wrong at index {wrongIndex}")


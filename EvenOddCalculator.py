import sys
from collections import Counter

myEvenNum = 0
myOddNum = 0
myBiggestNum = 0
even_count, odd_count = 0,0

try:
    print(sys.argv[1])
    #list1 = [int(i) for i in sys.argv[1].split(',')]
    list1 = sys.argv[1].split(',')
    print(list1)
    for number in list1:

        if int(number) % 2 == 0:
            myEvenNum += int(number)
            even_count += 1
        else:
                myOddNum += int(number)
                odd_count += 1

        # if int(number) > myBiggestNum:
        #     myBiggestNum = int(number)
        while int(number) > myBiggestNum:
            myBiggestNum = int(number)


    mySmallestNum = min(list1)
    myNumDiff = myBiggestNum - mySmallestNum
    list_copy = list1.copy()
    if len(list1) > 2:
        list_copy.remove(max(list_copy))
        list_copy.remove(min(list_copy))

    def meanNum(list):
        return sum(list) / len(list)

    myMean = meanNum(list_copy)
    # print(int(myMean))
    # print(myEvenNum)
    # print(myOddNum)
    # print(myBiggestNum)
    # print(mySmallestNum)
    # print(myNumDiff)
    # print(even_count, odd_count)

    #print(f"The sum of all even numbers is {myEvenNum}, the sum of all odd numbers is {myOddNum}, the difference between the biggest and smallest number is {myNumDiff}, the total number of even numbers is {even_count}, the total number of odd numbers is {odd_count}, the centered average is {int(myMean)}.")

except ValueError:
    print('Please enter valid integers.')




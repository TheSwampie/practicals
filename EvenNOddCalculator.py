import sys

myEvenNum = 0
myOddNum = 0
myBiggestNum = 0
even_count, odd_count = 0,0

try:
    for number in sys.argv[1:]:

        if int(number) % 2 == 0:
            myEvenNum += int(number)
            even_count += 1
        else:
                myOddNum += int(number)
                odd_count += 1

        while int(number) > myBiggestNum:
            myBiggestNum = int(number)

    list1 = [int(i) for i in sys.argv[1:]]
    mySmallestNum = min(list1)
    myNumDiff = myBiggestNum - mySmallestNum
    list_copy = list1.copy()
    if len(list1) > 2:
        list_copy.remove(max(list_copy))
        list_copy.remove(min(list_copy))

    def meanNum(list):
        return sum(list) / len(list)

    myMean = meanNum(list_copy)

    print(f"The sum of all even numbers is {myEvenNum}, the sum of all odd numbers is {myOddNum}, the difference between the biggest and smallest number is {myNumDiff}, the total number of even numbers is {even_count}, the total number of odd numbers is {odd_count}, the centered average is {int(myMean)}.")

except ValueError:
    print('Please enter valid integers.')
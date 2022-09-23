from collections import Counter

# person_weight = input("What is your weight: ")
# choice = input("(L)bs or (K)g: ")
# kg_to_pound = float(person_weight) * 2.204
# pound_to_kg = float(person_weight) * 0.453
#
# if choice.lower() == "l":
#     print("You are: " + str(pound_to_kg) + " kg")
# elif choice.lower() == "k":
#     print("You are: " +  str(kg_to_pound) + " poun  ds")

#This is using file IO to open the text file
txtfile = open('Lab2_testData.txt', 'r')
#This is to get the long string in the text file and put it into a variable called file_content
file_content = txtfile.read()
#This is to split the string in the text file by commas.
myString = file_content.split(",")
#Passing the string into an instance of the Counter class to count the string
Counter = Counter(myString)
#Using the Counter class to get most common number of word that appeared
most_occurs = Counter.most_common(5)

print(most_occurs)
txtfile.close()
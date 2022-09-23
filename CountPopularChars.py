import sys
from collections import Counter

myString = str(sys.argv[1])
mySortedString = sorted(myString.lower())
# Print mySortedString to see that it is a list.
# Print(mySortedString)
# Initializing a variable called Counter to pass my string into the class.
Counter = Counter(mySortedString)
# Print the variable "Counter" to see the key value as it is now a dictionary
# print(Counter.keys())
most_count = Counter.most_common(5)
print(most_count)

# for x,y in Counter.most_common(5):
#     print(x + ':',y)

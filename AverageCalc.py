import sys

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])

    avg = (a + b + c) / 3

    print("Average:%0.2f"%avg)

except ValueError:
    print("Your input is invalid!")
except IndexError:
    print("Your input is invalid")
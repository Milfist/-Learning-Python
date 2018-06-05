import sys

if len(sys.argv) < 2:
    print("ERROR: The input data is incorrect.")
    print("Example: decomposition.py [0-99999]")
else:
    number = int(sys.argv[1])

    if number > 99999 or number < 0:
        print("ERROR: The input data is incorrect.")
        print("Example: decomposition.py [0-99999]")
    else:
        string = str(number)
        length = len(string)

        for index in range(length):
            print("{:04d}".format(int(string[length - 1 - index]) * 10 ** index))
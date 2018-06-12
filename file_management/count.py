from io import open
import sys

file = open("count.txt", "a+")
file.seek(0)
content = file.readline()

if len(content) == 0:
    content = "0"
    file.write(content)

file.close()

try:
    count = int(content)

    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            count += 1
        elif sys.argv[1] == "dec":
            count -= 1

    print(count)

    file = open("count.txt", "w")
    file.write(str(count))
    file.close()

except:
    print("Error: corrupt file.")

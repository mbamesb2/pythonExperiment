
#!/usr/bin/python

import sys
import random
import string
import array


for x in range(3):

    s = ""
    for i in range(10):
        s += random.choice(string.ascii_lowercase)

    print s
    print " "

    nameFileArray = ["thisFile", "myFile", "randomFile"]
    fo = open(nameFileArray[x], "wb")
    fo.write(s);


    fo.close()

for c in range(2):
    num1 = (random.randint(1,42))
    num2 = (random. randint(1,42))

print num1
print " "
print num2
print " "
print num1 * num2
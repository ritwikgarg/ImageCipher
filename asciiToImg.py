# Program: asciiToImg.py

# This script takes a text file and coverts it to
# a 256x256 pixel image. The text is encoded by 
# using the ascii value of the characters as either
# the red, green or blue values in the image.

from PIL import Image
from random import randint

def rgbScrambler(pt,x,y,i):
    scrambleType = {
        0:(pt,x,y),
        1:(y,pt,x),
        2:(x,y,pt)
    }
    return scrambleType.get(i%3)

# Creating a new Image, and a pixel map.
img = Image.new('RGB',(256,256),color = (0,0,0))
pixels = img.load()

# Reading the text from text file that we want to encrypt.
with open("msg.txt", "r", encoding = "ASCII") as file:
    msg = file.read()

# Encoding the text message in UTF-8 i.e. saving ASCII value of each character into array pt
pt = msg.encode('ascii')
print("Byte Array:")
print(pt)
print()

xPts = [0]
yPts = [0]

for i in range(0, len(pt)):
    x = randint(0,254)
    y = randint(0,254)
    while((x in xPts)and(y in yPts)):
        # if duplicate pair is found, get a new pair
        x = randint(0,254)
        y = randint(0,254)
    # add new unique points to list
    xPts.append(x)
    yPts.append(y)
    pixels[xPts[i],yPts[i]] = rgbScrambler(pt[i],x,y,i)
img.save('msgImg.png')
r,g,b = pixels[0,0]

i=0
for i in range(0,len(pt),3):
    print(repr(msg[i])+": R: %s G: %s B: %s" % (str(r), str(g), str(b)))
    i+=1

    r,g,b = pixels[g,b]
    print(repr(msg[i])+": R: %s G: %s B: %s" % (str(r), str(g), str(b)))
    i+=1

    r,g,b = pixels[b,r]
    print(repr(msg[i])+": R: %s G: %s B: %s" % (str(r), str(g), str(b)))
    i+=1

    r,g,b = pixels[r,g]

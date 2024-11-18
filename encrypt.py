# Program: encoder.py

# This script takes the encrypted message image,
# the private key image, and a public image and
# combines the three.

from PIL import Image
from random import randint

# Import/create images and their pixel maps. 
# The images are also resized to 256 x 256.
PK = Image.open("pk.png","r")   
PK = PK.resize((256,256),Image.LANCZOS)
PKrgb = PK.convert("RGB")

MSG = Image.open("msgImg.png","r")
MSGrgb = MSG.convert("RGB")

PUB = Image.open("pub.png","r")
PUB = PUB.resize((256,256),Image.LANCZOS)
PUBrgb = PUB.convert("RGB")

ENCRimg = Image.new('RGB',(256,256),color = (0,0,0))
ENCRpixels = ENCRimg.load()

# Create text files for each image which store the RGB values for each pixel
msgimgtxt = open("msgimg.txt","w+")
pubtxt = open("pub.txt","w+")
pktxt = open("pk.txt","w+")
enctxt = open("enc.txt","w+")

for i in range(0,256):
    for j in range(0,256):
        # Get RGB values from all three images
        pubR,pubG,pubB = PUBrgb.getpixel((i,j))
        priR,priG,priB = PKrgb.getpixel((i,j))
        msgR,msgG,msgB = MSGrgb.getpixel((i,j))

        # Write RGB values to txt file for each image
        msgimgtxt.write("[%d][%d](%d,%d,%d)\n" %(i,j,msgR,msgG,msgB))
        pubtxt.write("[%d][%d](%d,%d,%d)\n" %(i,j,pubR,pubG,pubB))
        pktxt.write("[%d][%d](%d,%d,%d)\n" %(i,j,priR,priG,priB))
        
        # Calculate new encrypted image RGB values
        ENCRpixels[i,j] = (
            (int(pubR/2) + int(priR/2) + msgR)%255,
            (int(pubG/2) + int(priG/2) + msgG)%255,
            (int(pubB/2) + int(priB/2) + msgB)%255
        )
        #Write the rgb values to text file of final encrypted image
        enctxt.write("[%d][%d](%d,%d,%d)\n" %(i,j,ENCRpixels[i,j][0],ENCRpixels[i,j][1],ENCRpixels[i,j][2]))
        

#close/save all files
msgimgtxt.close()
pubtxt.close()
pktxt.close()
enctxt.close()
ENCRimg.save("enc.png")
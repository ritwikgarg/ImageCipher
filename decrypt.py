
# Program: decrypt.py
# This program takes an encrypted image, public key image, 
# and private key image then performs decryption algorithm
# to extract the message that was encrypted.

from PIL import Image
decrypted_message = open("decryptedMessage.txt","w+")


# Open images and load them into memory
EncryptedImage = Image.open('enc.png')
encRGB         = EncryptedImage.convert("RGB")

privateKey     = Image.open('pk.png')
PK = privateKey.resize((256,256),Image.LANCZOS)
priRGB         = PK.convert("RGB")

publicKey      = Image.open('pub.png')
PUK = publicKey.resize((256,256),Image.LANCZOS)
publRGB        = PUK.convert("RGB")

DECRimg = Image.new('RGB',(256,256),color = (0,0,0))
DECRpixels = DECRimg.load()


# Initialize a 2d array to save decrypted pixels
decryptedPixel = [[]]
decryptedPixel = [[0 for i in range(256)] for i in range(256)]

# Start processing images
for i in range(0,256):
    for j in range(0,256):
        # Get the pixel value at a given position
        pubR,pubG,pubB = publRGB.getpixel((i,j))
        encR,encG,encB = encRGB.getpixel((i,j))
        priR,priG,priB = priRGB.getpixel((i,j))


        # Decryption Algorithm
        msgR = int(int(encR) - int(pubR/2) - int(priR/2))
        msgG = int(int(encG) - int(pubG/2) - int(priG/2))
        msgB = int(int(encB) - int(pubB/2) - int(priB/2))
        if( msgR < 0):
            msgR =  msgR  + 255
        if( msgG < 0):
            msgG =  msgG  + 255
        if( msgB < 0):
            msgB =  msgB + 255
        
        # Save the decoded RGB values into a list to access later
        DECRpixels[i,j] = (msgR,msgG,msgB)
        decryptedPixel[i][j] = int(msgR),int(msgG),int(msgB)


DECRimg.save("dec_real.png")
# Message extraction algorithm
msgCount = 0
Xa = 0
Ya = 0

while(True):
    message = decryptedPixel[Xa][Ya][msgCount%3]
    newXa   = decryptedPixel[Xa][Ya][(msgCount+1)%3]
    Ya      = decryptedPixel[Xa][Ya][(msgCount+2)%3]
    Xa      = newXa

    msgCount = msgCount + 1
    if(Xa == 0 and Ya == 0):
        break
    print("%c" %(message),end = "")
    decrypted_message.write("%c" % (message))


decrypted_message.close()
EncryptedImage.close()
publicKey.close()
privateKey.close()
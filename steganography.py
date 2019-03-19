"""
This is a solution to the digital image steganography assignment. You can delete
as much of it as you want and leave the rest as starter code for your students
to fill in.  You can see an example of starter code by looking at the file
steganography_starter_code.py

In this assignment, students implement code to hide one image inside of another 
and then reveal this hidden image through the reverse process.  It's fun to give
students hidden messages that they have to reveal. To go one step further, these
hidden messages might be clues to find "treasures" hidden around campus.  

"""



import os
from PIL import Image
import time


def colorReduction(filename):
    """ reduces the number of colors in a png image (filename) from over
        16 million (256^3) to just 64 colors (4^3).  The red,green,
        blue values of each pixel will be either 0,85,170,255 depending
        on which value it is closest to.  Better choices probably
        exist than the scheme here, and you are encouraged to 
        play around with the algorithm to get better color reduced versions
        of the original
        For example, colorReduction("fox.png") will produce a color-reduced
        png image file called "fox_reduced.png"
    """
    #Im_pix = getRGB("fox.png")  # read in the in.png image
    Im_pix = getRGB(filename)  # read in the in.png image
    #print( "The first two pixels of the first row are", )
    #print( Im_pix[0][0:2] )
    # remember that Im_pix is a list (the image)
    # of lists (each row) of tuples (each pixel is (R,G,B)    

    for r in range(len(Im_pix)): # do this number of row times
      for c in range(len(Im_pix[r])): # iterate through the rth row
            rgb = Im_pix[r][c] #  [0][0], [0][1], ...
                                #   [1][0], [1][1],...
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            if red > 212:
                red = 255
            elif red > 128:
                red = 170
            elif red > 43:
                red = 85
            else:
                red = 0

            if green > 212:
                green = 255
            elif green > 128:
                green = 170
            elif green > 43:
                green = 85
            else:
                green = 0

            if blue > 212:
                blue = 255
            elif blue > 128:
                blue = 170
            elif blue > 43:
                blue = 85
            else:
                blue = 0


            Im_pix[r][c] = (red, green,blue)

    #saveRGB( Im_pix, "fox_reduced.png")
    saveRGB( Im_pix, filename.replace(".png", "_reduced.png"))

def encryptColor(filename1, filename2):
    '''

    encrypts(hides) filename1 by first applying a color reduction
    algorithm to reduce the colors to one of 64 possible colors.
    This color reduced image is now "hidden"
    into a full colored image(filename2) according to the following scheme:
    If the red, green, or blue value of filename1's pixel is 0,
    set the last two bits of the full color image(filename2) to 00
    If the red, green, or blue value of filename1's pixel is 85,
    set the last two bits of the full color image(filename2) to 01
    If the red, green, or blue value of filename1's pixel is 170,
    set the last two bits of the full color image(filename2) to 10
    If the red, green, or blue value of the filename1's pixel is 255,
    set the last two bits of the full color image(filename2) to 11
    These small changes to the original picture should be imperceptible, yet
    you've stored all the information you need and it the color
    reduced version of filenae1 is "hidden" in the 
    original full color image

    '''
    colorReduction(filename1)
    #reduced_pix = getRGB("fox_reduced.png")
    reduced_pix  = getRGB(filename1.replace(".png", "_reduced.png"))
    print( "The five pixels in the reduced image starting in row 300, column 300 are:" ,)
    print( reduced_pix[300][300:305] )
    #revealed_pix = getRGB( "lizard.png" )  # read in the in.png image
    revealed_pix = getRGB( filename2 )  # read in the full colored image
    print( "The five pixels in the revealed image starting in row 300, column 300 are:" ,)
    print( revealed_pix[300][300:305] )
    # remember that reduced_pix is a list (the image)
    # of lists (each row) of tuples (each pixel is (R,G,B)    

    for r in range(len(reduced_pix)): # do this number of row times
      for c in range(len(reduced_pix[r])): # iterate through the rth row
            rgbHidden = reduced_pix[r][c]   # rgbHidden = (85,170,255)
            rgbNotHidden = revealed_pix[r][c] # rgbNotHidden = (33,34,35)
            rgb = [0,0,0]
            for i in range(0,3):
                hidden = rgbHidden[i]
                notHidden = rgbNotHidden[i]
                binaryColor = "0" + decimal_to_binary(notHidden)
                if hidden == 0:
                    modifiedBinaryColor = binaryColor[:-2] + "00"
                elif hidden == 85:
                    modifiedBinaryColor = binaryColor[:-2] + "01"
                elif hidden == 170:
                    modifiedBinaryColor = binaryColor[:-2] + "10"
                elif hidden == 255:
                    modifiedBinaryColor = binaryColor[:-2] + "11"
                else:
                     print("error at " + str(r) + "," + str(c))
 
                modifiedDecimalColor = binary_to_decimal(modifiedBinaryColor);   
                rgb[i] = modifiedDecimalColor

            #revealed_pix[r][c] = (red,green,blue)
            revealed_pix[r][c] = tuple(rgb)

    saveRGB( revealed_pix, "secret_message.png" )
    print( "The five pixels in the secret message starting in row 300, column 300 are:" ,)
    print( revealed_pix[300][300:305] )

def decryptColor(filename):
    '''

    decrypts filename to reveal the hidden image within
    using the encryption scheme in reverse:
    If the last two bits of the image(filename) is 00,
    set the red, green, or blue value of the pixel to 0.
    If the last two bits of the image(filename) is 01,
    set the red, green, or blue value of the pixel to 85.
    If the last two bits of the image(filename) is 10,
    set the red, green, or blue value of the pixel to 170.
    If the last two bits of the image(filename) is 11,
    set the red, green, or blue value of the pixel to 255.
    You'll see the revealed image as a superlay on the original
    image. 

    '''

    image_pix = getRGB(filename)
    print( "The five pixels starting in row 300, column 300 are:" ,)
    print( image_pix[300][300:305] )
    # remember that reduced_pix is a list (the image)
    # of lists (each row) of tuples (each pixel is (R,G,B)    

    for r in range(len(image_pix)): # do this number of row times
      for c in range(len(image_pix[r])): # iterate through the rth row
            rgb = image_pix[r][c]
            rgb_new = [0,0,0]
            for i in range(0,3):
                #color = rgbHidden[i]
                #notHidden = rgbNotHidden[i]
                #needed for binary represenations with less than 2 digits
                binaryColor = "0" + decimal_to_binary(rgb[i])
                if binaryColor[-2:] == "00":
                    rgb_new[i] = 0
                elif binaryColor[-2:] == "01":
                    rgb_new[i] = 85
                elif binaryColor[-2:] == "10":
                    rgb_new[i] = 170
                elif binaryColor[-2:] == "11":
                    rgb_new[i] = 255
                else:
                    print("error at " + str(r) + "," + str(c))
                #modifiedDecimalColor = binary_to_decimal(modifiedBinaryColor);   
                #rgb[i] = modifiedDecimalColor     
            image_pix[r][c] = tuple(rgb_new)

    saveRGB( image_pix, "revealed_message.png" )
    print( "The five pixels starting in row 300, column 300 are:" ,)
    print( image_pix[300][300:305] )


def binary_to_decimal(bin):
    sum = 0
    pow = 1
    while len(bin) > 0:
        if bin[-1] == '1':
            sum = sum + pow
        pow = pow * 2
        bin = bin[0:-1]
    return sum 

def decimal_to_binary(dec):
    if dec == 0:
        return "0"
    bin = ""
    while (dec > 0):
        digit =  dec % 2
        bin = str(digit) + str(bin)
        dec = dec // 2
    return bin

# all functions that follow are borrowed from Harvey Mudd's CSForAll 
# course (cs5png.py) that are made available to the public.
def saveRGB( boxed_pixels, filename="out.png" ):
    """ need docstrings! """
    print( 'Starting to save', filename, '...' )
    W, H = getWH( boxed_pixels )
    im = Image.new("RGB", (W, H), "black")
    px = im.load()
    for r in range(H):
        #print( ".", end="" )
        for c in range(W):
            bp = boxed_pixels[r][c]
            t = tuple(bp)
            px[c,r] = t
    im.save( filename )
    time.sleep(0.5)
    print( filename, "saved." )

def getRGB( filename="in.png" ):
    """ reads a png file """
    original = Image.open(filename)
    print( "The size of the Image is: " )
    print(original.format, original.size, original.mode)
    WIDTH, HEIGHT = original.size
    px = original.load()
    PIXEL_LIST = []
    for r in range(HEIGHT):
        row = []
        for c in range(WIDTH):
            row.append( px[c,r][:3] )
        PIXEL_LIST.append( row )
    return PIXEL_LIST



def getWH( PX ):
    """ need docstrings! """
    H = len(PX)
    W = len(PX[0])
    return W, H

def binaryIm( s, cols, rows ):
    """ need docstrings! """
    PX = []
    for row in range(rows):
        ROW = []
        for col in range(cols):
            c = int(s[row*cols + col])*255
            px = [ c, c, c ]
            ROW.append( px )
        PX.append( ROW )
    saveRGB( PX, 'binary.png' )
    #return PX

class PNGImage:

    def __init__(self, width, height):
        """ constructor for PNGImage """
        self.width = width
        self.height = height
        default = (255,255,255)
        self.image_data = \
            [ [ default for col in range(width) ] \
                        for row in range(height)]

    def plotPoint(self, col, row, rgb=(0,0,0)):
        """ plot a single point to a PNGImage """
        # check if rgb is a three-tuple
        if type(rgb) == type( (0,0,0) ) and \
           len(rgb) == 3:
            pass # ok
        elif type(rgb) == type( [0,0,0] ) and \
           len(rgb) == 3:
            rgb = tuple(rgb)
        else:
            print( "in plotPoint, the color", rgb )
            print( "was not in a recognized format." )
            
        # check if we're in bounds
        if 0 <= col < self.width and \
           0 <= row < self.height:
            self.image_data[ row ][ col ] = rgb

        else:
            print( "in plotPoint, the col,row:", col, row, )
            print( "was not in bounds." )
            return

        return

    def saveFile( self, filename = "test.png" ):
        """ save the object's data to a file """
        # we reverse the rows so that the y direction
        # increases upwards...
        saveRGB( self.image_data[::-1], filename )









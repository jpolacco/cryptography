# Cryptography

Projects in cryptography for beggining computer science students, with starter code and solutions, in Python. 

## Steganography

In this assignment, students implement code to hide one image inside of another and then reveal this hidden image through the reverse process.  It's fun to give students hidden messages that they then have to reveal. To go one step further, these hidden messages might be clues to find "treasures" hidden around campus. 

To get there, students will first write a few functions to convert binary to decimal and vice versa. Students have access to a color reduction function that we developed in class together.  See the starter code and look for the TODO sections that need to be implemented by the students. Skills needed for this assignment include creating 2D lists, iterating trough 2D lists using nested for loops, and tuples. Students develop a deeper understanding of digital images, pixels, and RGB values.


###  Color Reduction Function

```python
def colorReduction(filename):
    """ reduces the number of colors in a png image (filename) from over
        16 million (256^3) to just 64 colors (4^3).  The red,green,
        blue values of each pixel will be either 0,85,170,255 depending
        on which value it is closest to.  Better choices probably
        exist than the scheme here, and you are encouraged to 
        play around with the algorithm to get better color reduced versions.
        For example, colorReduction("fox.png") will produce a color-reduced
        png image file called "fox_reduced.png"
    """
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

    saveRGB( Im_pix, filename.replace(".png", "_reduced.png")
```

### Video List

[Images, Pixels, and RGB](https://www.youtube.com/watch?v=15aqFQQVBWU)

#IMPORT
from sense_hat import SenseHat
from time import sleep
from random import choice

class SenseOutput:
    #create sense hat
    sense = SenseHat()
    
    #setup colours
    r = (255, 0, 0)
    g = (0, 255, 0)
    w = (255, 255, 255)
    p = (255, 105, 180)
    w = (128, 128, 128)
    e = (0, 0, 0)
    b = (0, 0, 255)

    #setup class variables to store the matrix images
    #an image (however bad) of a rat/mouse
    rat = [
    e,e,e,e,e,e,e,e,
    w,w,w,e,w,w,w,e,
    w,p,w,e,w,p,w,e,
    w,w,w,w,w,w,w,e,
    w,w,r,w,r,w,w,e,
    e,w,w,w,w,w,e,e,
    e,e,w,w,w,e,e,e,
    e,e,e,p,e,e,e,e
    ]

    #an image of a rat with a red cross through it
    noRat = [
    r,e,e,e,e,e,e,r,
    w,r,w,e,w,w,r,e,
    w,p,r,e,w,r,w,e,
    w,w,w,r,r,w,w,e,
    w,w,w,r,r,w,w,e,
    e,w,r,w,w,r,e,e,
    e,r,w,w,w,e,r,e,
    r,e,e,p,e,e,e,r
    ]

    #no image - used to clear the led matrix
    empty = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

    #a green tick - used to signify success
    tick = [
    e,e,e,e,e,e,e,g,
    e,e,e,e,e,e,g,g,
    e,e,e,e,e,g,g,e,
    e,e,e,e,g,g,e,e,
    g,e,e,e,g,e,e,e,
    g,g,e,g,g,e,e,e,
    e,g,g,g,e,e,e,e,
    e,e,g,e,e,e,e,e
    ]

    #a red cross used to signify failure
    cross = [
    r,e,e,e,e,e,e,r,
    e,r,e,e,e,e,r,e,
    e,e,r,e,e,r,e,e,
    e,e,e,r,r,e,e,e,
    e,e,e,r,r,e,e,e,
    e,e,r,e,e,r,e,e,
    e,r,e,e,e,e,r,e,
    r,e,e,e,e,e,e,r
    ]

    #initialising the class
    #requires a name - isnt curently use but thought
    #that we might use the name somewhere as output so
    #included it
    def __init__(self, name):
        self.name = name
    
    #displays a green tick on the matrix
    #length - currently for itteraing (a makeshift timer) cand probably use a propper timer
    def displayTick(self, length):
        count = 0
        while (count < length):
            self.sense.set_pixels(self.tick)
            count = count + 1
        self.sense.set_pixels(self.empty)

    #displays a red cross
    #length - currently for itteraing (a makeshift timer) cand probably use a propper timer
    def displayCross(self, length):
        count = 0
        while (count < length):
            self.sense.set_pixels(self.cross)
            count = count + 1
        self.sense.set_pixels(self.empty)

    #displays the rat graphic
    #length - currently for itteraing (a makeshift timer) cand probably use a propper timer
    def displayRat(self, length):
        count = 0
        while (count < length):
            self.sense.set_pixels(self.rat)
            count = count + 1
        self.sense.set_pixels(self.empty)

    #displays the rat with a cross graphic
    #length - currently for itteraing (a makeshift timer) cand probably use a propper timer
    def displayNoRat(self, length):
        count = 0
        while (count < length):
            self.sense.set_pixels(self.noRat)
            count = count + 1
        self.sense.set_pixels(self.empty)
    
#sense.show_message("Rat Caught", text_colour=[100,100,100])

o = SenseOutput("Duncan")
o.displayTick(1000)
o.displayCross(1000)
o.displayRat(1000)
o.displayNoRat(1000)

exit()



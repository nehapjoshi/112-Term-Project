#Animation Starter Code from http://www.cs.cmu.edu/~112/notes/notes-animations-part2.html

from tkinter import *
import buttons
import os

def init(data):
    data.title = "Galaxy Sorting"
    data.slideNum = 0
    data.margin = data.height//50
    loadGalaxyImages(data) #loads all necessary images
    data.spiralButton = (2*data.width/3, data.height /4)
    data.irregularButton = (2*data.width/3, data.height /2)
    data.ellipticalButton = (2*data.width/3, 3*data.height /4)
    data.bulgeButton = (2*data.width/3, data.height /4)
    data.barButton = (2*data.width/3, data.height /2)
    data.ringButton = (2*data.width/3, 3*data.height /4)

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if event.keysym == "Right":
        data.slideNum += 1
    elif event.keysym == "Left":
        data.slideNum -= 1

def timerFired(data):
    pass

def redrawAll(canvas, data):
    displaySlide(canvas, data)

def scaleImage(image, new_width, old_width, new_height, old_height):
    #https://stackoverflow.com/questions/6582387/image-resize-under-photoimage
    scale_w = new_width/old_width
    scale_h = new_height/old_height
    image.zoom(scale_w, scale_h)
    
def loadGalaxyImages(data):
    path = os.getcwd()
    pinwheelPath = 'image_gifs/pinwheel.gif'
    data.pinwheel = PhotoImage(file = pinwheelPath)
    NGC1427APath = 'image_gifs/NGC1427A.gif'
    data.NGC1427A = PhotoImage(file = NGC1427APath)
    ESO325G004Path = 'image_gifs/ESO 325-G004.gif'
    data.ESO325G004 = PhotoImage(file = ESO325G004Path)
    #data.pinwheel = pinwheel.subsample(2, 2)

    
#sets up what is going to show up on each slide
def displaySlide(canvas, data):
    if data.slideNum == 0:
        titleSlide(canvas, data)
    #decide what each slide displays (story board)
    elif data.slideNum == 1:
        galaxyCategoriesSlide(canvas, data)
    elif data.slideNum == 2:
        specialCharacteristicsSlide(canvas, data)
    elif data.slideNum == 3:
        endLearning(canvas, data)
    elif data.slideNum == 4:
        gameDirections(canvas, data)
    elif data.slideNum >= 5 and data.slideNum % 2 != 0:
        gameSlide1(canvas, data)
    elif data.slideNum >=5 and data.slideNum % 2 == 0:
        gameSlide2(canvas,data)
 
#defines what is shown on title slide       
def titleSlide(canvas, data):
    title = "GALAXY SORTING"
    
    #line too long:
    details = "Learn what makes a galaxy unique and become an astronomer too!"
    
    directions = "Press the right to advance through each slide."
    
    
    canvas.create_text(data.width//2, data.height//4, text = title, 
        font = "Arial " + str(data.height//10) + " bold")
    
    canvas.create_text(data.width//2, 5*data.height//8, text = details,
        font = "Arial " + str(data.height//30))
    
    canvas.create_text(data.width//2, 3*data.height//4, text = directions,
        font = "Arial " + str(data.height//30))

#text to be shown on slide teaching about types of galaxies
##insert images
def galaxyCategoriesSlide(canvas, data):
    heading = "THE THREE MAIN CATEGORIES OF GALAXIES"
    
    spiral = "SPIRAL"
    spiralInfo = "Most spiral galaxies are disk-like, with arms that reach out from the center.  \n Spiral galaxies rotate around theire center, in the plane of the disk, \n giving them the characteristic and recognizable shape. \n They are also the most abundant category in the universe"
    
    elliptical = "ELLIPTICAL"
    ellipticalInfo = "Characterized as a 'fuzzy ball' of stars and gas that form a relatively round shape. \n Elliptical galaxies are typically some of the oldest galaxies \n that have been rounded by gravity over time."
    
    irregular = "IRREGULAR"
    irregularInfo = "Irregular galaxies are just that--irregular.  \n They don't quite fit the description of spiral or elliptical galaxies."
    
    
    canvas.create_text(data.width//2, data.margin, text = heading, anchor = "n",
        font = "Arial " + str(data.height//30) + " bold")
    
    #spiral info and image
    canvas.create_text(data.width//5, 1*data.height//5, text = spiral, anchor = 
        "sw", font = "Arial " + str(data.height//50) + " bold")
    
    canvas.create_text(data.width//5, 1*data.height//5, text = spiralInfo,
        anchor = "nw", font = "Arial " + str(data.height//50))
    
    canvas.create_image(data.width//10, 1*data.height//5, image = data.pinwheel)
    
    #elliptical info and image
    canvas.create_text(data.width//5, 2*data.height//5, text = elliptical, 
        anchor = "sw", font = "Arial " + str(data.height//50) + " bold")
    
    canvas.create_text(data.width//5, 2*data.height//5, text = ellipticalInfo, 
        anchor = "nw", font = "Arial " + str(data.height//50))
    canvas.create_image(data.width//10, 2*data.height//5, image = data.ESO325G004)
    
    #irregular info and image
    canvas.create_text(data.width//5, 3*data.height//5, text = irregular, 
        anchor = "sw", font = "Arial " + str(data.height//50) + " bold")
    
    canvas.create_text(data.width//5, 3*data.height//5, text = irregularInfo, 
        anchor = "nw", font = "Arial " + str(data.height//50))
    
    canvas.create_image(data.width//10, 3*data.height//5, image = data.NGC1427A)
#text to be shown about special characteristics galaxies might have
##insert images
def specialCharacteristicsSlide(canvas, data):
    heading = "There are also other characteristics that a galaxy may have:"
    
    bar = "BAR"
    barInfo = "Some spiral galaxies have a bar that goes through the center, \n and the arms sprout out of it."
    
    bulge = "BULGE"
    bulgeInfo = "Spiral galaxies can have a central bulge where the galaxy is \n thicker than toward the edges."
    
    ring = "RING"
    ringInfo = "Some galaxies maight have a ring of matter surrounding them, \n similar to how a planet can have rings."
    
    canvas.create_text(data.width//2, data.margin, text = heading, anchor = "n",
        font = "Arial " + str(data.height//30) + " bold")
    
    canvas.create_text(data.width//5, 1*data.height//5, text = bar, anchor = 
        "sw", font = "Arial " + str(data.height//50) + " bold")
    
    canvas.create_text(data.width//5, 1*data.height//5, text = barInfo,
        anchor = "nw", font = "Arial " + str(data.height//50))
    
    canvas.create_text(data.width//5, 2*data.height//5, text = bulge, 
        anchor = "sw", font = "Arial " + str(data.height//50) + " bold")
    
    canvas.create_text(data.width//5, 2*data.height//5, text = bulgeInfo, 
        anchor = "nw", font = "Arial " + str(data.height//50))
    
    canvas.create_text(data.width//5, 3*data.height//5, text = ring, 
        anchor = "sw", font = "Arial " + str(data.height//50) + " bold")
    
    canvas.create_text(data.width//5, 3*data.height//5, text = ringInfo, 
        anchor = "nw", font = "Arial " + str(data.height//50))

#slide showing end of the learing module
def endLearning(canvas, data):
    text = "Now that you've learned about different types of galaxies \n give categorizing a try!"
    text2 = "All galaxies presented are REAL, with real data!"
    
    canvas.create_text(data.width//2, data.height//3, text = text,
        font = "Arial " + str(data.height//30))
        
    canvas.create_text(data.width//2, 2*data.height//3, text = text2,
        font = "Arial " + str(data.height//30))
        
#slide displaying directions of how to play game, and brief demo
def gameDirections(canvas, data):
    text = "Given a galaxy:"
    step1 = "1. Look at the image"
    step2 = "2. Choose the option that fits the galaxy the best"
    
    canvas.create_text(data.width//2, data.margin, text = text, anchor = "n",
        font = "Arial " + str(data.height//30) + " bold")
    
    canvas.create_text(data.margin, data.height//4, text = step1, anchor = "sw",
        font = "Arial " + str(data.height//30))
    
    canvas.create_text(data.margin, data.height//4, text = step2, anchor = "nw",
        font = "Arial " + str(data.height//30))

def gameSlide1(canvas, data):
    spiralButton = buttons.Buttons("spiral", data.spiralButton[0], data.spiralButton[1])
    irregularButton = buttons.Buttons("irregular", data.irregularButton[0], data.irregularButton[1])
    ellipticalButton = buttons.Buttons("elliptical", data.ellipticalButton[0], data.ellipticalButton[1])
    buttons.Buttons.draw(spiralButton, canvas)
    buttons.Buttons.draw(irregularButton, canvas)
    buttons.Buttons.draw(ellipticalButton, canvas)
    #get which galaxy to use
    #get image and use
    #use question and import buttons
    #draw method for button to put in correct location
def gameSlide2(canvas, data):
    barButton = buttons.Buttons("bar", data.barButton[0], data.barButton[1])
    bulgeButton = buttons.Buttons("bulge", data.bulgeButton[0], data.bulgeButton[1])
    ringButton = buttons.Buttons("ring", data.ringButton[0], data.ringButton[1])
    buttons.Buttons.draw(barButton, canvas)
    buttons.Buttons.draw(bulgeButton, canvas)
    buttons.Buttons.draw(ringButton, canvas)

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='lavender', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000, 1000)

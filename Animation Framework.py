#Animation Starter Code from http://www.cs.cmu.edu/~112/notes/notes-animations-part2.html

from tkinter import *
import buttons
import os
import getGalaxies
from PIL import Image, ImageTk



def init(data):
    data.title = "Galaxy Sorting"
    data.slideNum = 0
    data.margin = data.height//50
    data.spiralButton = (2*data.width/3, 2*data.height /7, "spiral")
    data.irregularButton = (2*data.width/3, 3*data.height /7, "irregular")
    data.ellipticalButton = (2*data.width/3, 4*data.height /7, "elliptical")
    data.bulgeButton = (2*data.width/3, 2*data.height /7, "bulge")
    data.barButton = (2*data.width/3, 3*data.height /7, "bar")
    data.ringButton = (2*data.width/3, 4*data.height /7, "ring")
    data.noneButton = (2*data.width/3, 5*data.height/7, "none")
    data.buttonHeight = 100
    data.buttonWidth = 200
    data.buttons = []
    data.answers = dict()
    data.galaxyNum = -1
    data.galaxy = ""
    data.galaxiesList = getGalaxies.getGalaxy()
    data.loadedImages = []
    data.name = ""
    loadGalaxyImages(data) #loads all necessary images
    

def mousePressed(event, data):
    x = event.x
    y = event.y
    if data.slideNum >= 5:
        for button in data.buttons:
            if (button[0] <= event.x <= button[0] + 
            data.buttonWidth) and (button[1] <= event.y <= 
            button[1] + data.buttonHeight):
                if data.slideNum % 2 != 0:
                    data.answers[data.galaxy] = [button[2]]
                    print(button[2])
                    print(data.answers)
                    data.galaxy = data.galaxiesList[data.galaxyNum]
                else:
                    data.answers[data.galaxy].append(button[2])
                    print(button[2])
                    print(data.answers)
                    data.galaxyNum += 1
                    data.galaxy = data.galaxiesList[data.galaxyNum]
                data.slideNum += 1
  

def keyPressed(event, data):
    if event.keysym == "Right":
        data.slideNum += 1
        if 15 > data.slideNum >=5 and data.slideNum % 2 != 0:
            data.galaxyNum += 1
            data.galaxy = data.galaxiesList[data.galaxyNum]
    elif event.keysym == "Left":
        data.slideNum -= 1
        if 15 > data.slideNum >=5 and data.slideNum % 2 == 0:
            data.galaxyNum -= 1
            data.galaxy = data.galaxiesList[data.galaxyNum]

def timerFired(data):
    pass

def redrawAll(canvas, data):
    displaySlide(canvas, data)
    
def loadGalaxyImages(data):
    #galaxy images from https://www.wikipedia.org/
    path = os.getcwd()
    pinwheelPath = 'image_gifs/pinwheel.gif'
    data.pinwheel = PhotoImage(file = pinwheelPath)
    NGC1427APath = 'image_gifs/NGC1427A.gif'
    data.NGC1427A = PhotoImage(file = NGC1427APath)
    ESO325G004Path = 'image_gifs/ESO 325-G004.gif'
    data.ESO325G004 = PhotoImage(file = ESO325G004Path)
    ringPath = 'image_gifs/ring.gif'
    data.ring = PhotoImage(file = ringPath)
    bulgePath = 'image_gifs/bulge.gif'
    data.bulge = PhotoImage(file = bulgePath)
    barredPath = 'image_gifs/barred.gif'
    data.barred = PhotoImage(file = barredPath)
    
    path = os.getcwd()
    for galaxyName in data.galaxiesList:
        fileName = galaxyName.replace(" ", "_")
        path2 = "/images2/" + fileName + "_2.jpg"
        completePath = path + path2
        #PhotoImage code from https://pythonbasics.org/tkinter-image/
        loadedImage = Image.open(completePath)
        data.loadedImages.append(loadedImage)
    
#sets up what is going to show up on each slide
def displaySlide(canvas, data):
    if data.slideNum == 0:
        titleSlide(canvas, data)
        getUsername(data)
    elif data.slideNum == 1:
        galaxyCategoriesSlide(canvas, data)
    elif data.slideNum == 2:
        specialCharacteristicsSlide(canvas, data)
    elif data.slideNum == 3:
        endLearning(canvas, data)
    elif data.slideNum == 4:
        gameDirections(canvas, data)
    elif 15 > data.slideNum >= 5 and data.slideNum % 2 != 0:
        gameCategory(canvas, data)
    elif 15 > data.slideNum >=5 and data.slideNum % 2 == 0:
        gameCharacteristic(canvas,data)
    elif data.slideNum == 15:
        endGame(canvas, data)

#widget info and code from: http://effbot.org/tkinterbook/entry.htm
def getUsername(data):
    master = Tk()
    
    msg = Label(master, text = "Enter a username")
    msg.pack()
    
    e = Entry(master)
    e.pack()
    
    e.focus_set()
    
    def callback():
        data.name = e.get()
        print(data.name)
    
    b = Button(master, text="Continue", width=10, command=callback, pady=10)
    b.pack()
    
    mainloop()
    e = Entry(master, width=50, padx=10, pady = 10)
    e.pack()
    
#defines what is shown on title slide       
def titleSlide(canvas, data):
    title = "GALAXY SORTING"
    
    details = "Learn what makes a galaxy unique and become an astronomer too!"
    
    directions = "Press the right to advance through each slide."
    
    
    canvas.create_text(data.width//2, data.height//4, text = title, 
        font = "Arial " + str(data.height//10) + " bold")
    
    canvas.create_text(data.width//2, 5*data.height//8, text = details,
        font = "Arial " + str(data.height//30))
    
    canvas.create_text(data.width//2, 3*data.height//4, text = directions,
        font = "Arial " + str(data.height//30))
        
#text to be shown on slide teaching about types of galaxies
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
    
    #barred info and image
    canvas.create_text(data.width//2, data.margin, text = heading, anchor = "n",
        font = "Arial " + str(data.height//30) + " bold")
    
    canvas.create_text(data.width//5, 1*data.height//5, text = bar, anchor = 
        "sw", font = "Arial " + str(data.height//50) + " bold")
    
    canvas.create_text(data.width//5, 1*data.height//5, text = barInfo,
        anchor = "nw", font = "Arial " + str(data.height//50))
    
    canvas.create_image(data.width//10, 1*data.height//5, image = data.barred)
    
    #bulge info and image
    canvas.create_text(data.width//5, 2*data.height//5, text = bulge, 
        anchor = "sw", font = "Arial " + str(data.height//50) + " bold")
    
    canvas.create_text(data.width//5, 2*data.height//5, text = bulgeInfo, 
        anchor = "nw", font = "Arial " + str(data.height//50))
        
    canvas.create_image(data.width//10, 2*data.height//5, image = data.bulge)

    #ring info and image
    canvas.create_text(data.width//5, 3*data.height//5, text = ring, 
        anchor = "sw", font = "Arial " + str(data.height//50) + " bold")
    
    canvas.create_text(data.width//5, 3*data.height//5, text = ringInfo, 
        anchor = "nw", font = "Arial " + str(data.height//50))
    
    canvas.create_image(data.width//10, 3*data.height//5, image = data.ring)

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
    
#gets galaxy name and link and image
def galaxyInfo(canvas,data):
    galaxyNum = (data.slideNum - 5)//2
    galaxyName = data.galaxy
    canvas.create_text(data.width//2, data.margin, text = galaxyName, anchor = "n",
        font = "Arial " + str(data.height//30) + " bold")
    galaxyLink = getGalaxies.getLink(galaxyNum)
    canvas.create_text(data.width//2, data.height//8, text = "For more information, visit https://en.wikipedia.org" + galaxyLink, anchor = "s",
        font = "Arial " + str(data.height//50) + " bold")
    
    #inserting image: https://stackoverflow.com/questions/16539460/insert-a-jpg-in-a-canvas-with-tkinter-and-python-3-2 and http://www.cs.cmu.edu/~112/notes/notes-animations-demos.html
    canvas.image = ImageTk.PhotoImage(data.loadedImages[data.galaxyNum])
    canvas.create_image(data.width//3, data.height//2, image=canvas.image)
    

def gameCategory(canvas, data):
    spiralButton = buttons.Category(data.spiralButton[0], data.spiralButton[1], data.spiralButton[2])
    irregularButton = buttons.Category(data.irregularButton[0], data.irregularButton[1],data.irregularButton[2])
    ellipticalButton = buttons.Category(data.ellipticalButton[0], data.ellipticalButton[1], data.ellipticalButton[2])
    buttons.Category.draw(spiralButton, canvas)
    buttons.Category.draw(irregularButton, canvas)
    buttons.Category.draw(ellipticalButton, canvas)
    data.buttons = [data.spiralButton, data.irregularButton, data.ellipticalButton]
    galaxyInfo(canvas,data)
    

def gameCharacteristic(canvas, data):
    barButton = buttons.Characteristic(data.barButton[0], data.barButton[1], data.barButton[2])
    bulgeButton = buttons.Characteristic(data.bulgeButton[0], data.bulgeButton[1], data.bulgeButton[2])
    ringButton = buttons.Characteristic(data.ringButton[0], data.ringButton[1], data.ringButton[2])
    noneButton = buttons.Characteristic(data.noneButton[0], data.noneButton[1], data.noneButton[2])
    buttons.Characteristic.draw(barButton, canvas)
    buttons.Characteristic.draw(bulgeButton, canvas)
    buttons.Characteristic.draw(ringButton, canvas)
    buttons.Characteristic.draw(noneButton, canvas)
    data.buttons = [data.barButton, data.bulgeButton, data.ringButton, data.noneButton]
    galaxyInfo(canvas,data)
    
def endGame(canvas, data):
    heading = "You've finished this learning activity!"
    results = "This is what you chose for each galaxy:"
    num = 0
    height = data.height//4
    canvas.create_text(data.width//2, data.margin, text = heading, font = "Arial " + str(data.height//30) + " bold")
    canvas.create_text(data.width//2, 3*data.margin, text = results, font = "Arial " + str(data.height//30) + " bold")
    for galaxy in data.answers:
        margin = 30
        canvas.create_text(3*data.margin, height, text = galaxy, font = "Arial " + str(data.height//50) + " bold", anchor = "w")
        canvas.create_text(3*data.margin, height + margin, text = data.answers[galaxy][0], font = "Arial " + str(data.height//50), anchor = "nw")
        canvas.create_text(data.width//2, height + margin, text = data.answers[galaxy][1], font = "Arial " + str(data.height//50), anchor = "nw")
        height += 80
    

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
    #e1 = Entry(root)
    
    canvas.configure(bd=0, highlightthickness=0)
    #e1.pack()
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
    
run(1000,1000)

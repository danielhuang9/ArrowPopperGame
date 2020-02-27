from tkinter import *
from time import *
from random import *

root = Tk()
s = Canvas(root, width = 900, height = 600, background = "white")
s.pack()


#game states
def gameModes():

    global gameRunning, introScreen, endScreen, informationScreen
    
    gameRunning = False
    introScreen = True    
    endScreen = False
    informationScreen = False


#initial values
def setInitialValues():

    global score, level, sectionReduction, letters,death, rectangles, rectColours, xChar, yChar, speed, interval, level
    global graphics, leaders, startTime, gameClock, bestLevel, xMouse, yMouse, introScreen

    startTime = time()
    gameClock = 0
    
    speed = 5
    interval = 20
    score = 100
    level = 1
    highScore = 0
    xMouse = 0
    yMouse = 0

    letters = []
    leaders = [0, 0, 0, 0]
    rectangles = [[],[],[],[]]
    rectColours = [[],[],[],[]]
    xChar = []
    yChar = []
    graphics = []


#drawing section
def drawObjects():

    global section, left, up, down, right, leftArrow, leftTip, upArrow, upTip
    global downArrow, downTip, rightArrow, rightTip

    section = s.create_rectangle(0, 390, 1100, 410, fill = "yellow")
    left = s.create_rectangle(100, 350, 200, 450, fill = "blue")
    up = s.create_rectangle(300, 350, 400, 450, fill = "blue")
    down = s.create_rectangle(500, 350, 600, 450, fill = "blue")
    right = s.create_rectangle(700, 350, 800, 450, fill = "blue")
    leftArrow = s.create_line(190, 400, 140, 400, fill = "orange", width = 15)
    leftTip = s.create_polygon(140, 440, 110, 400, 140, 360, fill = "orange")
    upArrow = s.create_line(350, 440, 350, 390, fill = "orange", width = 15)
    upTip = s.create_polygon(310, 390, 350, 360, 390, 390, fill = "orange")
    downArrow = s.create_line(550, 360, 550, 410, fill = "orange", width = 15)
    downTip = s.create_polygon(510, 410, 550, 440, 590, 410, fill = "orange")
    rightArrow = s.create_line(710, 400, 760, 400, fill = "orange", width = 15)
    rightTip = s.create_polygon(760, 360, 790, 400, 760, 440, fill = "orange")


#drawing title screen
def titleScreen():

    global introScreen, infoScreen, endScreen

    introScreen = True
    informationScreen = False
    endScreen = False

    s.delete("all")
    s.create_rectangle(280, 230, 620, 350, fill = "white", outline = "green2", width = 10)
    s.create_text(450, 290, text = "Play", font = ("Courier", 40), fill = "green2")
    s.create_rectangle(250, 380, 650, 450, fill = "white", outline = "red", width = 5)
    s.create_text(450, 415, text = "Instructions", font = ("Courier", 30), fill = "red")
    s.create_text(450, 100, text = "Arrow Popper", font = ("Fixedsys", 120))
    s.create_text(87, 588, text = "Press <ESC> to leave :(", font = ("Arial", 12))
    
    s.create_line(0, 137, 910, 137, width = 5) 
    

#drawing instructions screen
def infoScreen():

    global informationScreen, introScreen

    s.delete("all")

    informationScreen = True
    introScreen = False

    s.create_text(450, 70, text = "How To Play", font = ("Arial", 30))
    s.create_text(450, 120, text = "When a square enters a “section”, you will click the corresponding arrow key.", font = ("Arial", 12))
    s.create_text(450, 160, text = "You will be rewarded points and lose points if you miss.", font = ("Arial", 12))
    s.create_text(450, 200, text = "The game will end after 60 seconds or if your score goes below 0.", font =("Arial", 12))
    s.create_text(450, 240, text = "You will be rewarded more points if you click the arrow key when the square is more towards the middle of the section.", font = ("Arial", 12))
    s.create_text(450, 280, text = "The squares speed up everytime your score increases by 500.", font = ("Arial", 12))
    s.create_text(450, 350, text = "Points system", font = ("Arial", 30))
    s.create_text(450, 400, text = "If square is < 10 pixels from center, you receive 100 points,", font = ("Arial", 15), fill = "green")
    s.create_text(450, 440, text = "If square is > 10 and < 20 pixels from center, you receive 50 points,", font = ("Arial", 15), fill = "DarkOliveGreen")
    s.create_text(450, 480, text = "If square is > 20 and < 40 pixels from center, you receive 40 points,", font = ("Arial", 15), fill = "olive drab")
    s.create_text(450, 520, text = "If square is > 40 and < 60 pixels from center, you receive 20 points,", font = ("Arial", 15), fill = "Dark sea green")
    s.create_text(450, 560, text = "If you miss or let the square fall all the way down, you will lose 90.", font = ("Arial", 15), fill = "red")
    s.create_polygon(125, 20, 50, 20, 5, 50, 50, 80, 125, 80, fill = "black")
    s.create_text(80, 50, text = "Back", font = ("Arial", 20), fill = "white")


#function for mouse 1 clicks
def mouseDown(event):
 
    global gameRunning, introScreen, endScreen, informationScreen

    xMouse = event.x
    yMouse = event.y

    if introScreen == True:

        if 280 < xMouse < 620 and 230 < yMouse < 350:
            gameRunning = True
            introScreen = False
            runGame()

        elif 250 < xMouse < 650 and 380 < yMouse < 450:
            gameRunning = False
            introScreen = False
            infoScreen()

    elif informationScreen == True:

        if 125 > xMouse > 5 and 80 > yMouse > 20:

            informationScreen = False
            introScreen = True
            titleScreen()

    elif endScreen == True:
        
        if 600 > xMouse > 300 and 450 > yMouse > 350:
            
            endScreen = False
            introScreen = True
            gameRunning = True
            titleScreen()
            
    
#creates random square
def createRectangle():

    xPos = randint(0, 3)
    yPos = 0
    rectangles[xPos].append(yPos)
    rectColours[xPos].append("grey")


#game timer
def getTime():

    global gameClock, startTime

    elapsedTime = time() - startTime

    if elapsedTime >= 1.0:
        gameClock = gameClock + 1
        startTime = time()


#increase level and speed
def incLevel():

    global level, speed
    
    if score > level*500:
        level += 1
        speed = 2 * level

    elif score < (level-1)*500:
        level -= 1
        speed = 2 * level


#user's input
def userInput(event):

    char = event.keysym
    #pairing columns with keys pressed
    c = -1
    if char == "Left":
        c = 0
    elif char == "Up":
        c = 1
    elif char == "Down":
        c = 2
    elif char == "Right":
        c = 3
    #if user doesn't click anything and making sure leader is in rectangle[c] 
    if not c == -1 and leaders[c] < len(rectangles[c]):
        #getting distance from square to the target
        distance = abs(360-rectangles[c][leaders[c]])
        getScore(distance, c)
        leaders[c] += 1


#animate falling squares
def updateRectangle():

    global speed, interval, leaders, score

    for i, column in enumerate(rectangles):
        d = 0

        for j, rect in enumerate(column[:]):
            #moving the note in its column
            column[j-d] += speed
            r = s.create_rectangle(110+i*200, rect, 190+i*200, rect+80, fill = rectColours[i][j-d])
            graphics.append(r)
            if rect > 600:
                #deleting the rectangle when it goes below the screen
                if leaders[i] <= j-d:
                    score -= 90     #update score
                leaders[i] = max(0, leaders[i]-1)   #reset the leader
                #removing squares from columns
                del rectColours[i][j-d]     
                del column[j-d]
                d += 1  #update index after deleting


#increase/decrease score
def getScore(distance, c):
    
    global score, rectColours

    if distance < 10:
        #print("perfect hit")
        rectColours[c][leaders[c]] = "green"
        score += 100
    elif distance < 20:
        #print("awesome")
        rectColours[c][leaders[c]] = "DarkOliveGreen"
        score += 50
    elif distance < 40:
        #print("great")
        rectColours[c][leaders[c]] = "olive drab"
        score += 20
    elif distance < 60:
        #print("good")
        rectColours[c][leaders[c]] = "Dark sea green"
        score += 10
    else:
        #print("miss")
        rectColours[c][leaders[c]] = "red"
        score -= 90


#run game
def runGame():

    global frames, score, level, gameRunning

    setInitialValues()

    frames = 0

    #keeps game running
    while gameClock < 60 and score > 0 and gameRunning == True:
      
        s.delete("all")
        drawObjects()
        getTime()
        incLevel()
        frames = frames + 1

        r = s.create_text(50, 50, text = "Time: " + str(gameClock), font = ("Courier", 12))
        graphics.append(r)
        
        r = s.create_text(52, 100, text = "Score: " + str(score), font = ("Courier", 11))
        graphics.append(r)

        r = s.create_text(50, 150, text = "Level: " + str(level), font = ("Courier", 12))
        graphics.append(r)

        updateRectangle()

        if frames%interval == 0:
            createRectangle()

        s.update()
        sleep(0.03)

        for g in graphics:
            s.delete(g)
        del graphics[:]

    endGame()


#drawing end game screen
def endGame():

    global gameRunning, introScreen, endScreen, bestLevel


    gameRunning = False
    introScreen = False
    endScreen = True
    
    s.delete("all")
    s.create_text(450, 225, text = "Nice! You got to level " + str(level) + "!", font = ("Courier", 35))
    s.create_rectangle(300, 350, 600, 450, fill = "white", outline = "black")
    s.create_text(450, 400, text = "Play Again?", font = ("Courier", 30))
    s.create_text(87, 588, text = "Press <ESC> to leave :(", font = ("Arial", 12))
    

#quit game
def quitGame(event):
    
    root.destroy()

    
s.focus_set()
s.bind("<Key>", userInput)
s.bind("<Button-1>", mouseDown)
s.bind ("<Escape>", quitGame)

gameModes()
titleScreen()

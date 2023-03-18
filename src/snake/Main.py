from tkinter import Label, Canvas, ALL, Tk                                                                                          #
import random                                                                                                                       #
                                                                                                                                    #
BOARD_WIDTH = 750                                                                                                                   #
BOARD_HEIGHT = 750                                                                                                                  #
SQUARE_SIZE = 25                                                                                                                    #
AXIS_SIZE = (BOARD_WIDTH * BOARD_HEIGHT) / (SQUARE_SIZE * SQUARE_SIZE)                                                              #
SPEED = 300                                                                                                                         #
                                                                                                                                    #
axisX = [0] * int(AXIS_SIZE)                                                                                                        #
axisY = [0] * int(AXIS_SIZE)                                                                                                        #
foodScore = 0                                                                                                                       #
isRunning = True                                                                                                                    #
                                                                                                                                    #
SNAKE_COLOR = "#00FF00"                                                                                                             #
SNAKE_HEAD_COLOR = "#Ff0000"                                                                                                        #
FOOD_COLOR = "#FFFF00"                                                                                                              #
BACKGROUND_COLOR = "#000000"                                                                                                        #
                                                                                                                                    #
class Snake:                                                                                                                        #
                                                                                                                                    #
    def __init__(self):                                                                                                             #
        self.bodyPieces = 4                                                                                                         #
                                                                                                                                    #
    def drawSnake(self, x, y, index):                                                                                               #
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # Method               :    drawSnake()
        #
        # Method parameters    :    x, y, index
        #
        # Method return        :    void
        #
        # Synopsis             :    This method draws the snake on the screen.                            
        #                           If the index is 0 it draws the head in red color. Otherwise draws in green.
        # Modifications        :
        #                           Date            Developer                Notes
        #                           ----            ---------                -----
        #                           2022-11-21        Tiago                   none.
        #
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        if index == 0:                                                                                                              #
            canvas.create_rectangle(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE, fill=SNAKE_HEAD_COLOR, tag="snake")                     #
        else:                                                                                                                       #
            canvas.create_rectangle(x, y, x + SQUARE_SIZE, y + SQUARE_SIZE, fill=SNAKE_COLOR, tag="snake")                          #
                                                                                                                                    #
                                                                                                                                    #
class Food:                                                                                                                         #
                                                                                                                                    #
    def __init__(self):                                                                                                             #
        self.axisX = []                                                                                                             #
        self.axisY = []                                                                                                             #
                                                                                                                                    #
    def drawnFood(self):                                                                                                            
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        # Method               :    drawFood()
        #
        # Method parameters    :    none
        #
        # Method return        :    void
        #
        # Synopsis             :    This method draws the food on the screen.                            
        #                           
        # Modifications        :
        #                           Date            Developer                Notes
        #                           ----            ---------                -----
        #                           2022-11-21        Tiago                   none.
        #
        # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        canvas.create_oval(self.axisX, self.axisY, self.axisX + SQUARE_SIZE, self.axisY + SQUARE_SIZE, fill=FOOD_COLOR, tag="food") #
                                                                                                                                    #
                                                                                                                                    #
def startGame():                                                                                                                    #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Method               :    startGame()
    #
    # Method parameters    :    none
    #
    # Method return        :    void
    #
    # Synopsis             :    This method starts the game.                            
    #                           
    # Modifications        :
    #                           Date            Developer                Notes
    #                           ----            ---------                -----
    #                           2022-11-21        Tiago                   none.
    #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    if isRunning:                                                                                                                   #
        move()                                                                                                                      #
        if checkCollisions():                                                                                                       #
            if checkFood():                                                                                                         #
                food.drawnFood()                                                                                                    #
            else:                                                                                                                   #
                canvas.delete("snake")                                                                                              #
            window.after(SPEED, startGame)                                                                                          #
            drawGame()                                                                                                              #
        else:                                                                                                                       #
            saveFile()                                                                                                              #
            gameOver()                                                                                                              #
                                                                                                                                    #
                                                                                                                                    #
                                                                                                                                    #
def drawGame():                                                                                                                     #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Method               :    drawGame()
    #
    # Method parameters    :    none
    #
    # Method return        :    void
    #
    # Synopsis             :    This method draws the game itself (snake, food).                            
    #                           
    # Modifications        :
    #                           Date            Developer                Notes
    #                           ----            ---------                -----
    #                           2022-11-21        Tiago                   none.
    #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    if isRunning:                                                                                                                   #
        checkFood()                                                                                                                 #Draws the food.
        for index in range(0, snake.bodyPieces):                                                                                    #Loops to draw each part of the snake.
            snake.drawSnake(axisX[index], axisY[index], index)                                                                      #
    else:                                                                                                                           #
        gameOver()                                                                                                                  #
                                                                                                                                    #
                                                                                                                                    #
def foodRespawn():                                                                                                                  #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Method               :    foodRespawn()
    #
    # Method parameters    :    none
    #
    # Method return        :    void
    #
    # Synopsis             :    This method generates the random position for the food appears.                            
    #                           
    # Modifications        :
    #                           Date            Developer                Notes
    #                           ----            ---------                -----
    #                           2022-11-21        Tiago                   none.
    #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    food.axisX = random.randint(0, (BOARD_WIDTH / SQUARE_SIZE) - 1) * SQUARE_SIZE                                                   #
    food.axisY = random.randint(0, (BOARD_HEIGHT / SQUARE_SIZE) - 1) * SQUARE_SIZE                                                  #
                                                                                                                                    #
                                                                                                                                    #
def move():                                                                                                                         #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Method               :    move()
    #
    # Method parameters    :    none
    #
    # Method return        :    void
    #
    # Synopsis             :    This method updates the snake position.                            
    #                           
    # Modifications        :
    #                           Date            Developer                Notes
    #                           ----            ---------                -----
    #                           2022-11-21        Tiago                   none.
    #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    for index in range(snake.bodyPieces, 0, -1):                                                                                    #Keeps updating the snake.
        axisX[index] = axisX[index - 1]                                                                                             #
        axisY[index] = axisY[index - 1]                                                                                             #
                                                                                                                                    #
    if direction == "up":                                                                                                           #
        axisY[0] -= SQUARE_SIZE                                                                                                     #Updates Y coordinate.
    elif direction == "down":                                                                                                       #
        axisY[0] += SQUARE_SIZE                                                                                                     #Updates Y coordinate.
    elif direction == "left":                                                                                                       #
        axisX[0] -= SQUARE_SIZE                                                                                                     #Updates X coordinate.
    elif direction == "right":                                                                                                      #
        axisX[0] += SQUARE_SIZE                                                                                                     #Updates X coordinate.
                                                                                                                                    #
                                                                                                                                    #
def checkFood():                                                                                                                    #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Method               :    checkFood()
    #
    # Method parameters    :    none
    #
    # Method return        :    void
    #
    # Synopsis             :    This method checks collision between the snake's head and the food positions, add points and sets the respawn.                            
    #                           
    # Modifications        :
    #                           Date            Developer                Notes
    #                           ----            ---------                -----
    #                           2022-11-21        Tiago                   none.
    #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    global foodScore                                                                                                                #
    if axisX[0] == food.axisX and axisY[0] == food.axisY:                                                                           #Checks the collision.
        snake.bodyPieces += 1                                                                                                       #Draws another piece of the snake.
        canvas.delete("food")                                                                                                       #Deletes the food.
        foodRespawn()                                                                                                               #Repawns the food.
        foodScore += 1                                                                                                              #Add points.
        label.config(text="Score: {}".format(foodScore))                                                                            #Updates the score in the screen.
        return True                                                                                                                 #
    else:                                                                                                                           #
        return False                                                                                                                #
                                                                                                                                    #
                                                                                                                                    #
def changeDirection(new_direction):                                                                                                 #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Method               :    changeDirection()
    #
    # Method parameters    :    new_direction
    #
    # Method return        :    void
    #
    # Synopsis             :    This method stores temporarily the direction.                            
    #                           
    # Modifications        :
    #                           Date            Developer                Notes
    #                           ----            ---------                -----
    #                           2022-11-21        Tiago                   none.
    #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    global direction                                                                                                                #
                                                                                                                                    #
    if new_direction == 'left':                                                                                                     #
        if direction != 'right':                                                                                                    #
            direction = new_direction                                                                                               #
    elif new_direction == 'right':                                                                                                  #
        if direction != 'left':                                                                                                     #
            direction = new_direction                                                                                               #
    elif new_direction == 'up':                                                                                                     #
        if direction != 'down':                                                                                                     #
            direction = new_direction                                                                                               #
    elif new_direction == 'down':                                                                                                   #
        if direction != 'up':                                                                                                       #
            direction = new_direction                                                                                               #
                                                                                                                                    #
                                                                                                                                    #
def checkCollisions():                                                                                                              #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Method               :    checkCollisions()
    #
    # Method parameters    :    none
    #
    # Method return        :    void
    #
    # Synopsis             :    This method checks collision between the snake's and the board, also between the snake's head and body.                            
    #                           
    # Modifications        :
    #                           Date            Developer                Notes
    #                           ----            ---------                -----
    #                           2022-11-21        Tiago                   none.
    #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    isRunning = True                                                                                                                #
    for index in range(snake.bodyPieces, 0, -1):                                                                                    #Checks if the head is going to collide with the body.
        if axisX[0] == axisX[index] and axisY[0] == axisY[index]:                                                                   #
            isRunning = False                                                                                                       #
                                                                                                                                    #
    if axisX[0] < 0:                                                                                                                #Checks the collision on the edges.
        isRunning = False                                                                                                           #
    elif axisX[0] > BOARD_WIDTH:                                                                                                    #
        isRunning = False                                                                                                           #
    elif axisY[0] < 0:                                                                                                              #
        isRunning = False                                                                                                           #
    elif axisY[0] > BOARD_HEIGHT:                                                                                                   #
        isRunning = False                                                                                                           #
                                                                                                                                    #
    return isRunning                                                                                                                #
                                                                                                                                    #
                                                                                                                                    #
def gameOver():                                                                                                                     #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Method               :    gameOver()
    #
    # Method parameters    :    none
    #
    # Method return        :    void
    #
    # Synopsis             :    This method show the Game Over screen and saves the score into a file.                            
    #                           
    # Modifications        :
    #                           Date            Developer                Notes
    #                           ----            ---------                -----
    #                           2022-11-21        Tiago                   none.
    #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    canvas.delete(ALL)                                                                                                              #
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,                                                             #
                       font=('Arial',70), text="GAME OVER", fill="white", tag="gameover")                                           #
                                                                                                                                    #
                                                                                                                                    #
                                                                                                                                    #
def saveFile():                                                                                                                     #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Method               :    saveFile()
    #
    # Method parameters    :    none
    #
    # Method return        :    void
    #
    # Synopsis             :    This method saves the score into a file.                            
    #                           
    # Modifications        :
    #                           Date            Developer                Notes
    #                           ----            ---------                -----
    #                           2022-11-21        Tiago                   none.
    #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    global foodScore                                                                                                                #
    file = open('snakeLastScore_Python.txt', 'w')                                                                                   #Creates a file object.
    try:
        file.write(str(foodScore))                                                                                                      #Writes a line of text.    
        file.close()                                                                                                                    #
    except Exception:
        print("ERROR: Can't save the file.")                                                                                                                            #
                                                                                                                                    #
def loadFile():                                                                                                                     #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    # Method               :    loadFile()
    #
    # Method parameters    :    none
    #
    # Method return        :    void
    #
    # Synopsis             :    This method load the score into the game.                            
    #                           
    # Modifications        :
    #                           Date            Developer                Notes
    #                           ----            ---------                -----
    #                           2022-11-21        Tiago                   none.
    #
    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    global foodScore                                                                                                                #
    file = open("snakeLastScore_Python.txt")                                                                                        #Creates a file object.
    try:
        foodScore = int(file.read())                                                                                                #Reads a line of text.
        file.close()                                                                                                                #
        label.config(text="Score: {}".format(foodScore))                                                                            #Updates the score in the screen.
    except Exception:
        print("ERROR: Can't load the file.")                                                                                        #

window = Tk()                                                                                                                       #Instantiates the tkinter class.
window.title("Snake game")                                                                                                          #
window.resizable(False, False)                                                                                                      #
                                                                                                                                    #
isRunning = True                                                                                                                    #
foodScore = 0                                                                                                                       #
direction = 'down'                                                                                                                  #
                                                                                                                                    #
label = Label(window, text="Score: {}".format(foodScore), font=('Arial', 24))                                                       #
label.pack()                                                                                                                        #
                                                                                                                                    #
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=BOARD_HEIGHT, width=BOARD_WIDTH)                                                #
canvas.pack()                                                                                                                       #
                                                                                                                                    #
window.update()                                                                                                                     #
                                                                                                                                    #
window_width = window.winfo_width()                                                                                                 #
window_height = window.winfo_height()                                                                                               #
screen_width = window.winfo_screenwidth()                                                                                           #
screen_height = window.winfo_screenheight()                                                                                         #
                                                                                                                                    #
x = int((screen_width/2) - (window_width/2))                                                                                        #
y = int((screen_height/2) - (window_height/2))                                                                                      #
                                                                                                                                    #
window.geometry(f"{window_width}x{window_height}+{x}+{y}")                                                                          #Defines the screen's dimensions.
                                                                                                                                    #
window.bind('<Left>', lambda event: changeDirection('left'))                                                                        #Sets the directions.
window.bind('<Right>', lambda event: changeDirection('right'))                                                                      #
window.bind('<Up>', lambda event: changeDirection('up'))                                                                            #
window.bind('<Down>', lambda event: changeDirection('down'))                                                                        #
                                                                                                                                    #
snake = Snake()                                                                                                                     #Instantiates Snake class.
food = Food()                                                                                                                       #Instantiates Food class.
loadFile()                                                                                                                          #
foodRespawn()                                                                                                                       #
food.drawnFood()                                                                                                                    #
startGame()                                                                                                                         #
                                                                                                                                    #
window.mainloop()                                                                                                                   #
import random, os

path = os.getcwd()

ROW_NUM = 20
COL_NUM = 10 
BLOCK_SIZE = 20
HEIGHT = 400
WIDTH = 200
COLORS = [[255,51,52], [12,150,228], [30,183,66], [246,187,0], [76,0,153], [255,255,255], [0,0,0]]
boardArray = []
    
class Block:
    def __init__(self):
        self.size = BLOCK_SIZE
        self.color_index = random.randint(0,6)
        self.color = COLORS[self.color_index] 
        self.y = - BLOCK_SIZE
        self.x = random.randrange(0,200,20)

    def display(self):
        self.gravity()
        fill(self.color[0], self.color[1], self.color[2])
        rect(self.x, self.y, self.size, self.size) 
    
    # blocks move down unless blocks are placed in the column
    def gravity(self):
        if (BLOCK_SIZE + self.y < HEIGHT) and (game.game_grid[self.y//BLOCK_SIZE][self.x//BLOCK_SIZE] == 0): 
            self.y += BLOCK_SIZE

class Game():
    def __init__(self):
        self.speed = 0
        self.score = 0
        self.scored = False
        self.blocks = []
        self.key_press = {LEFT: False, RIGHT: False}
        self.blocks.append(Block())
        self.current_position = 0
        self.current_block = self.blocks[self.current_position]
        self.game_over = False
        self.string_score = "Score: " + str(self.score) 
        self.game_grid = []
        self.create_game_grid()
        self.check_game_over()
                  
    def draw_grid(self):
        for row in range(0, WIDTH, BLOCK_SIZE):
            fill(180)
            line(row, 0, row, height)
        for col in range(0, HEIGHT, BLOCK_SIZE):
            fill(180)
            line(0, col, width, col)
        self.check_score()
            
    # creating a list to store empty spaces
    def create_game_grid(self): 
        for i in range (ROW_NUM):
            rlist = []
            for r in range (COL_NUM):
                rlist.append(0)
            self.game_grid.append(rlist) 
        
    # game over when the ceilings of every column are full
    def check_game_over(self):
        cnt = 0
        for i in range(COL_NUM):
            if self.game_grid[0][i] != 0:
                cnt += 1
        if cnt == (COL_NUM):
            self.game_over = True 
     
    # print game over
    def play(self):
        self.check_game_over()
        if self.game_over == True:
            background(255)
            textSize(30)
            textAlign(CENTER, CENTER)
            text("GAME OVER!", WIDTH/3, HEIGHT/2)
            text("SCORE: " + str(self.score), (WIDTH/3)+32, (HEIGHT/2)+70)
            return 
        
        # if block is placed at the bottom... 
        if (BLOCK_SIZE + self.current_block.y >= HEIGHT) or (self.game_grid[self.current_block.y//BLOCK_SIZE][self.current_block.x//BLOCK_SIZE] != 0) and self.game_over == False:
            self.game_grid[(self.current_block.y//BLOCK_SIZE) - 1][(self.current_block.x//BLOCK_SIZE)] = self.current_block
            
            self.blocks.append(Block())
            self.current_position += 1
        
            # if we make a match of four 
            if self.new_point() == True: 
                self.speed = 0
                self.current_position -= 4 
            else:
                self.speed += 0.25
            self.current_block = self.blocks[self.current_position]
             
            
    # print scores
    def check_score(self):
        textSize(15)
        fill(0)
        textAlign(LEFT, TOP)
        self.string_score = "Score: " + str(self.score)
        text(self.string_score, BLOCK_SIZE * COL_NUM - 80, 0)
        noFill()   
    
    def new_point(self):
        # check if we have four same colored blocks stacked 
        for r in range(len(self.game_grid)-1, -1 ,-1):
            for c in range(len(self.game_grid[r])):
                if (self.game_grid[r][c] != 0) and (self.game_grid[r-1][c] != 0) and (self.game_grid[r-2][c] != 0) and (self.game_grid[r-3][c] != 0):
                    if self.game_grid[r][c].color == self.game_grid[r - 1][c].color == self.game_grid[r - 2][c].color == self.game_grid[r - 3][c].color:
                        for k in range(4):
                           self.blocks.remove(self.game_grid[r - k][c]) 
                           self.game_grid[r - k][c] = 0
                        self.score += 1
                        return True
                    
    def move_down(self):
        if len(self) == 1:
            if self.current_block.x == BLOCK_SIZE * (NUM_ROW - 1):
                self.current_block.placed = True
    
    def display(self):
        self.draw_grid()
        self.play()
        self.motion()
        # self.game_over == False
        for block in self.blocks:
            block.display()
        self.check_score()
        self.new_point()
    
    # keys and moves accordingly
    def motion(self):
        if game.key_press[RIGHT] == True:
            if ((game.current_block.x + BLOCK_SIZE < WIDTH) and (game.current_block.y + BLOCK_SIZE <= HEIGHT)) and game.game_grid[(game.current_block.y//BLOCK_SIZE)-1][((game.current_block.x)//BLOCK_SIZE)+1] == 0 and self.game_over == False:
                game.current_block.x += BLOCK_SIZE 
            
        elif game.key_press[LEFT] == True:
            if ((0<=(game.current_block.x - BLOCK_SIZE) < WIDTH) and (game.current_block.y + BLOCK_SIZE <= HEIGHT)) and game.game_grid[((game.current_block.y)//BLOCK_SIZE)-1][((game.current_block.x)//BLOCK_SIZE)-1] == 0 and self.game_over == False:
                game.current_block.x -= BLOCK_SIZE 
            
game = Game()  

def setup():
    background(210)
    size(WIDTH, HEIGHT)

def draw():
    if frameCount%(max(1, int(8 - game.speed))) == 0 or frameCount == 1:
        if game.game_over:
            background(255)
            textSize(20)
            textAlign(CENTER, CENTER)
            text("GAME OVER!", WIDTH//2, HEIGHT//2)
            text("SCORE: " + str(game.score), (WIDTH/3)+32, (HEIGHT/2)+70)
        else:
            background(210)
            stroke(180)
            game.display()

# move the blocks 
def keyPressed():
    if keyCode == LEFT:
        game.key_press[LEFT] = True
    elif keyCode == RIGHT:
        game.key_press[RIGHT] = True 
    

def keyReleased():
    if keyCode == LEFT:
        game.key_press[LEFT] = False
    elif keyCode == RIGHT:
        game.key_press[RIGHT] = False 
    
    
# mouse pressed function
def mouseClicked():
    global game
    if game.game_over:
        game = Game() 

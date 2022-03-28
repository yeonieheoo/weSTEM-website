WIDTH = 900
HEIGHT = 900
BLOCK_SIZE = 300
COL = 3
ROW = 3
global game
import random, os
import time

path = os.getcwd()

# create moles
class Moles():
    def __init__(self):
        self.img = loadImage(path + "/pic.png")
        self.r = 100
        self.up = 0
        self.x = (BLOCK_SIZE/2) + random.randrange(0,WIDTH,BLOCK_SIZE)
        self.y = (250)+(random.randrange(0,HEIGHT,BLOCK_SIZE))
        self.vy = 0
        
        
        
# vertical movements of moles within the block ranges
    def fly(self):
        if ( 0 <= self.y - (0.5*self.r)<=300 ) and 0 <= self.y + (0.5*self.r)<=300:
            self.y = self.y + self.vy
        elif 300 < self.y - (0.5*self.r)<= 600 and 300 < self.y + (0.5*self.r)<= 600:
            self.y = self.y + self.vy
        elif 600 < self.y - (0.5*self.r)<= 900 and 600 < self.y + (0.5*self.r)<= 900:
            self.y = self.y + self.vy
        else:
            self.up += 1
            self.vy = 0
            if self.up > 2:
                self.up = 3
            #self.vy = self.vy + 10
            #self.y = self.y + self.vy
        
#change movement (up or down)
    def update(self):
        if self.up ==0:
            self.vy = self.vy - 0.10
        elif self.up == 1:
            self.y += 10
            self.vy += 0.20
        self.fly()   
    
    def display(self):
        self.update() 
        print(self.y, self.vy)
        image(self.img, (self.x-(self.r/2)), (self.y-self.r), self.r*1.5, self.r*1.5)
    
             

class Game():
    def __init__(self):
        self.game_grid = []
        self.mole_store = []
        self.position = 0
        self.mole1 = Moles()
        self.mole2 = Moles()
        self.mole_store.append(self.mole1)
        self.mole_store.append(self.mole2)
        
        self.alive = True
        self.speed = 0.5
        self.score = 0 
        self.start = time.time()
        self.end_time = 0
        self.lives = 3
        self.click = hit.play()
        self.hit = hit
        self.music = bgm
        self.music.loop()
        self.key_press = {RIGHT: False}

# create grid for storage               
    def make_grid(self):
        for r in range (ROW):
            rlist = []
            for c in range (COL):
                rlist.append(0)
            self.game_grid.append(rlist)
                
# create game grid
    def draw_game_grid(self):
        for j in range(0, WIDTH, BLOCK_SIZE):
            fill(0,0,0)
            line(j, 0, j, height)
        for k in range(0, HEIGHT, BLOCK_SIZE):
            fill(0,0,0)
            line(0, k, width, k)
        
    def mallet(self):
        self.mal = loadImage(path + "/mallet.png")
        image(self.mal, mouseX-50, mouseY,150, 150)            


# points earned when mole hit. Life lost if misclick
    def clicked(self):
        if (self.mole1.x-100 <=mouseX <= self.mole1.x+100) and (self.mole1.y-100<= mouseY <= self.mole1.y+100):
            self.score += 1
            self.mole_store.pop(self.mole_store.index(self.mole1)) 
            self.mole1 = Moles()
            self.mole_store.append(self.mole1)
            self.hit.play()
  
        elif (self.mole2.x-100 <=mouseX <= self.mole2.x+100) and (self.mole2.y-100<= mouseY <= self.mole2.y+100):
            self.score += 1
            self.mole_store.pop(self.mole_store.index(self.mole2)) 
            self.mole2 = Moles()
            self.mole_store.append(self.mole2)
            self.hit.play()
            
        else:
            self.lives = self.lives - 1
            if self.lives == 0:
                self.alive = False 
                
    def backg(self):
        fill(30,183,66)
        rect(0, 0, 900, 900)    
        
        fill(0)
        ellipse((150),250, 200, 100 )
        ellipse((150),550, 200, 100 )
        ellipse((150),850, 200, 100 )
        ellipse((450),250, 200, 100 )
        ellipse((450),550, 200, 100 )
        ellipse((450),850, 200, 100 )
        ellipse((750),850, 200, 100 )  
        ellipse((750),250, 200, 100 )
        ellipse((750),550, 200, 100 )
        
              
    def display(self):
        self.make_grid()
        self.draw_game_grid()
        self.backg()
        
        if self.alive ==True :
        
            self.draw_game_grid()  


# Create new moles        
            if self.mole1.up >1:
                self.mole_store.pop(self.mole_store.index(self.mole1)) 
                self.mole1 = Moles()
                self.mole_store.append(self.mole1)
            
            if self.mole2.up >1:
                self.mole_store.pop(self.mole_store.index(self.mole2)) 
                self.mole2 = Moles()
                self.mole_store.append(self.mole2)
                
            for i in self.mole_store:
                i.display()
            self.end_time = time.time()
            
            if int(self.end_time - self.start) == 90:
                self.alive = False
            
            print("the num of secs" , self.end_time - self.start)
                
            textSize(30)
            fill(0)
            textAlign(LEFT, TOP)
            text('SCORE:'+str(self.score), BLOCK_SIZE * COL - 200, 0)
            noFill() 
            
            textSize(30)
            fill(0)
            textAlign(LEFT, TOP)
            timer = 90 - int(self.end_time - self.start)
            text('Timer:'+str(timer), BLOCK_SIZE * COL - 800, 0)
            noFill()
            
            textSize(30)
            fill(0)
            textAlign(LEFT, TOP)
            text('Lives:'+str(self.lives), BLOCK_SIZE * COL - 500, 0)
            noFill()
            
# Game over screen    
        else:
            background(225)
            textAlign(CENTER)
            textSize(30)
            text('Game Over', COL * BLOCK_SIZE / 2, ROW * BLOCK_SIZE / 2-BLOCK_SIZE)
        
            text('SCORE:' + str(self.score), WIDTH/2, HEIGHT/3)
            noFill()
            
            textSize(25)
            textAlign(CENTER, CENTER)
            text("Press 'RIGHT' to Restart", WIDTH/2, HEIGHT/2)
                  

game = Game()
     
def setup():
    size(WIDTH, HEIGHT)
    background(210)
    
def draw():
    game.display()
    game.mallet()

def mouseClicked():
    game.clicked()

def keyPressed():
    if keyCode == RIGHT:
        game.key_press[RIGHT] = False
        
        if game.alive == False:
            game = Game()
  

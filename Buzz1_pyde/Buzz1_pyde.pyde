# Inspiration: 
# https://thecodingtrain.com/CodingChallenges/131-bouncing-dvd-logo.html

x = 0
y = 0
xspeed = 9
yspeed = 3
#PImage(buzz)

def setup():
    background(0)
    size(500,450)
    frameRate(27)
    # noLoop()
    
def draw(): # primary animation loop of 60 frames per second
    global x, y, xspeed, yspeed, words #, buzz
    current = frameCount
    background(0)
    buzz = loadImage("TheBuzz.png")
        
    x += xspeed
    if x > width - 253 or x < 0:
        #fill(random(255), random(255), random(255))
        tint(random(255), random(255), random(255))
        xspeed *= -1
        
    y += yspeed
    if y > height - 78 or y < 0:
        #fill(random(255), random(255), random(255))
        tint(random(255), random(255), random(255))
        yspeed *= -1 
        
    image(buzz, x, y, 253, 78) #169, 52
    #fill(random(255), random(255), random(255))
    #fill(0xFFFFC30B) #random(255), random(255), random(255))
    #textSize(50)
    #text("The Buzz", x, y)
    
    

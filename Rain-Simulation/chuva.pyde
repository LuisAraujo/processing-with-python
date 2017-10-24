listaChuvas = []
chuvatime = 0

class Chuva():
    def __init__(self):
        self.x= random(0,300)
        self.y= 0
    
    def move(self):
        self.y+=1
    
    def drawchuva(self):
        stroke(255,255,255,255 - self.y)
        line(self.x,self.y,self.x,self.y+10)
        
        
        
def setup():
    size(300,300)
    background(0)
    listaChuvas.append(Chuva())
        

def draw():
    global chuvatime
    chuvatime+=1
    if(chuvatime%10 == 0):
        listaChuvas.append(Chuva())
        
    background(0)
    for c in listaChuvas:
        c.move()
        c.drawchuva()
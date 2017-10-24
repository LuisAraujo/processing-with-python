def setup():
    global img
    size(300,300)
    img = loadImage("stevejobs.jpg");
    
    
def draw():
    global img
    background(0)
    tint(100)
    image(img, 0, 0);
def setup():
    size(304,304)
    background(0)
    strokeWeight(2)
    stroke(255)
    global jogo, jogador
    jogador = "o"
    jogo = [["","",""],
            ["","",""],
            ["","",""]]
    
def draw():
    global jogo, jogador
    background(0)
    line(100,4,100,300)
    line(202,4,202,300)
    line(4,100,300,100)
    line(4,202,300,202)
    fill(255,255,255,100)
    posx = (mouseX/100);
    posy = (mouseY/100)
    rect(posx  * 100, posy * 100, 100,100)
    
    if(mousePressed):
        if(jogo[posx][posy] == ""):
           jogo[posx][posy]=jogador
           if(jogador == "o"):
              jogador = "x"
           else:
              jogador = "o"
           
   
    for i in range(0,3):
        for j in range(0,3):
            if(jogo[i][j]=="o"):
                noFill()
                ellipse(i*100 + 50,j*100 + 50,90,90) 
            elif(jogo[i][j] == "x"):
                line(i*100,j*100,i*100+100,j*100+100)
                line(i*100,j*100+100,i*100+100,j*100)
    
    
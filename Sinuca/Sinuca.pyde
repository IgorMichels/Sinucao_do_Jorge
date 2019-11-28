from Bola import Bola, gera_bolas
from Bordas import Bordas
from Mesa import Mesa
from Taco import Taco

def setup():
    size(800, 600)

bolas = gera_bolas()
mesa = Mesa()
taco = Taco()
inc = PVector(0, 0)
ver = False

bordas = Bordas.bordas
for i in bordas:
    i[0] = PVector(i[0][0], i[0][1])
    i[1] = PVector(i[1][0], i[1][1])

oldt = millis()
def draw():
    global oldt, ver, bolas
    
    t = millis()
    dt = t-oldt
    oldt = t
        
    background(0)
    
    for i in range(len(bolas)):
        for j in bordas:
            bolas[i].verifica_colisao_parede(j)
        for j in range(len(bolas)):
            if i < j:
                if bolas[i].v != PVector(0, 0) or bolas[j].v != PVector(0, 0):
                    bolas[i].verifica_colisao(bolas[j])
    
    for i in bolas:
        i.move(dt)
    if mousePressed and ver:
        stroke(0)
        taco.desenha(mouseX, mouseY, bolas[0].pos.x, bolas[0].pos.y)
        
    mesa.desenha()
    a = 5*2**(1/2)
    pops = []
    for i in range(len(bolas)):
        if bolas[i].pos[0] < 102 or bolas[i].pos[0] > 698 or bolas[i].pos[1] < 273 or bolas[i].pos[1] > 567:
            if i == 0:
                bolas[i] = Bola(PVector(180, 420), 8.5, 1, (255, 255, 255))
            else:
                pops.append(i)
        elif bolas[i].pos[0] > 680 - a and bolas[i].pos[1] < 290 + a:
            if i == 0:
                bolas[i] = Bola(PVector(180, 420), 8.5, 1, (255, 255, 255))
            else:
                pops.append(i)
        elif bolas[i].pos[0] > 680 - a and bolas[i].pos[1] > 550 - a:
            if i == 0:
                bolas[i] = Bola(PVector(180, 420), 8.5, 1, (255, 255, 255))
            else:
                pops.append(i)
        elif bolas[i].pos[0] < 120 + a and bolas[i].pos[1] < 290 + a:
            if i == 0:
                bolas[i] = Bola(PVector(180, 420), 8.5, 1, (255, 255, 255))
            else:
                pops.append(i)
        elif bolas[i].pos[0] < 120 + a and bolas[i].pos[1] > 550 - a:
            if i == 0:
                bolas[i] = Bola(PVector(180, 420), 8.5, 1, (255, 255, 255))
            else:
                pops.append(i)
        elif bolas[i].pos[0] > 400 - a and bolas[i].pos[0] < 400 + a and bolas[i].pos[1] < 287 + a:
            if i == 0:
                bolas[i] = Bola(PVector(180, 420), 8.5, 1, (255, 255, 255))
            else:
                pops.append(i)
        elif bolas[i].pos[0] > 400 - a and bolas[i].pos[0] < 400 + a and bolas[i].pos[1] > 553 - a:
            if i == 0:
                bolas[i] = Bola(PVector(180, 420), 8.5, 1, (255, 255, 255))
            else:
                pops.append(i)
        bolas[i].desenha()
    for i in pops:
        bolas.pop(i)
    
    textSize(72)
    textAlign(CENTER)
    fill(255,228,181)
    string = 'SINUCAO DO JORGE'
    for i in range(len(string)):
        if i == 3:
            if frameCount % 200 > 5:
                fill(255,228,181, 50)
                text(string[i],50 + 48*i,100)
            else:
                fill(255,228,181)
                text(string[i],50 + 48*i,100)
        elif i == 5:
            if frameCount % 400 > 300:
                fill(255,228,181, 50)
                text(string[i],50 + 48*i,100)
            else:
                fill(255,228,181)
                text(string[i],50 + 48*i,100)
        elif i == 12:
            if frameCount % 150 > 130:
                fill(255,228,181, 50)
                text(string[i],50 + 48*i,100)
            else:
                fill(255,228,181)
                text(string[i],50 + 48*i,100)
        elif i == 13:
            if frameCount % 40 > 35:
                fill(255,228,181, 50)
                text(string[i],50 + 48*i,100)
            else:
                fill(255,228,181)
                text(string[i],50 + 48*i,100)
        elif i == 15:
            translate(50 + 48*i,110)
            rotate(2*PI - 0.3)
            text(string[i],0,0)
            resetMatrix()
        else:
            fill(255,228,181)
            text(string[i],50 + 48*i,100)
    textSize(16)
    textAlign(LEFT)
    text("by: Igor Patricio Michels e Isaque Vieira Machado Pim", 380, 590)
    
    textSize(24)
    textAlign(CENTER)
    text('Restart', 630, 220)
    if mouseX <= 630 + 70 and mouseX >= 630 - 70 and mouseY <= 220 + 30 and mouseY >= 220 - 30:
        noFill()
        rectMode(CENTER)
        stroke(255,228,181)
        rect(630, 220, 140, 60)
        rectMode(CORNER)

def mouseClicked():
    global bolas
    if mouseX <= 630 + 70 and mouseX >= 630 - 70 and mouseY <= 220 + 30 and mouseY >= 220 - 30:
        bolas = gera_bolas()

def mouseDragged():
    global inc, ver
    
    if (mouseX - bolas[0].pos.x)**2 + (mouseY-bolas[0].pos.y)**2 <= (bolas[0].r+10)**2:
        ver = True

    if ver:
        inc.x = bolas[0].pos.x - mouseX
        inc.y = bolas[0].pos.y - mouseY
        stroke(0)
        taco.desenha(mouseX, mouseY, bolas[0].pos.x, bolas[0].pos.y)

def mouseReleased():
    global inc, ver

    if ver:
        taco.desenha(mouseX, mouseY, bolas[0].pos.x, bolas[0].pos.y, release = True)
        bolas[0].v.add(inc/400)
        inc = PVector(0,0) 
        ver = False

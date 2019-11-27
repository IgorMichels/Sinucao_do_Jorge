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
    global oldt, ver
    
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

    pops = []
    for i in range(len(bolas)):
        if bolas[i].pos[0] < 122 or bolas[i].pos[0] > 678 or bolas[i].pos[1] < 293 or bolas[i].pos[1] > 547:
            if i == 0:
                bolas[i] = Bola(PVector(180, 420), 8.5, 1, (255, 255, 255))
            else:
                pops.append(i)
        bolas[i].desenha()
        
    for i in pops:
        bolas.pop(i)
    

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

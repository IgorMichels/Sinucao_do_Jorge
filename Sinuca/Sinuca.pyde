from Bola import Bola, gera_bolas
from Bordas import Bordas
from Mesa import Mesa


def setup():
    size(800, 600)


bolas = gera_bolas()
mesa = Mesa()

inc = PVector(0, 0)
ver = False

bordas = Bordas.bordas
for i in bordas:
    i[0] = PVector(i[0][0], i[0][1])
    i[1] = PVector(i[1][0], i[1][1])


oldt = millis()
def draw():
    global oldt
    
    t = millis()
    dt = t-oldt
    oldt = t
    
    
    background(0)
    
    for i in range(len(bolas)):
        if bolas[i].status() == "on":
            for j in bordas:
                bolas[i].verifica_colisao_parede(j)
            for j in range(len(bolas)):
                if i < j and bolas[j].status() == "on":
                    bolas[i].verifica_colisao(bolas[j])
    
    for i in bolas:
        i.move(dt)
  
    mesa.desenha()

    pops = []
    for i in range(len(bolas)):
        if bolas[i].status() == "off":
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
        stroke(255,0,0)
        line(bolas[0].pos.x,bolas[0].pos.y,mouseX,mouseY)

def mouseReleased():
    global inc, ver

    if ver:
        bolas[0].v.add(inc/400)
        inc = PVector(0,0) 
        ver = False

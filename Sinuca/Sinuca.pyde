import Bola
import Bordas
import Mesa

def setup():
    size(800, 600)
    
    

bolas = [
         Bola(PVector(180, 420), 8.5, 1, (255, 255, 255)),
         Bola(PVector(600,386), 8.5, 1, (255,0,0)),      
         Bola(PVector(600,403), 8.5, 1, (255,0,0)),
         Bola(PVector(600,420), 8.5, 1, (255,0,0)),
         Bola(PVector(600,437), 8.5, 1, (255,0,0)),
         Bola(PVector(600,454), 8.5, 1, (255,0,0)),
         Bola(PVector(600-17*2**(0.5),394.5), 8.5, 1, (255,0,0)),
         Bola(PVector(600-17*2**(0.5),411.5), 8.5, 1, (255,0,0)),
         Bola(PVector(600-17*2**(0.5),428.5), 8.5, 1, (255,0,0)),
         Bola(PVector(600-17*2**(0.5),445.5), 8.5, 1, (255,0,0)),
         Bola(PVector(600-34*2**(0.5),437), 8.5, 1, (255,0,0)),
         Bola(PVector(600-34*2**(0.5),420), 8.5, 1, (255,0,0)),
         Bola(PVector(600-34*2**(0.5),403), 8.5, 1, (255,0,0)),
         Bola(PVector(600-51*2**(0.5),428.5), 8.5, 1, (255,0,0)),
         Bola(PVector(600-51*2**(0.5),411.5), 8.5, 1, (255,0,0)),
         Bola(PVector(600-68*2**(0.5),420), 8.5, 1, (255,0,0))
         ]
mesa = Mesa()

inc = PVector(0, 0)
ver = False

bordas = Bordas.bordas
for i in bordas:
    i[0] = PVector(i[0][0], i[0][1])
    i[1] = PVector(i[1][0], i[1][1])


oldt = millis()
a = 100
wb = False
def draw():
    global oldt, a, wb
    
    t = millis()
    dt = t-oldt
    oldt = t
    
    
    background(0)
    
    for i in range(len(bolas)):
#        if bolas[i].v != PVector(0,0):
        for j in bordas:
            bolas[i].verifica_colisao_parede(j)
        for j in range(len(bolas)):
            if i < j:
                bolas[i].verifica_colisao(bolas[j])
    
    for i in bolas:
        i.move(dt)
  
    mesa.desenha()

    if a == 100:
        wb = True
    
    a = len(bolas)
    for i in range(a):
        if bolas[i].pos[0] < 130 or bolas[i].pos[0] > 670 or bolas[i].pos[1] < 297 or bolas[i].pos[1] > 543:
            if i == 0:
                bolas[i] = Bola(PVector(180, 420), 8.5, 1, (255, 255, 255))
                if wb == True:
                    bolas[i].desenha()
                    wb = False
                    a = 0
                else:
                    a += 1
                    print(a)
            else:
                bolas.pop(i)
                a = len(bolas)
        else:
            bolas[i].desenha()
    

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

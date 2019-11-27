from Bola import Bola
from Mesa import Mesa
from Bordas import Bordas

def setup():
    size(800, 600)
    
    
b = Bola(PVector(160, 450), 7, 1, (255, 255, 255))    
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
    
    for i in bordas:
        b.verifica_colisao_parede(i)
    b.move(dt)
  
    mesa.desenha()
    b.desenha()


def mouseDragged():
    global inc, ver
    
    if sqrt((mouseX - b.pos.x)**2 + (mouseY-b.pos.y)**2) <= b.r+10:
        ver = True

    if ver:
        inc.x = b.pos.x - mouseX
        inc.y = b.pos.y - mouseY
        stroke(255,0,0)
        line(b.pos.x,b.pos.y,mouseX,mouseY)

def mouseReleased():
    global inc, ver

    if ver:
        b.v.add(inc/400)
        inc = PVector(0,0) 
        ver = False

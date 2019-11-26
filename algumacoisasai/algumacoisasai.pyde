class Bola:
    def __init__(self,pos, raio, massa, cor):
        self.pos = pos
        self.r = raio
        self.m = massa
        self.v = PVector(0, 0)
        self.a = PVector(0, 0)
        self.cor = cor
    def move(self, dt):
       
        self.v = self.v + self.a * dt
        self.pos = self.pos + self.v * dt    
       
    def desenha(self):
       
        fill(self.cor[0], self.cor[1], self.cor[2])
        ellipse(self.pos.x, self.pos.y, self.r, self.r)
   
def colide(a, b):

    dir_x = b.pos - a.pos
    dir_x.normalize()
   
    va_x = dir_x * (a.v.dot(dir_x))
    va_y = a.v - va_x
   
    vb_x = dir_x * (b.v.dot(dir_x))
    vb_y = b.v - vb_x

   
    new_ax = va_x.mag() * ((a.m - b.m)/(a.m + b.m)) - vb_x.mag() * ((2*b.m)/(a.m + b.m))
    new_bx = va_x.mag() * ((2*a.m)/(a.m + b.m)) - vb_x.mag() * ((b.m - a.m)/(a.m + b.m))
   

    a.v = new_ax * dir_x + va_y
    b.v = new_bx * dir_x + vb_y
    
    corr =  (a.r + b.r)/2 - dist(a.pos.x, a.pos.y, b.pos.x, b.pos.y)
    a.pos -= dir_x * corr
    b.pos += dir_x * corr 
    
   
def detecta_colisao(a, b):
    stroke(255,255,0)
    line(a.pos.x,a.pos.y,b.pos.x,b.pos.y)
    
    if (a.pos.x - b.pos.x)**2 + (a.pos.y - b.pos.y)**2 < ((a.r + b.r)/2)**2:
        colide(a, b)

def paredao(a):
   
    if a.pos.x <= a.r/2 or a.pos.x >= 800 - a.r/2:
        a.v.x = -a.v.x
        a.pos.x += a.v.x
       
    if a.pos.y <= a.r/2 or a.pos.y >= 600 - a.r/2:
        a.v.y = -a.v.y
        a.pos.y += a.v.y


def setup():
    size(800, 600)



bolas = []

for i in range(6):
    bolas.append(Bola(PVector(random(50, 750),random(50, 550)), 50, 1, (255, random(0, 255), random(0, 255))))
    bolas[i].v += PVector(random(10)/70,random(10)/70)
    



oldt = millis()

def draw():
    global branca, oldt, bolas
    t = millis()
    dt = t - oldt
    oldt = t
   
    background(0)
   
    for i in bolas:    
        i.move(dt)

    
    for i in range(len(bolas)):
        paredao(bolas[i])
        for j in range(i+1, len(bolas)):
            detecta_colisao(bolas[i], bolas[j])
    
    for i in bolas:
        i.desenha()

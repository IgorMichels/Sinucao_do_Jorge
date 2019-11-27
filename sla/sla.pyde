class Bola:
    def __init__(self, pos, raio, massa, cor):
        self.pos = pos
        self.r = raio
        self.m = massa
        self.v = PVector(0, 0)
        self.a = PVector(0, 0)
        self.cor = cor
        self.para = False

    def move(self, dt):
        if self.v.mag() < 0.004:
            self.a = PVector(0, 0)
            self.v = PVector(0, 0)
        else:
            v = self.v.copy()
            self.a = PVector(v[0], v[1])
            self.v = self.v - 0.0004 * self.a * dt        

        self.pos = self.pos + self.v * dt    
                
    def desenha(self):
        stroke(0)
        fill(self.cor[0], self.cor[1], self.cor[2])
        ellipse(self.pos.x, self.pos.y, 2*self.r, 2*self.r)
        
    def verifica_colisao(self, a):        
        if (self.pos.x - a.pos.x)**2 + (self.pos.y - a.pos.y)**2 < (self.r + a.r)**2:
            self.colide(a)
    
    def verifica_colisao_parede(self, p):

        pa = p[0] - p[1]
        v1 = pa.dot(self.pos - p[1])
        v2 = pa.dot(self.pos - p[0])
        
        if v1 > 0 and v2 < 0:
            a_ = (self.pos-p[1]) - (v1/(v1-v2))*pa
            if a_.x**2 + a_.y**2 <= self.r**2:
                self.colide_parede(a_)
        
    def colide(self, a):
        
        dir_x = a.pos - self.pos
        dir_x.normalize()
    
        va_x = dir_x * (self.v.dot(dir_x))
        va_y = self.v - va_x
    
        vb_x = dir_x * (a.v.dot(dir_x))
        vb_y = a.v - vb_x
    
        if va_x.dot(vb_x) > 0.0:
            if va_x.dot(dir_x) < 0:
                new_ax = - va_x.mag() * ((self.m - a.m)/(self.m + a.m)) - vb_x.mag() * ((2*a.m)/(self.m + a.m))
                new_bx = - va_x.mag() * ((2*self.m)/(self.m + a.m)) - vb_x.mag() * ((a.m - self.m)/(self.m + a.m))
                self.pos += 2 * self.v
                a.pos += 2 * a.v  

            else:
                new_ax =  va_x.mag() * ((self.m - a.m)/(self.m + a.m)) + vb_x.mag() * ((2*a.m)/(self.m + a.m))
                new_bx =  va_x.mag() * ((2*self.m)/(self.m + a.m)) + vb_x.mag() * ((a.m - self.m)/(self.m + a.m))
                self.pos += 2 * self.v
                a.pos += 2 * a.v  
        else:
            new_ax =  va_x.mag() * ((self.m - a.m)/(self.m + a.m)) - vb_x.mag() * ((2*a.m)/(self.m + a.m))
            new_bx =  va_x.mag() * ((2*self.m)/(self.m + a.m)) - vb_x.mag() * ((a.m - self.m)/(self.m + a.m))
            self.pos += 2 * self.v
            a.pos += 2 * a.v  

            
    
        self.v = new_ax * dir_x + va_y
        a.v = new_bx * dir_x + vb_y

        #self.pos += 2 * self.v
        #a.pos += 2 * a.v  
        
    def colide_parede(self, n):
        n.normalize()
        vy = n*(self.v.dot(n))
        vx = self.v - vy
    
        
        vy = vy* (-1)
        self.pos.add(2*vy)
        self.v = vx + vy
        
        
class Bordas:
    bordas = [[[130, 287],[142, 296]],
              [[142, 296],[386, 296]],
              [[386, 296],[390, 287]],
              [[670, 287],[658, 296]],
              [[414, 296],[658, 296]],
              [[130, 553],[142, 544]],
              [[142, 544],[386, 544]],
              [[386, 544],[390, 553]],
              [[670, 553],[658, 544]],
              [[414, 544],[658, 544]],
              [[414, 544],[410, 553]],
              [[117, 300],[126, 312]],
              [[126, 312],[126, 528]],
              [[126, 528],[117, 540]],
              [[683, 300],[674, 312]],
              [[674, 312],[674, 528]],
              [[674, 528],[683, 540]]]
    
    
class Mesa:
    def __init__(self):
        pass
        
    def desenha(self):
        # borda de madeira
        stroke(0)
        fill(89, 47, 37)
        rect(100, 270, 600, 300)
        
        # quinas/ partes ao redor dos buracos
        fill(77, 63, 52)
        rect(100, 270, 40, 40)
        rect(700, 270, -40, 40)
        rect(100, 570, 40, -40)
        rect(700, 570, -40, -40)
        rect(390, 270, 20, 20)
        rect(390, 570, 20, -20)
        
        # tecido verde
        fill(18, 166, 97)
        rect(117, 287, 566, 266)
        
        # buraco
        fill(112, 86, 69)
        ellipse(400, 287, 20, 20)
        ellipse(400, 553, 20, 20)
        ellipse(120, 290, 20, 20)
        ellipse(120, 550, 20, 20)
        ellipse(680, 290, 20, 20)
        ellipse(680, 550, 20, 20)
        
        # estopa verde
        fill(2, 115, 62)
        triangle(130, 287, 142, 287, 142, 296)
        rect(142, 287, 244, 9)
        triangle(386, 287, 386, 295, 390, 287)
    
        triangle(670, 287, 658, 287, 658, 296)
        rect(414, 287, 244, 9)
        triangle(414, 287, 414, 295, 410, 287)
    
        triangle(130, 553, 142, 553, 142, 544)
        rect(142, 544, 244, 9)
        triangle(386, 553, 386, 545, 390, 553)
    
        triangle(670, 553, 658, 553, 658, 544)
        rect(414, 544, 244, 9)
        triangle(414, 553, 414, 545, 410, 553)
    
        triangle(117, 300, 117, 312, 126, 312)
        rect(117, 312, 9, 216)
        triangle(117, 528, 117, 540, 126, 528)
    
        triangle(683, 300, 683, 312, 674, 312)
        rect(674, 312, 9, 216)
        triangle(683, 528, 683, 540, 674, 528)
        
        stroke(2, 115, 62)
        line(142, 288, 142, 295)
        line(386, 288, 386, 294)
        line(658, 288, 658, 295)
        line(414, 288, 414, 294)
        line(142, 552, 142, 545)
        line(386, 552, 386, 546)
        line(658, 552, 658, 545)
        line(414, 552, 414, 546)
        line(118, 312, 125, 312)
        line(118, 528, 125, 528)
        line(682, 312, 675, 312)
        line(682, 528, 675, 528)

def setup():
    size(800, 600)
    
    

bolas = [
         Bola(PVector(180, 420), 8.5, 1, (255, 255, 255)),
         #Bola(PVector(600,403), 8.5, 1, (255,255,255)),
         #Bola(PVector(600,420), 8.5, 1, (255,255,255)),
         #Bola(PVector(600,437), 8.5, 1, (255,255,255)),
         #Bola(PVector(600,454), 8.5, 1, (255,255,255)),
         #Bola(PVector(600-17*2**(0.5),394.5), 8.5, 1, (255,255,255)),
         #Bola(PVector(600-17*2**(0.5),411.5), 8.5, 1, (255,255,255)),
         #Bola(PVector(600-17*2**(0.5),428.5), 8.5, 1, (255,255,255)),
         #Bola(PVector(600-17*2**(0.5),445.5), 8.5, 1, (255,255,255)),
         #Bola(PVector(600-34*2**(0.5),437), 8.5, 1, (255,255,255)),
         #Bola(PVector(600-34*2**(0.5),420), 8.5, 1, (255,255,255)),
         #Bola(PVector(600-34*2**(0.5),403), 8.5, 1, (255,255,255)),
         #Bola(PVector(600-51*2**(0.5),428.5), 8.5, 1, (255,255,255)),
         #Bola(PVector(600-51*2**(0.5),411.5), 8.5, 1, (255,255,255)),
         #Bola(PVector(600-68*2**(0.5),420), 8.5, 1, (255,255,255)),
         Bola(PVector(600,386), 8.5, 1, (255,255,255))      
         ]    
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
        if bolas[i].v != PVector(0,0):
            for j in bordas:
                bolas[i].verifica_colisao_parede(j)
            for j in bolas:
                if bolas[i] != j:
                    bolas[i].verifica_colisao(j)
        
    for i in bolas:
        i.move(dt)
  
    mesa.desenha()
    for i in bolas:
        i.desenha()
    

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

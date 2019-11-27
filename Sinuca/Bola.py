class Bola:

    def __init__(self, pos, raio, massa, cor):
        self.pos = pos
        self.r = raio
        self.m = massa
        self.v = PVector(0, 0)
        self.a = PVector(0, 0)
        self.cor = cor

    def status(self):
        if self.pos[0] < 130 or self.pos[0] > 670 or self.pos[1] < 297 or self.pos[1] > 543:
            return "off"
        else:
            return "on"

    def move(self, dt):
        if self.status() == "on":
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

def gera_bolas():
        bolas = [Bola(PVector(180, 420), 8.5, 1, (255, 255, 255)),
         Bola(PVector(600,384), 8.5, 1, (255,0,0)),      
         Bola(PVector(600,402), 8.5, 1, (255,0,0)),
         Bola(PVector(600,420), 8.5, 1, (255,0,0)),
         Bola(PVector(600,438), 8.5, 1, (255,0,0)),
         Bola(PVector(600,456), 8.5, 1, (255,0,0)),
         Bola(PVector(599-8.5*3**(0.5),392.5), 8.5, 1, (255,0,0)),
         Bola(PVector(599-8.5*3**(0.5),410.5), 8.5, 1, (255,0,0)),
         Bola(PVector(599-8.5*3**(0.5),429.5), 8.5, 1, (255,0,0)),
         Bola(PVector(599-8.5*3**(0.5),447.5), 8.5, 1, (255,0,0)),
         Bola(PVector(598-17*3**(0.5),402), 8.5, 1, (255,0,0)),
         Bola(PVector(598-17*3**(0.5),420), 8.5, 1, (255,0,0)),
         Bola(PVector(598-17*3**(0.5),438), 8.5, 1, (255,0,0)),
         Bola(PVector(597-25.5*3**(0.5),429.5), 8.5, 1, (255,0,0)),
         Bola(PVector(597-25.5*3**(0.5),410.5), 8.5, 1, (255,0,0)),
         Bola(PVector(596-34*3**(0.5),420), 8.5, 1, (255,0,0))
         ]
        return bolas

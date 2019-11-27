class Buraco:
    def __init__(self, posx, posy, dx, dy):
        self.posx = posx
        self.posy = posy
        self.dx = dx
        self.dy = dy
        self.cor = (112, 86, 69)

    def desenha(self):
        fill(cor[0], cor[1], cor[2])
        ellipse(posx, posy, dx, dy)

def gera_buraco():
    buracos  = [Buraco(400, 287, 20, 20),
                Buraco(400, 553, 20, 20),
                Buraco(120, 290, 20, 20),
                Buraco(120, 550, 20, 20),
                Buraco(680, 290, 20, 20),
                Buraco(680, 550, 20, 20)
                ]
    return buracos

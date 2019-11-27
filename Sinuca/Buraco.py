class Buraco:
    def __init__(self, pos.x, pos.y, d.x, d.y):
        self.pos.x = pos.x
        self.pos.y = pos.y
        self.d.x = d.x
        self.d.y = d.y
        self.cor = (112, 86, 69)

    def desenha(self):
        fill(cor[0], cor[1], cor[2])
        ellipse(pos.x, pos.y, d.x, d.y)

def gera_buraco():
    buracos  = [Buraco(400, 287, 20, 20),
                Buraco(400, 553, 20, 20),
                Buraco(120, 290, 20, 20),
                Buraco(120, 550, 20, 20),
                Buraco(680, 290, 20, 20),
                Buraco(680, 550, 20, 20)
                ]
    return buracos

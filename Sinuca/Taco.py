class Taco:
    def __init__(self):
        pass
    def desenha(self, x, y, px, py, release = False):
        if release:
            dir = PVector(x,y) - PVector(px,py)
            translate(px, py)
            if y > py:
                rotate(PVector.angleBetween(PVector(1,0), dir) + PI)
            else:
                rotate(3*PI - PVector.angleBetween(PVector(1,0), dir))
            fill(0)
            rect(-8.5 - 6, -3, 6, 6)
            fill(168, 116, 50)
            rect(-8.5 - 6- 200, -3, 200, 6)
            resetMatrix()
        else:
            
            dir = PVector(x,y) - PVector(px,py)
            translate(px, py)
            if y > py:
                rotate(PVector.angleBetween(PVector(1,0), dir) + PI)
            else:
                rotate(3*PI - PVector.angleBetween(PVector(1,0), dir))
            fill(0)
            rect(-8.5 - 6-20-dir.mag(), -3, 6, 6)
            fill(168, 116, 50)
            rect(-8.5 - 6- 200-20-dir.mag(), -3, 200, 6)
            resetMatrix()

from Bola import Bola
from Mesa import Mesa


def setup():
    size(800, 600)
    
    
b1 = Bola(PVector(160, 450), 10, 1, (255, 255, 255))    
mesa = Mesa()

def draw():
    
    
    
    background(0)
    
  
    mesa.desenha()
    b1.desenha()
    
    

def Mesa():
    # borda de madeira
    fill(89, 47, 37)
    rect(100, 270, 600, 300)
    
    # quinas/partes ao redor dos buracos
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
#    ellipse(128.5, 298.5, 23*2**(1/2), 23*2**(1/2)) # teste maluco aqui
    
    # estopa verde
    fill(2, 115, 62)
    triangle(130, 287, 138, 287, 138, 295)
    rect(138, 287, 248, 9)
    triangle(386, 287, 386, 295, 390, 287)

    triangle(670, 287, 662, 287, 662, 295)
    rect(414, 287, 248, 9)
    triangle(414, 287, 414, 295, 410, 287)

    triangle(130, 553, 138, 553, 138, 545)
    rect(138, 544, 248, 9)
    triangle(386, 553, 386, 545, 390, 553)

    triangle(670, 553, 662, 553, 662, 545)
    rect(414, 544, 248, 9)
    triangle(414, 553, 414, 545, 410, 553)

    triangle(117, 300, 117, 308, 126, 308)
    rect(117, 308, 9, 235)
    triangle(414, 553, 414, 545, 410, 553)
    
    stroke(2, 115, 62)
    line(138, 288, 138, 294)
    line(386, 288, 386, 294)
    line(662, 288, 662, 294)
    line(414, 288, 414, 294)
    line(138, 552, 138, 546)
    line(386, 552, 386, 546)
    line(662, 552, 662, 546)
    line(414, 552, 414, 546)
    line(118, 308, 125, 308)
        
    stroke(0)
    # uma bola branca aleatória qualquer
    fill(255, 255, 255)
    ellipse(350, 420, 17, 17)
    
def setup():
    size(800, 600)

def draw():
    Mesa()

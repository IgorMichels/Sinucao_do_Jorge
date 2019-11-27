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
        # ellipse(128.5, 298.5, 23*2**(1/2), 23*2**(1/2)) # teste maluco aqui
        
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

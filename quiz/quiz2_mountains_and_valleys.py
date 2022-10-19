import turtle

def mountains_and_valleys(m, v, slope):
    t = turtle.Turtle() #N1
    i = 0 #A1
    while i <= m + v: #F1
        if i < m: #G2
        
            t.left(slope) #K3
            t.forward(50) #K3
            
            t.right(2*slope) #L3
            t.forward(50) #L3
            
            t.left(slope) #E3
        elif i > m: #H2
            
            t.right(slope) #J3
            t.forward(50) #J3
            
            t.left(2*slope) #M3
            t.forward(50) #M3
            
            t.right(slope) #C3
        else: #I2
            
            t.forward(50) #D3
            
        i+= 1 #B2
        
            
mountains_and_valleys(2,3,80)
#N1 A1 F1 G2 K3 L3 E3 H2 J3 M3 C3 I2 D3 B2
def input_IP():
    
    octets = [] #G1
    for i in range(4): #D1
        octet = -1 #A2
        while octet < 0 or octet > 255: #F2
            octet = int(input("Enter octet:")) #I3
            
        octets.append(str(octet)) #E2
         
    octets_s = (octets[0] + '.' + octets[1] + '.' +
                octets[2] + '.' + octets[3]) #C1
    
    return octet_s #H1

    
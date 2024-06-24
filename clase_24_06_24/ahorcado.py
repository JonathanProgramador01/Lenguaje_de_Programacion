import Data
import random

palabra = random.choice(Data.WORDS)
print("PSSS esta es la palabra: ",palabra)
Molde = [ "_" for _ in palabra ]


Vidas = 8
while Vidas > 1:
    print(Molde)
    letra = input("Ingresa letra: ")
    if letra in palabra:
        if letra not in Molde:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    Molde[i] = letra
        else:
            Vidas -= 1
            print(Data.IMAGES[8-Vidas])
            
    else:           
            
        Vidas -= 1
        print(Data.IMAGES[8-Vidas])
        
    
    
    
        
    if "_" not in Molde:
        print(Molde)
        print("GANASSTTEEEE FEICIDADESS")
        break
   
   
     
if Vidas == 1:
    print("LOO SIENTOO PERDISTEE")        
        

        
        

    
    
    
    
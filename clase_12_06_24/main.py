def operacion (dato):
    gybyte = 1024
    microdisco = 1.44
    a = dato * gybyte
    a /= microdisco
    return f"Tienes {a} microdiscos"

    
    



print("##############################Calculadora de Microdiscoss########################################")
microdiscos = float(input("\n\nIingrese el numero de Gybytes de tu disco duro:  "))
#SUPONIENDO QUE MI DISCO DURO ES DE 100 GYBYTES
print(operacion(microdiscos))











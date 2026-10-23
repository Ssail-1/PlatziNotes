
# Es la idea de como funciona property 
def decorador(funcion):
    
    def nueva_funcion():
        
        print("Antes")
        
        funcion()
        
        print("Despues")
    
    return nueva_funcion
    
def saludar():
    print("Hola")
    
saludar_1 = decorador(saludar)

saludar_1()

#print(nueva_funcion())
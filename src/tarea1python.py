# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="Juank"
__date__ ="$18-ago-2014 23:03:16$"

def funcion():
    """Main Program"""
    respuesta = 0
    for a in range(1, 101): #ciclos for para ir de 1 a 100 en valor de a
        for b in range(1, 101): #ciclos for para ir de 1 a 100 en valor de b
            numero = a ** b  #asigna el valor al numero
            L = list(str(numero)) #pasamos el numero a string y lo agregamos a la lista
            suma = 0
            for i in L:
                suma = suma + int(i)
            if suma > respuesta:
                respuesta = suma
    print "Suma maxima  = ", respuesta
    
if __name__ == "__main__":
    print "Hello World"
    funcion()
  
  

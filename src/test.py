def funcion():
    """Main Program"""
    respuesta = 0
    k = {'97','98','99','100'}
    for a in range(90,101): #ciclos for para ir de 1 a 100 en valor de a
        for b in  range(90,101): #ciclos for para ir de 1 a 100 en valor de b
            numero = int(a) ** int(b)  #asigna el valor al numero
            L = list(str(numero)) #pasamos el numero a string y lo agregamos a la lista
            suma = 0
            for i in L:
                suma = suma + int(i)
            if suma > respuesta:
                respuesta = suma
    print ("Suma maxima  = " + str(respuesta))
    
if __name__ == "__main__":
    print ("Hello World")
    funcion()
  
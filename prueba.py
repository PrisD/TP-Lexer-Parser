def afd_id(cadena):
    estadoActual= 'A'
    estadoFinal = 'Z'
    for caracter in cadena:
            if estadoActual == 'A' and caracter.isalpha():
                  estadoActual = 'Z'
            elif estadoActual == 'A':
                  estadoActual = 'X'
            elif estadoActual == 'X':
                  break
    if estadoFinal == estadoActual :
        print('es el token id')
    else: print('no es el token id')

''' afd_id("aaaaaa")
afd_id("123")
afd_id("a213123") '''

def afd_si(cadena): 
    estadoActual= 'A'
    estadoFinal = 'Z'
    for caracter in cadena:
        if estadoActual == 'A' and caracter == 's':
                estadoActual ='B'
        elif estadoActual =='A' and caracter != 's':
                estadoActual ='X'

        elif estadoActual =='B' and caracter == 'i':
                estadoActual ='Z'
        elif estadoActual =='B' and caracter != 'i':
                estadoActual ='X'

        elif estadoActual =='Z' and caracter != '':
                estadoActual = 'X'
        elif estadoActual == 'X':
            break             
    if estadoFinal == estadoActual :
          print('Es el token si')
    else: print('No es un token si')
             
 
''' afd_si("si")       
afd_si("a") 
 '''

 


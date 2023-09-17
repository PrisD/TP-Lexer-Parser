import lexer as lexer

"""Implementar un analizador sintáctico descendente predictivo por
procedimientos.
Enunciado
➔ La implementación del analizador sintáctico descendente predictivo con
tabla se realizará en grupo de hasta cuatro alumnos, el mismo grupo que el
formado para el TP N°1 de laboratorio.
➔ Cada grupo implementará el analizador para la misma gramática utilizada en
el TP N°1, utilizando el analizador lexicográfico producido para dicho
trabajo.
➔ Debe verificarse que la gramática dada cumple las condiciones teóricas
para poder analizarse con el tipo de analizador sintáctico solicitado.
➔ El programa que resulte de la implementación deberá recibir una cadena y
luego indicar si dicha cadena pertenece al lenguaje generado por la
gramática y además deberá indicar qué producciones de la gramática
deben ser usadas para derivar la cadena de entrada, en caso de
pertenecer.
Aquí enumeramos algunas consideraciones a tener en cuenta a la hora de
desarrollar el trabajo, respecto al formato del código, versión del software,
formato y nombre de las entregas, etc , a modo de recordatorio de lo sugerido en
clase:
1
➔ No utilizar funciones tipo input o cualquier interactividad que requiera la
intervención del usuario más allá de correr el programa, pues esto dificulta
el desarrollo para los alumnos y la evaluación por parte del profesor.
➔ Enviar todos los archivos necesarios para correr el programa comprimidos
en un único archivo con formato zip, rar o similares.
El analizador sintáctico se realizará utilizando la misma gramática que en el TP N°1,
con las mismas consideraciones que allí fue indicado.
Por cuestiones de claridad, la gramática G=<VN, VT, P, S> se repite completa para
"""

VNT = ['Program','ListaSentencias','ListaSentencias+','Sentencia','SentenciaSi','SentenciaRepetir','SentenciaAsig','SentenciaLeer','SentenciaMostrar','SentenciaFunc','Proc','ListaPar','ListaPar+','Expresion','Expresion+','Expresion2','Expresion2+','Termino','Termino+','Factor']
VT=[token for token, nombre in lexer.TOKENS_POSIBLES] #extrae los tokens de la tupla de la lista de Tokens Posibles


tablaProducciones = {
        'Program' : { 'si' : ['ListaSentencias'],
                    'repetir' : ['ListaSentencias'],
                    'id' : ['ListaSentencias'],
                    'leer' : ['ListaSentencias'],
                    'mostrar' : ['ListaSentencias'],
                    'func' : ['ListaSentencias'] },

        'ListaSentencias' : { 'si' : ['Sentencia' , 'ListaSentencias+'],
                            'repetir' : ['Sentencia' , 'ListaSentencias+'],
                            'id' : ['Sentencia' , 'ListaSentencias+'],
                            'leer' : ['Sentencia' , 'ListaSentencias+'],
                            'mostrar' : ['Sentencia' , 'ListaSentencias+'],
                            'func' : ['Sentencia' , 'ListaSentencias+'] },

        'ListaSentencias+' : { ';' : [';' , 'Sentencia' , 'ListaSentencias+'],
                            '#' : [],
                            'sino' : [],
                            'finsi' : [],
                            'hasta' : [], },

        'Sentencia' : { 'si' : ['SentenciaSi'],
                       'repetir' : ['SentenciaRepetir'],
                       'id' : ['SentenciaAsig'],
                       'leer' : ['SentenciaLeer'],
                       'mostrar' : ['SentenciaMostrar'],
                       'func' : ['SentenciaFunc'] },
                        
        'SentenciaSi' : { 'si' : ['si' , 'Expresion' , 'entonces' , 'ListaSentencias' , 'SentenciaSi+'] },     

        'SentenciaSi+' : { 'sino' : ['sino' , 'ListaSentencia' , 'finsi'],
                           'finsi' : ['finsi'] },

        'SentenciaRepetir' : { 'repetir' : ['repetir' , 'ListaSentencias' , 'hasta' , 'Expresion'] },

        'SentenciaAsig' : { 'id' : ['id' , 'equal' , 'Expresion'] },

        'SentenciaLeer' : { 'leer' : ['leer' , 'id'] },

        'SentenciaMostrar' : { 'mostrar' : ['mostrar' , 'Expresion'] },

        'SentenciaFunc' : { 'func' : ['func' , 'Proc' , 'finfunc'] },

        'Proc' : { 'id' : ['id' , '(' , 'ListaPar' , ')' , 'ListaSentencias'] }, 

        'ListaPar' : { 'id' : ['id' , 'ListaPar+'] },

        'ListaPar+' : { ';' : [';' , 'id' , 'ListaPar+'],
                       ')' : [] } ,

        'Expresion' : { 'id' : ['Expresion2' , 'Expresion+'],
                       '(' : ['Expresion2' , 'Expresion+'],
                       'num' : ['Expresion2' , 'Expresion+'], },

        'Expresion+' : { 'oprel' : ['oprel' , 'Expresion2'],
                        'entonces' : [],
                        ';' : [], },    

        'Expresion2' : { 'id' : ['Termino' , 'Expresion2+'],
                        '(' : ['Termino' , 'Expresion2+'],
                        'num' : ['Termino' , 'Expresion2+'], }, 

        'Expresion2+' : { 'opsum' : ['opsum' , 'Expresion2+'],
                        ';' : [],
                        'oprel' : [],
                        'entonces' : [], },   

        'Termino' : { 'id' : ['Factor'  , 'Termino+'],
                     '(' : ['Factor' , 'Termino+'],
                     'num' : ['Factor' , 'Termino+'], },  

        'Termino+' : { 'opmult' : ['opmult' , 'Termino+'],
                     'opsum' : [],
                     'oprel' : []  },

        'Factor' : { 'id' : ['id'],
                     '(' : ['(' , 'Expresion' , ')'],
                     'num' : ['num'], }           
}

lexemas = lexer.lexer(lexer.texto)



def parser(codigo):
    codigo=[token for token, nombre in lexemas] #extrae los tokens de la tupla
    codigo.append('#')
    posicionActual=0
    t = codigo[posicionActual]
    pila = ['#', 'Program']
    tope = pila[-1] #Accede al ultimo elemente de la lista
    while True: #Termina cuando tope y t son '#'
        if tope=='#' and t=='#':
            return 'La cadena pertenece'
        if tope in VT:
            if tope==t :
                pila.pop() #Remueve el ultimo elemento de la lista
                posicionActual = posicionActual + 1 
                t = codigo[posicionActual]  
            else:
                 return False
        elif tope in VNT:
            if  t in tablaProducciones[tope]: #Se fija si existe una produccion entre el no terminal actual en tope y el terminal al que apunta t
                produccion = tablaProducciones[tope].get(t)
                print(tope, ' -> ', produccion)
                produccion.reverse()
                pila.pop()
                for token in produccion:
                    pila.append(token) #Agrega al tope de la pila la produccion
            else:
                return ('No existe produccion entre ', tope, 'y ', t)  
        tope = pila[-1]
        
print(parser(lexemas))
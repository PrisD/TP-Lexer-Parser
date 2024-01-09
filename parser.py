import lexer as lexer
from collections import OrderedDict

VNT = ['Program','ListaSentencias','ListaSentencias+','Sentencia','SentenciaSi','SentenciaSi+','SentenciaRepetir','SentenciaAsig','SentenciaLeer','SentenciaMostrar','SentenciaFunc','Proc','ListaPar','ListaPar+','Expresion','Expresion+','Expresion2','Expresion2+','Termino','Termino+','Factor']
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
                            'hasta' : [],
                            'finfunc' : [] },

        'Sentencia' : { 'si' : ['SentenciaSi'],
                       'repetir' : ['SentenciaRepetir'],
                       'id' : ['SentenciaAsig'],
                       'leer' : ['SentenciaLeer'],
                       'mostrar' : ['SentenciaMostrar'],
                       'func' : ['SentenciaFunc'] },
                        
        'SentenciaSi' : { 'si' : ['si' , 'Expresion' , 'entonces' , 'ListaSentencias' , 'SentenciaSi+'] },     

        'SentenciaSi+' : { 'sino' : ['sino' , 'ListaSentencias' , 'finsi'],
                           'finsi' : ['finsi'] },

        'SentenciaRepetir' : { 'repetir' : ['repetir' , 'ListaSentencias' , 'hasta' , 'Expresion'] },

        'SentenciaAsig' : { 'id' : ['id' , 'equal' , 'Expresion'] },

        'SentenciaLeer' : { 'leer' : ['leer' , 'id'] },

        'SentenciaMostrar' : { 'mostrar' : ['mostrar' , 'Expresion'] },

        'SentenciaFunc' : { 'func' : ['func' , 'Proc' , 'finfunc'] },

        'Proc' : { 'id' : ['id' , '(' , 'ListaPar' , ')' , 'ListaSentencias'] }, 

        'ListaPar' : { 'id' : ['id' , 'ListaPar+'] },

        'ListaPar+' : { ';' : [';' , 'id' , 'ListaPar+'],
                       ')' : [] },

        'Expresion' : { 'id' : ['Expresion2' , 'Expresion+'],
                       '(' : ['Expresion2' , 'Expresion+'],
                       'num' : ['Expresion2' , 'Expresion+'] },

        'Expresion+' : { 'oprel' : ['oprel' , 'Expresion2'],
                        'entonces' : [],
                        ';' : [],
                        '#' : [],
                        'finsi' : [],
                        'sino' : [],
                        'hasta' : [],
                        ')' : [],
                        'finfunc' : [] },    
       
        'Expresion2' :  {'id' : ['Termino' , 'Expresion2+'],
                        '(' : ['Termino' , 'Expresion2+'],
                        'num' : ['Termino' , 'Expresion2+']}, 

        'Expresion2+' : { 'opsum' : ['opsum' , 'Termino', 'Expresion2+'],
                        ';' : [],
                        'oprel' : [],
                        'entonces' : [],
                        '#' : [],
                        ')' : [],
                        'sino' : [],
                        'finsi' : [],
                        'finfunc' : [],
                        'hasta' : [] },   

        'Termino' : { 'id' : ['Factor'  , 'Termino+'],
                     '(' : ['Factor' , 'Termino+'],
                     'num' : ['Factor' , 'Termino+'], },  

        'Termino+' : { 'opmult' : ['opmult' , 'Factor' , 'Termino+'],
                     'opsum' : [],
                     'oprel' : [],
                     '#' : [],
                     ')' : [],
                     'entonces' : [],
                     ';' : [],
                     'sino' : [],
                     'finsi' : [],
                     'finfunc' : [],
                     'hasta' : [] },

        'Factor' : { 'id' : ['id'],
                     '(' : ['(' , 'Expresion' , ')'],
                     'num' : ['num'], }           
}

def parser(codigo):
    codigo=[token for token, nombre in lexemas] #extrae los tokens de la tupla
    codigo.append('#')
    posicionActual=0
    ListaProducciones =[] # Lista donde se almacenarán las producciones utilizadas en caso de pertenecer al lenguaje
    t = codigo[posicionActual]
    pila = ['#', 'Program']
    tope = pila[-1] #Accede al ultimo elemento de la 
    while True: #Termina cuando tope y t son '#'
        if tope=='#' and t=='#':
            print('La lista de Producciones utilizadas es: ' , ListaProducciones)
            return 'La cadena pertenece al lenguaje'
        if tope in VT:
            if tope==t :
                pila.pop() #Remueve el ultimo elemento de la lista
                posicionActual = posicionActual + 1 
                t = codigo[posicionActual] 
            else:
                 return 'La cadena no pertenece al lenguaje'
        elif tope in VNT:
            if  t in tablaProducciones[tope]: #Se fija si existe una produccion entre el no terminal actual en tope y el terminal al que apunta t             
                produccion = tablaProducciones[tope].get(t)
                ListaProducciones.append(tope + ' -> ' + ' '.join(produccion)) #Se acumulan las producciones utilizadas en la lista
                pila.pop()
                for token in reversed(produccion):
                    pila.append(token) #Agrega al tope de la pila la produccion
            else:
                return ('La cadena no pertenece al lenguaje') 
        tope = pila[-1]

lexemas = lexer.lexer(lexer.texto)
print(parser(lexemas))
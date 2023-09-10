import lexer as lexerTp

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

VNT = ["Programa","ListaSentencias","LS","Sentencias","SS","SentenciaSi","SentenciaRepetir","SentenciaAsig","SentenciaLeer","SentenciaMostrar","SentenciaFun","Proc","ListaPar","LP","Expresion","E","Exprecion2","E2","Termino","T","Factor"]
VT = lexerTp.TOKENS_POSIBLES

"""
Simbolos directrices de la gramatica:

sd(p -> ls) = {si,repetir,id,leer,mostrar,func}
sd(ls -> s ls') = {si,repetir,id,leer,mostrar,func}
sd(ls' -> lambda) = vacio
sd(ls' -> ; ls) = {;}
sd(s -> ss) = {si}
sd(s -> sr) = {repetir}
sd(s -> sa) = {id}
sd(s -> sl) = {leer}
sd(s -> sm) = {mostrar}
sd(s -> sf) = {func}
sd(ss -> si e entonces ls ss') = {si}
sd(ss' -> finsi) = {finsi}
sd(ss' -> sino ls finsi) = {sino}
sd(sr -> repetir ls hasta e) = {repetir}
sd(sa -> id equal e) =  {id}
sd(sl -> leer id) =  {leer}
sd(sm -> mostrar e) =  {mostrar}
sd(sf -> func pr finfunc) =  {func}
sd(pr -> id ( lp ) ls) =  {id}
sd(lp -> id lp') =  {id}
sd(lp' -> lambda) =  vacio
sd(lp' -> ; lp) =  {;}
sd(e -> e2 e') =  {(,num,id}
sd(e' -> lambda) =  vacio
sd(e' -> oprel) =  {<,>,=,<=,>=}
sd(e2 -> t e2') =  {(,num,id}
sd(e2' -> lambda) =  vacio
sd(e2' -> opsuma e2) =  {-,+}
sd(t -> f t') =  {(,num,id}
sd(t' -> lambda) =  vacio
sd(t' -> opmult t) =  {/,*}
sd(f -> ( e )) =  {(}
sd(f -> num) = {num}
sd(f -> id) = {id}


"""



def parser(codigo):
    # tablaProducciones = insertarDiccionario
    posicionActual=0
    t = codigo[posicionActual]
    pila = ['#','Program']
    tope = pila[-1] #Accede al ultimo elemente de la lista
    while not(tope=='#') and not(t=='#'): #Termina cuando tope y t son '#'
        if tope in VT:
            if (tope==t) :
                pila.pop() #Remueve el ultimo elemento de la lista
                posicionActual = posicionActual + 1 
            else:
                return False
            
        else:
            if 't' in tablaProducciones['tope']: #Se fija si existe una produccion entre el no terminal actual en tope y el terminal al que apunta t
                produccion = tablaProducciones['tope'].get('t')
                pila.pop()
                pila.append(produccion) #Agrega al tope de la pila produccion
            else:
                return False
            
    return 'La cadena pertenece al lenguaje'
        
         




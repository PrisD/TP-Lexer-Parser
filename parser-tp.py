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

tokens= lexerTp.lexer("")

diccionario = {
    "Programa": [["ListaSentencias"]],
    "ListaSentencias" : [["Sentencias","LS"]], 
    "LS": [[""],[";","ListaSentencias"]],
    "Sentencias" : [["SentenciaSi"],["SentenciaRepetir"],["SentenciaAsig"],["SentenciaLeer"],["SentenciaMostrar"],["SentenciaFun"]],
    "SentenciaSi": [["si","Expresion", "entonces","ListaSentencias"],"SS"],
    "SS": [["finsi"],["sino","ListaSentencias","finsi"]],
    "SentenciaRepetir": [["repetir","ListaSentencias","hasta","Expresion"]],
    "SentenciaAsig": [["id","=","Expresion"]],
    "SentenciaLeer": [["leer","id"]],
    "SentenciaMostrar": [["mostrar","Expresion"]],
    "SentenciaFun": [["func","Proc","finfunc"]],
    "Proc": [["id","(","ListaPar",")","ListaSentencias"]],
    "ListaPar": [["id","LP"]],
    "LP": [[""],[";","ListaPar"]],
    "Expresion": [["Exprecion2","E"]],
    "E": [[""],["oprel","Exprecion2"]],
    "Exprecion2": [["Termino","E2"]],
    "E2": [[""],["opsuma","E2"]],
    "Termino": [["Factor","T"]],
    "T": [[""],["opmult","Termino"]],
    "Factor": [["id"],["num"],["(","Expresion",")"]]
}

first()
VN = {Program,ListaSentencias,ListaSentencias',Sentencia,SentenciaSi,SentenciaRepetir,SentenciaAsig,SentenciaLeer,
SentenciaMostrar,SentenciaFunc,SentenciaSi',Proc,ListaPar,ListaPar',Expresion,Expresion',Expresion2,Expresion2',
Termino,Termino',Factor}
VT = {;,si,sino,finsi,repetir,id,leer,mostrar,func,(,),finfunc,+,-,=,<,>,=<,>=,num,hasta,equal,/,*}


Program → ListaSentencias
ListaSentencias → Sentencia ListaSentencias'
ListaSentencias' → ; Sentencia ListaSentencias'
| lambda
Sentencia → SentenciaSi
| SentenciaRepetir
| SentenciaAsig
| SentenciaLeer
| SentenciaMostrar
| SentenciaFunc
SentenciaSi → si Expresion entonces ListaSentencias SentenciaSi'
SentenciaSi' → sino ListaSentencia finsi
|finsi
SentenciaRepetir → repetir ListaSentencias hasta Expresion
SentenciaAsig → id equal Expresion
SentenciaLeer → leer id
SentenciaMostrar → mostrar Expresion
SentenciaFunc → func Proc finfunc
Proc → id ( ListaPar ) ListaSetencias
LispaPar → id ListaPar'
ListaPar' → ; id ListaPar'
| lambda
Expresion → Expresion2 Expresion'
Expresion' → oprel Expresion2
| lambda
Expresion2 → Termino Expresion2'
Expresion2' → opsuma Expresion2'
| lambda
Termino → Factor Termino'
Termino' → opmult Termino'
| lambda
Factor → ( Expresion )
| num 
| id

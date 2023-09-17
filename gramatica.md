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
ListaPar → id ListaPar'
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


Simbolos directrices de la gramatica:

sd(p -> ls) = {si,repetir,id,leer,mostrar,func}
sd(ls -> s ls') = {si,repetir,id,leer,mostrar,func}
sd(ls' -> lambda) = {#,hasta,sino,finsi,}
sd(ls' -> ; s ls) = {;}
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
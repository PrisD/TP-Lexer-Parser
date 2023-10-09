ESTADO_NO_FINAL = 'ESTADO NO FINAL'
ESTADO_ACEPTADO = 'ESTADO ACEPTADO'
ESTADO_TRAMPA = 'ESTADO TRAMPA'

# LOS AUTOMATAS ESTAN EN EL ORDEN MISMO QUE POSEEN LOS TOKEN

def afd_par_abre (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == '(':
            estado_actual = 'Z'
        elif estado_actual == 'A'and caracter != '(':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_par_cierra (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == ')':
            estado_actual = 'Z'
        elif estado_actual == 'A'and caracter != ')':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_punto_coma (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == ';':
            estado_actual = 'Z'
        elif estado_actual == 'A'and caracter != ';':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_finfunc (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == 'f':
            estado_actual = 'B'
        elif estado_actual == 'A' and caracter != 'f':
            estado_actual = 'X'
        elif estado_actual == 'B' and caracter == 'i':
            estado_actual = 'C'
        elif estado_actual == 'B' and caracter != 'i':
            estado_actual = 'X'
        elif estado_actual == 'C' and caracter == 'n':
            estado_actual = 'D'
        elif estado_actual == 'C' and caracter != 'n':
            estado_actual = 'X'
        elif estado_actual == 'D' and caracter == 'f':
            estado_actual = 'E'
        elif estado_actual == 'D' and caracter != 'f':
            estado_actual = 'X'
        elif estado_actual == 'E' and caracter == 'u':
            estado_actual = 'F'
        elif estado_actual == 'E' and caracter != 'u':
            estado_actual = 'X'
        elif estado_actual == 'F' and caracter == 'n':
            estado_actual = 'G'
        elif estado_actual == 'F' and caracter != 'n':
            estado_actual = 'X'
        elif estado_actual == 'G' and caracter == 'c':
            estado_actual = 'Z'
        elif estado_actual == 'G' and caracter != 'c':
            estado_actual = 'X'
        elif estado_actual =='Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual =='X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_entonces (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == 'e':
            estado_actual = 'B'
        elif estado_actual == 'A' and caracter != 'e':
            estado_actual = 'X'
        elif estado_actual == 'B' and caracter == 'n':
            estado_actual = 'C'
        elif estado_actual == 'B' and caracter != 'n':
            estado_actual = 'X'
        elif estado_actual == 'C' and caracter == 't':
            estado_actual = 'D'
        elif estado_actual == 'C' and caracter != 't':
            estado_actual = 'X'
        elif estado_actual == 'D' and caracter == 'o':
            estado_actual = 'E'
        elif estado_actual == 'D' and caracter != 'o':
            estado_actual = 'X'
        elif estado_actual == 'E' and caracter == 'n':
            estado_actual = 'F'
        elif estado_actual == 'E' and caracter != 'n':
            estado_actual = 'X'
        elif estado_actual == 'F' and caracter == 'c':
            estado_actual = 'G'
        elif estado_actual == 'F' and caracter != 'c':
            estado_actual = 'X'
        elif estado_actual == 'G' and caracter == 'e':
            estado_actual = 'H'
        elif estado_actual == 'G' and caracter != 'e':
            estado_actual = 'X'
        elif estado_actual == 'H' and caracter == 's':
            estado_actual = 'Z'
        elif estado_actual == 'H' and caracter != 's':
            estado_actual = 'X'
        elif estado_actual =='Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual =='X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_mostrar (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == 'm':
            estado_actual = 'B'
        elif estado_actual == 'A' and caracter != 'm':
            estado_actual = 'X'
        elif estado_actual == 'B' and caracter == 'o':
            estado_actual = 'C'
        elif estado_actual == 'B' and caracter != 'o':
            estado_actual = 'X'
        elif estado_actual == 'C' and caracter == 's':
            estado_actual = 'D'
        elif estado_actual == 'C' and caracter != 's':
            estado_actual = 'X'
        elif estado_actual == 'D' and caracter == 't':
            estado_actual = 'E'
        elif estado_actual == 'D' and caracter != 't':
            estado_actual = 'X'
        elif estado_actual == 'E' and caracter == 'r':
            estado_actual = 'F'
        elif estado_actual == 'E' and caracter != 'r':
            estado_actual = 'X'
        elif estado_actual == 'F' and caracter == 'a':
            estado_actual = 'G'
        elif estado_actual == 'F' and caracter != 'a':
            estado_actual = 'X'
        elif estado_actual == 'G' and caracter == 'r':
            estado_actual = 'Z'
        elif estado_actual == 'G' and caracter != 'r':
            estado_actual = 'X'
        elif estado_actual =='Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual =='X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_repetir (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == 'r':
            estado_actual = 'B'
        elif estado_actual == 'A' and caracter != 'r':
            estado_actual = 'X'
        elif estado_actual == 'B' and caracter == 'e':
            estado_actual = 'C'
        elif estado_actual == 'B' and caracter != 'e':
            estado_actual = 'X'
        elif estado_actual == 'C' and caracter == 'p':
            estado_actual = 'D'
        elif estado_actual == 'C' and caracter != 'p':
            estado_actual = 'X'
        elif estado_actual == 'D' and caracter == 'e':
            estado_actual = 'E'
        elif estado_actual == 'D' and caracter != 'e':
            estado_actual = 'X'
        elif estado_actual == 'E' and caracter == 't':
            estado_actual = 'F'
        elif estado_actual == 'E' and caracter != 't':
            estado_actual = 'X'
        elif estado_actual == 'F' and caracter == 'i':
            estado_actual = 'G'
        elif estado_actual == 'F' and caracter != 'i':
            estado_actual = 'X'
        elif estado_actual == 'G' and caracter == 'r':
            estado_actual = 'Z'
        elif estado_actual == 'G' and caracter != 'r':
            estado_actual = 'X'
        elif estado_actual =='Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual =='X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_opsuma (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == '+':
            estado_actual = 'Z'
        elif estado_actual == 'A' and caracter == '-':
            estado_actual = 'Z'
        elif estado_actual == 'A' and caracter != '+' and caracter != '-':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_opmult (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == '*':
            estado_actual = 'Z'
        elif estado_actual == 'A' and caracter == '/':
            estado_actual = 'Z'
        elif estado_actual == 'A' and caracter != '*' and caracter != '/':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_oprel (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == '=':
            estado_actual = 'Z'
        elif estado_actual == 'A' and caracter == '<':
            estado_actual = 'Z'
        elif estado_actual == 'A' and caracter == '>':
            estado_actual = 'Z'
        elif estado_actual == 'A' and caracter == '<=':
            estado_actual = 'Z'
        elif estado_actual == 'A' and caracter == '>=':
            estado_actual = 'Z'
        elif estado_actual == 'A' and caracter != '=' and caracter != '<' and caracter != '>' and caracter != '<=' and caracter != '>=':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_equal (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == 'e':
            estado_actual = 'B'
        elif estado_actual == 'A' and caracter != 'e':
            estado_actual = 'X'
        elif estado_actual == 'B' and caracter == 'q':
            estado_actual = 'C'
        elif estado_actual == 'B' and caracter != 'q':
            estado_actual = 'X'
        elif estado_actual == 'C' and caracter == 'u':
            estado_actual = 'D'
        elif estado_actual == 'C' and caracter != 'u':
            estado_actual = 'X'
        elif estado_actual == 'D' and caracter == 'a':
            estado_actual = 'E'
        elif estado_actual == 'D' and caracter != 'a':
            estado_actual = 'X'
        elif estado_actual == 'E' and caracter == 'l':
            estado_actual = 'Z'
        elif estado_actual == 'E' and caracter != 'l':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_func (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == 'f':
            estado_actual = 'B'
        elif estado_actual == 'A' and caracter != 'f':
            estado_actual = 'X'
        elif estado_actual == 'B' and caracter == 'u':
            estado_actual = 'C'
        elif estado_actual == 'B' and caracter != 'u':
            estado_actual = 'X'
        elif estado_actual == 'C' and caracter == 'n':
            estado_actual = 'D'
        elif estado_actual == 'C' and caracter != 'n':
            estado_actual = 'X'
        elif estado_actual == 'D' and caracter == 'c':
            estado_actual = 'Z'
        elif estado_actual == 'D' and caracter != 'c':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_finsi (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == 'f':
            estado_actual = 'B'
        elif estado_actual == 'A' and caracter != 'f':
            estado_actual = 'X'
        elif estado_actual == 'B' and caracter == 'i':
            estado_actual = 'C'
        elif estado_actual == 'B' and caracter != 'i':
            estado_actual = 'X'
        elif estado_actual == 'C' and caracter == 'n':
            estado_actual = 'D'
        elif estado_actual == 'C' and caracter != 'n':
            estado_actual = 'X'
        elif estado_actual == 'D' and caracter == 's':
            estado_actual = 'E'
        elif estado_actual == 'D' and caracter != 's':
            estado_actual = 'X'
        elif estado_actual == 'E' and caracter == 'i':
            estado_actual = 'Z'
        elif estado_actual == 'E' and caracter != 'i':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_hasta (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == 'h':
            estado_actual = 'B'
        elif estado_actual == 'A' and caracter != 'h':
            estado_actual = 'X'
        elif estado_actual == 'B' and caracter == 'a':
            estado_actual = 'C'
        elif estado_actual == 'B' and caracter != 'a':
            estado_actual = 'X'
        elif estado_actual == 'C' and caracter == 's':
            estado_actual = 'D'
        elif estado_actual == 'C' and caracter != 's':
            estado_actual = 'X'
        elif estado_actual == 'D' and caracter == 't':
            estado_actual = 'E'
        elif estado_actual == 'D' and caracter != 't':
            estado_actual = 'X'
        elif estado_actual == 'E' and caracter == 'a':
            estado_actual = 'Z'
        elif estado_actual == 'E' and caracter != 'a':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_leer (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == 'l':
            estado_actual = 'B'
        elif estado_actual == 'A' and caracter != 'l':
            estado_actual = 'X'
        elif estado_actual == 'B' and caracter == 'e':
            estado_actual = 'C'
        elif estado_actual == 'B' and caracter != 'e':
            estado_actual = 'X'
        elif estado_actual == 'C' and caracter == 'e':
            estado_actual = 'D'
        elif estado_actual == 'C' and caracter != 'e':
            estado_actual = 'X'
        elif estado_actual == 'D' and caracter == 'r':
            estado_actual = 'Z'
        elif estado_actual == 'D' and caracter != 'r':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_sino (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == 's':
            estado_actual = 'B'
        elif estado_actual == 'A' and caracter != 's':
            estado_actual = 'X'
        elif estado_actual == 'B' and caracter == 'i':
            estado_actual = 'C'
        elif estado_actual == 'B' and caracter != 'i':
            estado_actual = 'X'
        elif estado_actual == 'C' and caracter == 'n':
            estado_actual = 'D'
        elif estado_actual == 'C' and caracter != 'n':
            estado_actual = 'X'
        elif estado_actual == 'D' and caracter == 'o':
            estado_actual = 'Z'
        elif estado_actual == 'D' and caracter != 'o':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_si (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter == 's':
            estado_actual = 'B'
        elif estado_actual == 'A' and caracter != 's':
            estado_actual = 'X'
        elif estado_actual == 'B' and caracter == 'i':
            estado_actual = 'Z'
        elif estado_actual == 'B' and caracter != 'i':
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isascii():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL     
def afd_id (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter.isalpha():
            estado_actual = 'Z'
        elif estado_actual == 'A' and not caracter.isalpha():
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isalnum():
            estado_actual = 'Z'
        elif estado_actual == 'Z' and not caracter.isalnum():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL
def afd_num (lexema):
    estado_actual = 'A'
    estado_final = 'Z'
    estado_trampa = 'X'
    for caracter in lexema:
        if estado_actual == 'A' and caracter.isdigit():
            estado_actual = 'Z'
        elif estado_actual == 'A' and not caracter.isdigit():
            estado_actual = 'X'
        elif estado_actual == 'Z' and caracter.isdigit():
            estado_actual = 'Z'
        elif estado_actual == 'Z' and not caracter.isdigit():
            estado_actual = 'X'
        elif estado_actual == 'X' and caracter.isascii():
            estado_actual = 'X'
    if  estado_actual == estado_final:
        return ESTADO_ACEPTADO
    elif estado_actual == estado_trampa:
        return ESTADO_TRAMPA
    else:
        return ESTADO_NO_FINAL    

TOKENS_POSIBLES = [("(", afd_par_abre),(")", afd_par_cierra),(";", afd_punto_coma),("finfunc", afd_finfunc),("entonces",afd_entonces),("mostrar", afd_mostrar),
                   ("repetir",afd_repetir),("opsum", afd_opsuma),("opmult", afd_opmult),("oprel", afd_oprel),("equal", afd_equal),("func", afd_func),("finsi", afd_finsi),
                    ("hasta", afd_hasta),("leer", afd_leer),("sino", afd_sino),("si", afd_si),("id", afd_id),("num", afd_num),("desconocido", afd_id)]

def lexer(codigo):
    tokens = []
    posActual = 0  # pos es referencia a posicion
    while posActual < len(codigo):
        while posActual < len(codigo) and codigo[posActual].isspace():  # salta los espacios en blanco
            posActual = posActual + 1
        
        inicio_lexema = posActual
        tokens_Posible = []
        tokens_Posible_mas1 = []  # mas1 hace referencia a calcular un token posible agregando un caracter al lexema
        lexema = ""
        todos_trampa = False

        while todos_trampa == False and posActual <= len(codigo):  # todavia hay posibles
            todos_trampa = True
            lexema = codigo[inicio_lexema:posActual+1]
            tokens_Posible = tokens_Posible_mas1
            tokens_Posible_mas1 = []

            for (un_token, afd) in TOKENS_POSIBLES:  # analiza todos los automatas
                simulacion_afd = afd(lexema)
                if simulacion_afd == ESTADO_ACEPTADO:
                    tokens_Posible_mas1.append(un_token)
                    todos_trampa = False
                elif simulacion_afd == ESTADO_NO_FINAL:
                    todos_trampa = False  
                    
            posActual = posActual + 1 
        
        if len(tokens_Posible) == 0:
            print("error: token desconocido " + "'" + lexema + "'")

        posActual = posActual - 1
        un_token = tokens_Posible [0]
        token = (un_token, codigo[inicio_lexema:posActual]) 
        tokens.append(token)
    return tokens

texto='leer si entonces finsi repetir hasta'
# print(lexer(texto))

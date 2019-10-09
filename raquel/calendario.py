def calendario (inicio,numdias):
    str = "  D  L MA MI  J  V  S\n"
    inicio = inicio - 1
    dias = 1
    posicion = 0
    for x in range(0, inicio):
        str += formato(None)
        posicion = posicion + 1

    for x in range(1,numdias + 1):
        str += formato(x)
        posicion = posicion + 1
        if posicion % 7 == 0:
            str += "\n"
    return str

def formato(dias):
    if dias == None:
        return "   "
    if dias < 10:
        return "  "+str(dias)
    else:
        return " "+str(dias)

print(calendario(4,31))

mensaje = "Fundamentos de programacion"
consonantes= int (0)
vocales = int (0)
lstvocales = "a,e,i,o,u"
for caracter in mensaje:
    if "a" in lstvocales:
        if caracter in lstvocales:
            vocales +=1
        else:
            consonantes+=1


print (f"El total de vocales es = {vocales}")
print ("fEl total de consonantes es = {consonantes}")
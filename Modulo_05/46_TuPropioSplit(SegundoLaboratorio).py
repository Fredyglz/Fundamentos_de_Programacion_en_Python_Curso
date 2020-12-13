def misplit(strng):
    l_split = []
    palabra = ''
    strng = strng.strip() 
    if len(strng) > 0:
        strng = strng + ' '
        for c in strng:
            if c == ' ':
                l_split.append(palabra)
                palabra = ''
                continue
            palabra += c
    return l_split

print(misplit("Ser o no ser, esa es la pregunta"))
print(misplit("Ser o no ser,esa es la pregunta"))
print(misplit("   "))
print(misplit(" abc "))
print(misplit(""))

with open('listas.in', 'r') as archivo:
    contenido = archivo.read().strip()
    listas = contenido.split('.')
    listas = [lista.replace('\n', '').strip() for lista in listas if lista.strip()]
    
    for lista in listas:
        elementos = lista.split(', ')
        palabras = []
        numeros = []
        
        for elemento in elementos:
            if elemento.replace('-', '').isdigit():
                numeros.append(int(elemento))
            else:
                palabras.append(elemento)

        ordenarPalabras = sorted(palabras, key=str.lower)
        ordenarNumeros = sorted(numeros)
        
        listaOrdenada = []
        indexPalabras = 0
        indexNumeros = 0

        for elemento in elementos:
            if elemento.replace('-', '').isdigit():
                listaOrdenada.append(str(ordenarNumeros[indexNumeros]))
                indexNumeros += 1
            else:
                listaOrdenada.append(ordenarPalabras[indexPalabras])
                indexPalabras += 1

        resultado = ", ".join(listaOrdenada) + "."

        print(resultado)
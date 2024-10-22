def obtener_datos(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read().strip()

def limpiar_y_dividir(contenido):
    listas = contenido.split('.')
    return [lista.replace('\n', '').strip() for lista in listas if lista.strip()]

def separar_elementos(contenido):
    elementos = contenido.split(', ')
    palabras = list(filter(lambda x: not x.replace('-', '').isdigit(), elementos))
    numeros = list(filter(lambda x: x.replace('-', '').isdigit(), elementos))
    return sorted(palabras, key=str.lower), sorted(map(int, numeros))

def ordenar_lista(original, palabras_ordenadas, numeros_ordenados):
    lista_ordenada = []
    index_palabras = 0
    index_numeros = 0
    for elemento in original:
        if elemento.replace('-', '').isdigit():
            lista_ordenada.append(str(numeros_ordenados[index_numeros]))
            index_numeros += 1
        else:
            lista_ordenada.append(palabras_ordenadas[index_palabras])
            index_palabras += 1
    return lista_ordenada

contenido = obtener_datos('listas.in')
listas_limpias = limpiar_y_dividir(contenido)
for lista in listas_limpias:
    elementos = lista.split(', ')
    palabras_ordenadas, numeros_ordenados = separar_elementos(lista)
    lista_final = ordenar_lista(elementos, palabras_ordenadas, numeros_ordenados)
    print(", ".join(lista_final) + ".")

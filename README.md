# Proyecto de Ordenamiento de Listas

Este proyecto es una práctica sencilla que muestra cómo leer, limpiar y ordenar listas de palabras y números desde un archivo de texto. Es ideal para estudiantes que están aprendiendo sobre el procesamiento de datos y la programación en Python.

## Descripción del Programa

El programa lee el contenido de un archivo llamado `listas.in`, donde se encuentran listas de palabras y números separados por puntos (`.`). Luego, limpia y divide estas listas, separando las palabras de los números. Finalmente, ordena ambos grupos por separado y los combina de nuevo en la estructura original antes de imprimir los resultados.

## Estructura del Código

### Funciones Principales

- `obtener_datos(nombre_archivo)`: Lee el contenido de un archivo y elimina los espacios en blanco.
- `limpiar_y_dividir(contenido)`: Divide el contenido en listas separadas por puntos y elimina los saltos de línea.
- `separar_elementos(contenido)`: Separa los elementos de la lista en palabras y números, ordenándolos por separado.
- `ordenar_lista(original, palabras_ordenadas, numeros_ordenados)`: Reconstruye la lista original con las palabras y números ordenados.

### Ejecución del Programa

El programa se ejecuta llamando a las funciones en el siguiente orden:

1. `obtener_datos('listas.in')`: Obtiene el contenido del archivo.
2. `limpiar_y_dividir(contenido)`: Limpia y divide el contenido en listas.
3. `separar_elementos(contenido)`: Separa y ordena las palabras y números.
4. `ordenar_lista(elementos, palabras_ordenadas, numeros_ordenados)`: Reconstruye la lista ordenada.
5. Imprime el resultado final.


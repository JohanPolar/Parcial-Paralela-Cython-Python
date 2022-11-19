# **Algoritmo KMP (Knuth-Morris-Pratt)**

El algoritmo KMP es un algoritmo de búsqueda de subcadenas simple. Por lo tanto su objetivo es buscar la existencia de una subcadena (habitualmente llamada patrón) dentro de otra cadena. La búsqueda se lleva a cabo utilizando información basada en los fallos previos. Información obtenida del propio patrón creando previamente una tabla de valores sobre su propio contenido. El objetivo de crear dicha tabla es poder determinar donde podría darse la siguiente existencia, sin necesidad de analizar más de 1 vez los caracteres de la cadena donde se busca.

El algoritmo KMP trata de localizar la posición de comienzo de una cadena dentro de otra. Previamente sobre el patrón a localizar se calcula una tabla de saltos (conocida como tabla de fallos) que después se utiliza (al examinar las cadenas) para hacer saltos cuando se localiza un fallo de coincidencia en la comparación de un carácter.

[Referencia](https://es.wikipedia.org/wiki/Algoritmo_Knuth-Morris-Pratt)

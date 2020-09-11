# Tarea 1 - Pruebas de Software
Gaspar Correa Vergara

# Descripcion
Se necesita cumplir con un requirimiento que exige una funcion compare dos strings y retorne aquel
de mayor largo en caracteres.

# Implementacion
Se implementara la funcion en el lenguaje Python

# Supuestos adicionales
* Se asumira que el formato de codificacion permitido por la funcion es UTF8, por lo que debe funcionar con cualquier caracter que pertenezca a este formato.
* Adicionalmente, en caso de que ambos argumentos tengan el mismo largo en caracteres, se procedera a retornar el segundo argumento.

# Dependencias
La unica libreria usada es datetime para efectos de logging. No es necesario ninguna dependencia adicional a las librerias basicas de python.

# Instrucciones de ejecucion
Dentro del repositorio se incluye el archivo 'test_cases.txt' el cual incluye 17 casos de pruebas distintos. El formato de este archivo son lineas de 3 cadenas de caracteres separadas por una coma.

Para ejecutar el codigo es necesario tener en el mismo directorio el archivo de prueba.

```
 python .\tarea.py
```

# Output de ejemplo
Usando el archivo de test incluido en el repositorio, el output debiese ser el siguiente:

```
2020-09-10 23:24:09.671238  - Testing: Reading test_cases.txt
2020-09-10 23:24:09.759413  - Testing: str1:  F , str2: 3512 , expected: 3512 , result: 3512 , correct: True
2020-09-10 23:24:09.760259  - Testing: str1:  4543** , str2: 321 , expected: 4543** , result: 4543** , correct: True
2020-09-10 23:24:09.761246  - Testing: str1:  'a''s , str2: $%^!@#%& , expected: $%^!@#%& , result: $%^!@#%& , correct: True
2020-09-10 23:24:09.775068  - Testing: str1:  JFJFJDDDD , str2: aaaaaaaDeeeeeee , expected: aaaaaaaDeeeeeee , result: aaaaaaaDeeeeeee , correct: True
2020-09-10 23:24:09.776066  - Testing: str1:  a , str2: b , expected: b , result: b , correct: True
2020-09-10 23:24:09.776066  - Testing: str1:  .=.=.= , str2: -=-=-=@!@!@! , expected: -=-=-=@!@!@! , result: -=-=-=@!@!@! , correct: True
2020-09-10 23:24:09.800997  - Testing: str1:  Gaspar , str2: gaspar , expected: gaspar , result: gaspar , correct: True
2020-09-10 23:24:10.356279  - Testing: str1:  reunión , str2: reunion , expected: reunion , result: reunion , correct: True
2020-09-10 23:24:10.397206  - Testing: str1:  L A L A , str2: lala , expected: L A L A , result: L A L A , correct: True   
2020-09-10 23:24:10.397763  - Testing: str1:  uno , str2: dos , expected: dos , result: dos , correct: True
2020-09-10 23:24:10.397763  - Testing: str1:  microµ , str2: bus , expected: microµ , result: microµ , correct: True       
2020-09-10 23:24:10.506023  - Testing: str1:  ϏЖЖЖЖЊ , str2: pan , expected: ϏЖЖЖЖЊ , result: ϏЖЖЖЖЊ , correct: True       
2020-09-10 23:24:10.508984  - Testing: str1:  ѸLѸѸ , str2: LoLaa , expected: LoLaa , result: LoLaa , correct: True
2020-09-10 23:24:10.589582  - Testing: str1:  Manzanas , str2: Peras , expected: Manzanas , result: Manzanas , correct: True
2020-09-10 23:24:10.614402  - Testing: str1:  ݽݾݾݾݾ , str2: what , expected: ݽݾݾݾݾ , result: ݽݾݾݾݾ , correct: True
2020-09-10 23:24:10.631471  - Testing: str1:  1 , str2: uno , expected: uno , result: uno , correct: True
2020-09-10 23:24:10.773079  - Testing: str1:  testfinal , str2: error , expected: testfinal , result: testfinal , correct: 
True
2020-09-10 23:24:10.774869  - Finished:  17  of  17  cases were correct.
```

# Material Complementario
[The difference between verification and validation](https://www.easterbrook.ca/steve/2010/11/the-difference-between-verification-and-validation/)
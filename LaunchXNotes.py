""" 
*******   Operaciones matematicas

+
-
*
/
// División conocida como división de piso. Hace la división y redondea hacia abajo
%  Operador modulo
round Redondea al entero mas cercano (menos que .5 redondea hacia abajo)

--> Jerarquía 
    1 parentesis
    2 exponentes
    3 multiplicacion y division
    4 suma y resta

--> Conversion de cadena
    int: transforma a entero
    float: acepta deciamles

==> Biblioteca Math
    floor: Redondea siempre hacia el entero mas cercano inferior
    ceil: Redondea siempre hacia el entero mas cercano superior

*******   Condiciones Logicas

Iguales: a == b
No es igual: a != b
Menos que: a < b
Menor o igual que: a <= b
Mayor que: a > b
Mayor o igual que: a >= b
Y: and
O: or

if a = b:
    # indicaciones

if a == 34 or b == 34:
    print(a + b)

if a = b:
    # indicaciones
else:
    # mas indicaciones

if a = b:
    # indicaciones
elif:
    # mas indicaciones (elif es la abreviatura de else if, para anidar ifs)

*******   Estructuras de Control

while condicion:
    # instrucciones

for numero in contador:
    # instrucciones




*******   Listas 

len = obtener la longitud de una lista
.append(valor) = agregar un elemento a la lista
.pop = eliminar el ultimo elemento de una lista
.index(valor) = metodo que sirve para devolver en que parte esta un valor en una lista.
    si no encuentra devolvera un -1
max() = devuelve el valor maximo de una lista
min() = devuelve el valor minimo de una lista
lista[0:2] slice = este metodo crea una nueva lista desde los indices que se le indican de
    una lista ya existente
+ = se puede usar para unir dos listas, esto crea una nueva lista
.sort() = ordena una lista en orden alfabetico, o en orden numerico
.sort(reverse=true) = ordena una lista en orden inverso
.lower() =





TIP:
* Los indices negativos en listas trabajan de fin a inicio, siendo -1 el ultimo elemento, -2 
el penultimo y así.

*******   Entornos virtuales

Para crear el entorno vitual hay que ir al directorio donde se quiere crear y en consola
ejecutar el siguiente comando:

(python) -m venv (env)

En python se puede usar python3, python2 depende la version.
env sera el nombre de la carpeta, puedes cambiarlo

Para activarlo hay que usar el comando:

env\scripts\activate

que es basicamente llamar al archivo activate que se creo del entorno virtuales

Para salir del entorno simplemente usar el comando:

deactivate

--- TIPS:

pip freeze = te muestra los paquetes instalados en el entorno virtual


*******   DICCIONARIOS

planet = {
    'name': 'Earth',
    'moons': 1
}

.get = sirve para acceder a un valor mediante su clave. 'planet.get('name')' o 'planet['name']'
    la diferencia es que get devuelve un none si un valor no esta, y [] regresa un error
.update = sirve para actualizar un valor, planet.update[{'name':'jupiter'}] o 
    planet['name'] = 'Makemake'
    
        # Usando update
    planet.update({
        'name': 'Jupiter',
        'moons': 79
    })

    # Usando corchetes
    planet['name'] = 'Jupiter'
    planet['moons'] = 79
.pop = puede eliminar una clave de un diccionario planet.pop('orbital period')

Se pueden crear nuevas claves de la siguiente manera: planet['orbital period'] = 4333
se pueden guardar diccionarios dentro de diccionarios y se acceden de la siguiente manera
    print(f'{planet['name']} polar diameter: {planet['diameter (km)']['polar']}')
Para acceder a todos los valores de un diccionario puedes usar el metodo 'keys'
    for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
Para acceder todos los valores de un diccionario sin las claves se puede usar 'value'
    for value in rainfall.values():
        total_rainfall = total_rainfall + value


*******   FUNCIONES

Para escribir una función se necesita usar la clave def, un nombre, parentesis y el cuerpo.
    def rocket_parts():
        print("partes")

Si quieres que devuelva un valor agregar return
def rocket_parts():
    return 'payload, propellant, structure'

Para requerir un argumento es necesario agregar la varibale ne los parentesis











"""


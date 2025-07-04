# La regla del polimorfismo es cuando agregas un metodo a la clase 
# hija y al momento de imprimir tomará en cuenta lo hecho en la clase 
# hija más no en la clase padre.


class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hago Guauuu!")

class Pez(Animales):
    def hablar(self):
        print("Yo no hago nada")

aniamal = Animales("Hola")
perro = Perro("Holaaaa")
perro.hablar()      # Acá no sale el mensaje Hola de la clase Animal por que se esta cumpliendo la norma del polimorfismo
pez = Pez("Nada")
pez.hablar()        # Acá no sale el mensaje Hola de la clase Animal por que se esta cumpliendo la norma del polimorfismo
aniamal.hablar()    # Aca no pasa nada ya que estamos llamando a la clase padre.



# Realizar un programa que conste de una clase llamada Alumno que 
# tenga como atributos el nombre y la nota del alumno. Definir los 
# métodos para inicializar sus atributos, imprimirlos y mostrar un 
# mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def nota(self):
        if self._nota >= 11:
            print("La nota del alumno es:{}. Alumno Aprobado".format(self._nota))
        else:
            print("La nota del alumno es:{}. Alumno Desaprobrado".format(self._nota))
        return self._nota

    
alumno = Alumno("Geanfranco",10)
alumno.nombre
print(alumno.nombre)
alumno.nota

######################################################

class Alumno():
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def nota(self):
        return self._nota
    
    def estadoAlumno(self):
        if self._nota >= 11:
            print("Alumno Aprobado")
        else:
            print("Alumno Desaprobrado")



    
alumno = Alumno("Geanfranco",10)
alumno.nombre
print(alumno.nombre)
alumno.nota
print(alumno.nota)
alumno.estadoAlumno()

################################################

# Escribir una clase en python que calcule pow(x, n)

# x = es la base

# n = es el exponente

from math import pow        # Importar siempre fuera de la clase
class Exponente():
    def __init__(self, x, n):
        self._x = x
        self._n = n

    def resultado(self):
        return pow(self._x,self._n)
        # print("El resultado de {} elevado a {} es: {}".format(self._x, self._n, pow(self._x,self._n)))

expo = Exponente(10, 2)
expo.resultado()
print(expo.resultado())
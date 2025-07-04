# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio;
# luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro.
# Crear metodos que muestren la cantidad de llantas, color y precio de ambos
# transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla
# los atributos de cada uno.

from math import floor

llantas = int(input("Ingrese la cantidad de llantas: "))
color = input("Ingrese el color: ")
precio = float(input("Ingrese el precio del producto: "))


class Fabrica():
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

    @property
    def llantas(self):
        return self._llantas

    @property
    def color(self):
        return self._color

    @property
    def precio(self):
        return self._precio


class Moto(Fabrica):
    # Acá podemos agregar una linea donde nos permita reemplazar self.llantas() = llantas
    def llantas_moto(self):
        if self.llantas >= 2:
            if self.llantas % 2 == 0:
                print(
                    f"Con {self.llantas} llantas puede crear {floor(self.llantas/2)} motos")
            else:
                print(
                    f"Con {self.llantas} llantas puede crear {floor(self.llantas/2)} motos y sobraría {self.llantas % 2} llanta.")
        else:
            print(
                f"No se puede fabricar una moto, no hay suficientes llantas. N° de llantas:{self.llantas}")

    def colormoto(self):
        print(f"Las motos serán de color {self.color}")
        return self.color

    def preciomoto(self):
        print(f"El precio de cada moto es de S/{self.precio}")
        return self.precio


class Carro(Fabrica):
    def llantas_carro(self):
        llantasc = self.llantas
        if llantasc >= 4:
            if llantasc % 4 == 0:
                print(
                    f"Con {llantasc} llantas puede fabricar {llantasc/4} carros")
            else:
                print(
                    f"Con {llantasc} llantas puede fabricar {floor(llantasc/4)} carros y sobraria {llantasc % 4} llantas")
        else:
            print(
                f"No se puede fabricar un carro, no hay suficientes llantas. N° de llantas: {llantasc}")

    def colorauto(self):
        print(f"Los carros serán de color {self.color}")
        return self.color

    def precioauto(self):
        print(f"Los carros tendran un precio de S/{self.precio} por unidad")
        return self.precio


# fabricar = Fabrica(llantas, color, precio)
fabricarmoto = Moto(llantas, color, precio)
fabricarmoto.llantas_moto()
fabricarmoto.colormoto()
fabricarmoto.preciomoto()
fabricarcarro = Carro(llantas, color, precio)
fabricarcarro.llantas_carro()
fabricarcarro.colorauto()
fabricarcarro.precioauto()

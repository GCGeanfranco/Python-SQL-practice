# Crear una clase llamada Marino(), con un metodo que sea hablar, en donde
# muestre un mensaje que diga "Hola...". Luego, crear una clase Pulpo() que
# herede Marino, pero modificar el mensaje de hablar por "Soy un Pulpo". Por
# ultimo, crear una clase Foca(), heredada de Marino, pero que tenga un atributo
# nuevo llamado mensaje y que muestre ese mesjae como parametro

class Marino():
    def mensaje(self):              # Metodo
        return "Hola soy un animal Marino."

        # Cuando queremos utilizar herencia debemos llamar igual el nombre de la definicion en este caso "mensaje"


class Pulpo(Marino):                # Metodo
    def mensaje(self):
        return "Hola soy un pulpo."


class Foca(Marino):
    def __init__(self, mensaje):        # Atributo
        self._mensaje = mensaje

    @property
    # Get para poder llamar al atributo correctamente.
    def mensaje(self):
        return self._mensaje


print(marino.mensaje())
pulpo = Pulpo()
print(pulpo.mensaje())
foca = Foca("Hola soy una foquita.")
print(foca.mensaje)

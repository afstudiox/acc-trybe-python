'''
Cria uma classe Car e, depois, atribua valores 
aos atributos brand, model, year e color.
'''


class Car():
    def __init__(self, brand: str, model: str, year: int, color: str):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def identify(self) -> None:
        output = f"Meu carro é um {self.model}, da {self.brand}."
        output += f"Ele é do ano {self.year} e tem a cor {self.color}."
        print(output)


mustang = Car("Ford", "Mustang", 1969, "Vermelho")
mustang.identify()

fusca = Car("Volkswagen", "Fusca", 1970, "Azul")
fusca.identify()

vectra = Car("Chevrolet", "Vectra", 2000, "Prata")
vectra.identify()

"""
Exercício 9
Crie as classes Motorcycle e Truck e inicialize
as duas com o atributo max_speed.
"""


class Motorcycle:
    def __init__(self, max_speed):
        self.max_speed = max_speed


class Truck:
    def __init__(self, max_speed):
        self.max_speed = max_speed


harley = Motorcycle("200 Km/h")
cg150 = Motorcycle("150 Km/h")
yamaha = Motorcycle("180 Km/h")
volvo = Truck("180 Km/h")

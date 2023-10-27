"""
Exercício 10
Utilize as classes criadas no exercício anterior para criar
uma função print_max_speed que recebe um objeto e imprime a
velocidade máxima dele. Retorne uma mensagem de erro com um
TypeError caso o veículo passado como argumento não seja uma
motocicleta.
"""
from exercicio9 import Motorcycle, Truck, harley, cg150, yamaha, volvo


def print_max_speed(vehicle: Motorcycle) -> None:
    if isinstance(vehicle, Motorcycle):
        print(f"A velocidade máxima do veículo é {vehicle.max_speed}")
    else:
        raise TypeError("O veículo precisa ser uma motocicleta")


print_max_speed(harley)
print_max_speed(cg150)
print_max_speed(yamaha)
# print_max_speed(volvo)

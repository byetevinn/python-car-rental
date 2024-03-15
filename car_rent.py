import os


cars = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai HB20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130),
]
rented = []


def show_list_cars(list_of_cars):
    for i, car in enumerate(list_of_cars):
        print("[{}] {} - R$ {} /dia.".format(i, car[0], car[1]))


while True:
    os.system("clear")
    print("=================================")
    print("Bem vindo à locadora de carros!")
    print("=================================")

    print("")

    print("O que você deseja fazer?")
    print("0 - Mostrar Portifólio | 1 - Alugar um Carro | 3 - Devolver um Carro")
    op = int(input())

    os.system("clear")
    if op == 0:
        show_list_cars(cars)

    elif op == 1:
        show_list_cars(cars)
        print("=================================")
        print("Escolha o código do carro:")

        car_code = int(input())

        print("Por quantos dias você deseja alugar esse carro?")
        days = int(input())

        os.system("clear")

        print("Você escolheu o {} por {} dias.".format(cars[car_code][0], days))
        print(
            "O valor total do aluguel é de R$ {}. Deseja alugar?".format(
                days * cars[car_code][1]
            )
        )

        print("0 - SIM | 1 - NÃO")
        conf = int(input())

        if conf == 0:
            print(
                "Parabéns você alugou o {} por {} dias.".format(cars[car_code][0], days)
            )
            rented.append(cars.pop(car_code))

    elif op == 2:
        if len(rented) == 0:
            print("Não há carros para devolver.")

        else:
            print("Lista de carros alugados. Qual você deseja devolver?")
            show_list_cars(rented)
            print("")
            print("Escolha o código do carro que deseja devolver:")

            car_code = int(input())

            if conf == 0:
                print("Obrigado por devolver o carro {}.".format(cars[car_code][0]))
                cars.append(rented.pop(car_code))

    print("=================================")
    print("0 para CONTINUAR | 1 para SAIR")

    if int(input()) == 1:
        break

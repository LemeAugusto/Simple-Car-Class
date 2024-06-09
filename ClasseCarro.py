class Carro:
    def __init__(self, cor, modelo, cv, ano):
        self.cor = cor
        self.modelo = modelo
        self.cv = cv
        self.ano = ano

    def ligarcarro(self):
        print(f'\033[0:32mLigando {self.modelo} {self.ano}\033[m')

HondaCivic = Carro('cinza','Honda Civic','158','2023')
ToyotaCorolla = Carro('branco','Toyota Corolla','140','2022')
FordMustang = Carro('vermelho','Ford Mustang','460','2023')
VolkswagenGol = Carro('azul','Volkswagen Gol','85','2020')
BMWx5 = Carro('preto','BMW X5','335','2024')
class Human:
    # статические поля

    def_name = 'No name'
    def_age = 0

    def __init__(self, name=def_name, age=def_age):
        # Динамические поля
        # Публичные
        self.name = name
        self.age = age
        # Приватные
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name {self.name}')
        print(f'Age {self.age}')
        print(f'Money {self.__money}')
        print(f'House {self.__house}')

    # статический метод

    @staticmethod
    def def_info():
        print(f'Def Name {Human.def_name}')
        print(f'Def Age {Human.def_age}')

    def earn_money(self, ammount):
        self.__money +=ammount
        print( f'Заработал {ammount}! теперь у меня {self.__money} денег!')

    # Приватный метод
    def __make_deal(self, house, price):
        self.__money -=price
        self.__house = house

    def buy_house(self, house, discont):
        pass


class House:

    def __init__(self, area, price:int):
        self.area = area
        self.price = price

    def final_price(self, discont):
        final_price = self.price*(100-discont)/100
        print(f' Final price{final_price}')
        return final_price


fedor = Human('Fedor',32)
fedor.info()
Human.def_info()

fedor.earn_money(10_000)
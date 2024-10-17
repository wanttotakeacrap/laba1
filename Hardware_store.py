class Hardware_store():

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __getitem__(self, item): #объект класса становится подписным(как будто словарь)
        pass

    def make_dict(self):
        return {
            "name": self.name,
            "price": self.price,
        }


class TV(Hardware_store):

    def __init__(self, name: str, price: float, resolution: str):
        super().__init__(name, price)
        self.resolution = resolution

    def __getitem__(self, item):
        return getattr(self, item)


    def make_dict(self):
        tv_dict = super().make_dict()
        tv_dict["resolution"] = self.resolution
        return tv_dict


class Laptop(Hardware_store):

    def __init__(self, name: str, price: float, weight: float):
        super().__init__(name, price)
        self.weight = weight

    def __getitem__(self, item):
        return getattr(self, item)

    def make_dict(self):
        laptop_dict = super().make_dict()
        laptop_dict["weight"] = self.weight
        return laptop_dict


class Phone(Hardware_store):

    def __init__(self, name: str, price: float, memory: int):
        super().__init__(name, price)
        self.memory = memory

    def __getitem__(self, item):
        return getattr(self, item)

    def make_dict(self):
        phone_dict = super().make_dict()
        phone_dict["memory"] = self.memory
        return phone_dict


class Charger(Hardware_store):

    def __init__(self, name: str, price: float, power: int):
        super().__init__(name, price)
        self.power = power

    def __getitem__(self, item):
        return getattr(self, item)

    def make_dict(self):
        charger_dict = super().make_dict()
        charger_dict["power"] = self.power
        return charger_dict


class Earphone(Hardware_store):

    def __init__(self, name: str, price: float, frequency: int):
        super().__init__(name, price)
        self.frequency = frequency

    def __getitem__(self, item):
        return getattr(self, item)

    def make_dict(self):
        earphone_dict = super().make_dict()
        earphone_dict["frequency"] = self.frequency
        return earphone_dict


class Computer(Hardware_store):

    def __init__(self, name: str, price: float, cpu: str):
        super().__init__(name, price)
        self.cpu = cpu

    def __getitem__(self, item):
        return getattr(self, item)

    def make_dict(self):
        computer_dict = super().make_dict()
        computer_dict["cpu"] = self.cpu
        return computer_dict

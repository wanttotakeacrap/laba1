import json


class Json1:

    @staticmethod
    def safe_json(data, filename: str):
        try:
            with open(filename, "w", encoding="utf-8") as json_file:  # сохранение в файл
                json.dump(data, json_file, indent=4, ensure_ascii=False, default=lambda o: o.__dict__)
            print("Saved file: " + filename)
        except IOError as e:  # обработка ошибки при открытии фойла
            print("error when starting json file: " + str(e))

    @staticmethod
    def load_json(filename):
        try:
            with open(filename, "r", encoding="utf-8") as js:  # чтение из json
                result = json.load(js)
                return result
        except (FileNotFoundError, json.decoder.JSONDecodeError):  # если файла нет или
            # он пуст заполняем его пустым словарем
            return {"tv": [], "laptop": [], "phone": [], "charger": [],
                    "earphone": [], "computer": []}

    # добавляем инфу в словарь
    @staticmethod
    def add_tv(data, tv):
        data["tv"].append(tv)

    @staticmethod
    def add_laptop(data, laptop):
        data["laptop"].append(laptop)

    @staticmethod
    def add_phone(data, phone):
        data["phone"].append(phone)

    @staticmethod
    def add_charger(data, charger):
        data["charger"].append(charger)

    @staticmethod
    def add_earphone(data, earphone):
        data["earphone"].append(earphone)

    @staticmethod
    def add_computer(data, computer):
        data["computer"].append(computer)
from Hardware_store import TV, Laptop, Phone, Charger, Earphone, Computer
from json1 import Json1

def get_positive_num(messege: str) -> int:
    while True:
        try:
            price = int(input(messege))
            if price <= 0:
                raise ValueError
            return price
        except ValueError:
            print("Please enter right value")

def print_data(data):
    print("\nData from JSON")

    print("\nTV")
    for tv in data["tv"]:
        print(f"Name: {tv['name']}, Price: {tv['price']}, Resolution: {tv['resolution']}")

    print("\nLaptop")
    for laptop in data["laptop"]:
        print(f"Name: {laptop['name']}, Price: {laptop['price']}, Weight: {laptop['weight']}")

    print("\nPhone")
    for phone in data["phone"]:
        print(f"Name: {phone['name']}, Price: {phone['price']}, Memory: {phone['memory']}")

    print("\nCharger")
    for charger in data["charger"]:
        print(f"Name: {charger['name']}, Price: {charger['price']}, Power: {charger['power']}")

    print("\nEarphone")
    for earphone in data["earphone"]:
        print(f"Name: {earphone['name']}, Price: {earphone['price']}, Frequency: {earphone['frequency']}")


    print("\nComputer")
    for computer in data["computer"]:
        print(f"Name: {computer['name']}, Price: {computer['price']}, CPU: {computer['cpu']}\n")


def main():
    data = Json1.load_json("result.json")

    while True:
        print("choose operation \n"
              "1. print data from JSON\n"
              "2. add TV\n"
              "3. add laptop\n"
              "4. add phone\n"
              "5. add charger\n"
              "6. add earphone\n"
              "7. add computer\n"
              "8. save to JSON\n"
              "9. exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print_data(data)

        elif choice == 2:
            name = input("Enter name of TV: ")
            price = get_positive_num("Enter price of TV: ")
            resolution = input("Enter resolution of TV: ")
            tv = TV(name, price, resolution)
            Json1.add_tv(data, tv)

        elif choice == 3:
            name = input("Enter name of laptop: ")
            price = get_positive_num("Enter price of laptop: ")
            weight = get_positive_num("Enter weight of laptop: ")
            laptop = Laptop(name, price, weight)
            Json1.add_laptop(data, laptop)

        elif choice == 4:
            name = input("Enter name of phone: ")
            price = get_positive_num("Enter price of phone: ")
            memory = get_positive_num("Enter memory of phone: ")
            phone = Phone(name, price, memory)
            Json1.add_phone(data, phone)

        elif choice == 5:
            name = input("Enter name of charger: ")
            price = get_positive_num("Enter price of charger: ")
            power = input("Enter power of charger: ")
            charger = Charger(name, price, power)
            Json1.add_charger(data, charger)

        elif choice == 6:
            name = input("Enter name of earphone: ")
            price = get_positive_num("Enter price of earphone: ")
            frequency = get_positive_num("Enter frequency of earphone: ")
            earphone = Earphone(name, price, frequency)
            Json1.add_earphone(data, earphone)

        elif choice == 7:
            name = input("Enter name of computer: ")
            price = get_positive_num("Enter price of computer: ")
            cpu = input("Enter CPU of computer: ")
            computer = Computer(name, price, cpu)
            Json1.add_computer(data, computer)

        elif choice == 8:
            Json1.safe_json(data, "result.json")

        elif choice == 9:
            print("End of program")
            break

        else:
            print("Enter correct choice")


if __name__ == "__main__":
    main()
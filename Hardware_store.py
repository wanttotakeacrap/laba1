from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET

class Hardware_store(ABC):

    def __init__(self, name, price):
        self.name = input("Enter name: ")
        self.price = input("Enter price: ")

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def to_json(self, filename):
        pass

    @abstractmethod
    def to_xml(self, filename):
        pass

class TV(Hardware_store):

    def __init__(self, name, price):
        self.name = input("Enter name: ")
        while True:
            try:
                self.price = float(input("Enter price: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Error, enter other number: ")


class laptop(Hardware_store):

    def __init__(self, name, price):
        self.name = input("Enter name: ")
        while True:
            try:
                self.price = float(input("Enter price: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Error, enter other number: ")


class phone(Hardware_store):

    def __init__(self, name, price):
        self.name = input("Enter name: ")
        while True:
            try:
                self.price = float(input("Enter price: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Error, enter other number: ")


class macbook(Hardware_store):

    def __init__(self, name, price):
        self.name = input("Enter name: ")
        while True:
            try:
                self.price = float(input("Enter price: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Error, enter other number: ")


class charger(Hardware_store):

    def __init__(self, name, price):
        self.name = input("Enter name: ")
        while True:
            try:
                self.price = float(input("Enter price: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Error, enter other number: ")


class earphone(Hardware_store):

    def __init__(self, name, price):
        self.name = input("Enter name: ")
        while True:
            try:
                self.price = float(input("Enter price: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Error, enter other number: ")


class lamp(Hardware_store):

    def __init__(self, name, price):
        self.name = input("Enter name: ")
        while True:
            try:
                self.price = float(input("Enter price: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Error, enter other number: ")


class mouse(Hardware_store):

    def __init__(self, name, price):
        self.name = input("Enter name: ")
        while True:
            try:
                self.price = float(input("Enter price: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Error, enter other number: ")


class keyboard(Hardware_store):

    def __init__(self, name, price):
        self.name = input("Enter name: ")
        while True:
            try:
                self.price = float(input("Enter price: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Error, enter other number: ")


class computer(Hardware_store):

    def __init__(self, name, price):
        self.name = input("Enter name: ")
        while True:
            try:
                self.price = float(input("Enter price: "))
                if self.price <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Error, enter other number:")

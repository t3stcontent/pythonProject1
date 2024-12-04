class Person:
    def __init__(self, name = "None", age = 0):
        self.name = name
        self.age = age
        self.lang = []
        self.weight = 0
        self.satiety = 10
        self.isAlive = True
        self.address = ""

        print("Створення об'єкта класу")

    def say_Hello(self, user_name = ""):
        print(f"Hello {user_name}, my name is {self.name}")

    def show_info(self, fullInfo = False):
        if fullInfo:
            print(f"Name = {self.name}\tAge = {self.age}")
        else:
            print(f"Name: {self.name}")

    def enter_data(self):
        self.name = input("ВВедіть нове ім'я ")
        self.age = int(input("ВВедіть вік "))

    def __del__(self):
        print(f"Наш клас {self.name} знищено")

tom = Person("Tom", 25)
bob = Person("Bob", 22)
sam = Person("Sam", 33)
alice = Person()

tom.lang.extend(["eu", "ua", "fra"])
print(tom.lang)

tom.say_Hello("Kate")
sam.say_Hello("Kate")
bob.say_Hello()

tom.show_info(True)
bob.show_info()
sam.show_info()
alice.show_info()

tom.enter_data()
tom.show_info(True)
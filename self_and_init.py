class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def describe(self):
        print(f"{self.color} {self.brand}")


car1 = Car("Toyota", "red")
car2 = Car("BMW", "blue")

car1.describe()
car2.describe()

print(car1.brand)
print(car1.color)

print(car2.brand)
print(car2.color)


if __name__ == "__main__":
    print("Program finished.")
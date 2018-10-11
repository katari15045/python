class Car:
    name="Baleno"
    # All non-static methods in a class should have self as first argument
    def turn_left(self):
        print("Turning Left")

car = Car()
print(car.name)
car.turn_left()

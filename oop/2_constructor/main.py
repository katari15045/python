class Planet:
    # All methods in a class should have self as first parametre
    def __init__(self, name):
        self.name = name
    def rotate(self):
        print(self.name + " starts rotating!")

planet = Planet("Earth")
planet.rotate()

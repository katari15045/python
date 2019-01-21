class Main:

	@staticmethod
	def sort_key(car):
		return car.capacity

	@staticmethod
	def print_cars(cars):
		for car in cars:
			print(car)

	@staticmethod
	def main():
		car_1 = Car(33, 4)
		car_2 = Car(43, 2)
		car_3 = Car(23, 3)
		cars = [car_1, car_2, car_3]
		print("Before Sorting: ")
		Main.print_cars(cars)
		#sort(cars, key=sort_key, reverse=True) # inplace sorting
		cars = sorted(cars, key=Main.sort_key, reverse=True) # not inplace
		print("After sorting: ")
		Main.print_cars(cars)

class Car:

	def __init__(self, id_, capacity):
		self.id_ = id_
		self.capacity = capacity

	def __str__(self):
		return str(self.id_) + ", " + str(self.capacity)

Main.main()
class Instructor:
	"Assistant professor at IIITD"
	data = None

	def shout(self):
		print("Shouting...")

instructor_1 = Instructor()
instructor_1.data = 3
print(instructor_1.data)

instructor_2 = Instructor()
instructor_2.data = "sak"
print(instructor_2.data)

instructor_3 = Instructor()
instructor_3.data = [2, 3]
print( instructor_3.data )
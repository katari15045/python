import numpy

class Instructor:
	"Assistant professor at IIITD"
	name = "pk"
	age = 37

	def shout(self):
		print("Shouting...")


faculty = numpy.empty( (3, ), dtype=object )

faculty[0] = Instructor()
faculty[1] = Instructor()
faculty[2] = Instructor()

print( faculty[0].__doc__ )
print( faculty[1].__doc__ )
print( faculty[2].__doc__ )
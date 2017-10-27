import numpy
import Instructor

faculty = numpy.empty( (3, ), dtype=object )

faculty[0] = Instructor.Instructor()
faculty[1] = Instructor.Instructor()
faculty[2] = Instructor.Instructor()

faculty[0].shout()
faculty[1].shout()
faculty[2].shout()
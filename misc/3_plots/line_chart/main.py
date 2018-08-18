from matplotlib import pyplot

year = [2012, 2013, 2014, 2015, 2016, 2017, 2018]
rupee_value = [55, 57, 59, 64, 67, 65, 68]

pyplot.plot(year, rupee_value)
pyplot.xlabel("Year")
pyplot.ylabel("1 USD in INR")
pyplot.title("INR vS USD")
pyplot.show()

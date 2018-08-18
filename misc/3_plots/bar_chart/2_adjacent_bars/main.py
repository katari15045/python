from matplotlib import pyplot
import numpy

india_gdp = [0.47, 0.83, 1.68, 2.11]
uk_gdp = [1.64, 2.51, 2.43, 2.86]

figure, axes = pyplot.subplots()
index = numpy.arange(len(india_gdp))
width = 0.33

axes.bar(index, india_gdp, width, label="India")
axes.bar(index+width, uk_gdp, width, label="UK")
pyplot.xticks(index+width/2, [2000, 2005, 2010, 2015])

pyplot.ylabel("GDP in Trillion USD")
pyplot.xlabel("Years")
pyplot.title("GDP of India vs UK")
pyplot.legend(loc="best")
pyplot.show()




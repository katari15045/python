from matplotlib import pyplot

india_population = [0.87, 0.96, 1.05, 1.14, 1.22]
index = list(range(len(india_population)))
width = 0.60

pyplot.bar(index, india_population, width)
pyplot.xticks(index, [1990, 1995, 2000, 2005, 2010])
pyplot.xlabel("Year")
pyplot.ylabel("Population in Billions")
pyplot.title("Population of India")
pyplot.show()

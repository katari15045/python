from matplotlib import pyplot

year = [2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018]
nifty = [1756, 1160, 1848, 2983, 6200, 5245, 4747, 6171, 7211, 10559]
sensex = [5414, 3377, 5696, 9743, 20827, 16191, 15849, 21064, 24455, 34154]

pyplot.plot(year, nifty, label="Nifty")
pyplot.plot(year, sensex, label="Sensex")
pyplot.xlabel("Year")
pyplot.ylabel("Points")
pyplot.title("Sensex vs Nifty")
pyplot.legend(loc="best")
pyplot.show()

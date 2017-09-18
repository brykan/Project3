#CECS 545 
#Project # 3 
#Bryan Evans
#Due 9/19/2017


import re
import itertools
import time

cityRaw = []
cityCoords = []
data = []
def memoize(f):
    """ Memoization decorator for functions taking one or more arguments.  """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

def getData(tspName):	
	#Opens the file and shows the data as a list cleared of spaces and newline characters
	with open(tspName) as f:
		full = f.read().splitlines()
		refined = [x.lstrip() for x in full if x != ""]	
	return refined
def getDimension(refinedList):
		nonNumeric = re.compile(r'[^\d]+')
		for item in refinedList:
			if item.startswith("DIMENSION"):
				return nonNumeric.sub("",item)	
def getCityRaw(dimension,refinedList):
	for item in refinedList:
		for num in range(1,dimension+1):
			if item.startswith(str(num)):
				index,space,rest = item.partition(' ')
				if rest not in cityRaw:
					cityRaw.append(rest)
	return cityRaw
def getCityCoords(cityRaw):
	for item in cityRaw:
		firstCoord, space, secondCoord = item.partition(' ')
		cityCoords.append((firstCoord.strip(), secondCoord.strip()))
	return cityCoords
@memoize
def getDistance(p1,p2):
	#distance formula between 2 points
	xCoord1 = float(p1[0])
	xCoord2 = float(p2[0])
	yCoord1 = float(p1[1])
	yCoord2 = float(p2[1])
	distance = (((xCoord2 - xCoord1)**2) + ((yCoord2 - yCoord1)**2))**.5
	return float(distance)
def initTour(cityPool, cities):
	pairs = list(map(list, itertools.combinations(cityPool,2)))
	costs = []
	for p1,p2 in pairs :
		 costs.append(getDistance(cities[p1-1],cities[p2-1]))
	minDist = min(costs)
	minPath = pairs[costs.index(minDist)]
	return minPath, minDist
def addPoint():
	print x
def main(fileName):
	startTime = time.time()
	data = getData(fileName)
	dimension = int(getDimension(data))
	cityNumbers = [x for x in range (1, dimension+1)]
	print cityNumbers
	cityRaw = getCityRaw(dimension,data)
	cityCoords = getCityCoords(cityRaw)
	tour,cost= initTour(cityNumbers, cityCoords)
	x,y = tour
	cityNumbers.remove(x)
	cityNumbers.remove(y)
	tour.append(tour[0])
	cost+=cost
	print tour, cost
	print("--- %s seconds ---" % (time.time() - startTime))

if __name__ == '__main__':
    main('Random30.tsp')

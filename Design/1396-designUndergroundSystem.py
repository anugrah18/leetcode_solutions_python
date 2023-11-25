class UndergroundSystem:

    def __init__(self):
        self.check_in_data = {}
        self.journey_data = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_in_data.pop(id)
        if (start_station, stationName) not in self.journey_data:
            self.journey_data[(start_station, stationName)] = []
        self.journey_data[(start_station, stationName)].append(t - start_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        listOfTimes = self.journey_data[(startStation, endStation)]
        return sum(listOfTimes) / len(listOfTimes)


X = UndergroundSystem()
print(X.checkIn(45, "Leyton", 3))
print(X.checkIn(32, "Paradise", 8))
print(X.checkIn(27, "Leyton", 10))
print(X.checkOut(45, "Waterloo", 15))
print(X.checkOut(27, "Waterloo", 20))
print(X.checkOut(32, "Cambridge", 22))
print(X.getAverageTime("Paradise", "Cambridge"))
print(X.getAverageTime("Leyton", "Waterloo"))
print(X.checkIn(10, "Leyton", 24))
print(X.getAverageTime("Leyton", "Waterloo"))
print(X.checkOut(10, "Waterloo", 38))
print(X.getAverageTime("Leyton", "Waterloo"))


# Time Complexity : O(1) for all operations
# Space Complexity: O(P+S^2) , pair of stations getting stored in journey_data

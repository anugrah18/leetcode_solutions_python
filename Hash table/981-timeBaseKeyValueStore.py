class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []

        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.dict:
            return ""

        VALUES = self.dict[key]

        for i in range(len(VALUES) - 1, -1, -1):
            if VALUES[i][0] <= timestamp:
                return VALUES[i][1]

        return ""


obj = TimeMap()
print(obj.set("foo","bar",1),obj.get("foo",1),obj.get("foo",3),obj.set("foo","bar2",4),obj.get("foo",4),obj.get("foo",5))

# Time Complexity : set() - O(L) , get() - O(T) , t= timestamps
# Space Complexity : O(L)

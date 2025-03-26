class TimeMap:

    def __init__(self):
        # Dictionary to store key -> list of (timestamp, value) pairs
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If key is new, initialize with an empty list
        if key not in self.dict:
            self.dict[key] = []

        # Append the (timestamp, value) pair in chronological order
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # If key not found, return empty string
        if key not in self.dict:
            return ""

        # Get the list of (timestamp, value) pairs for the key
        VALUES = self.dict[key]

        # Search from the end of the list to find the latest timestamp <= given timestamp
        for i in range(len(VALUES) - 1, -1, -1):
            if VALUES[i][0] <= timestamp:
                return VALUES[i][1]

        # If no such timestamp is found, return empty string
        return ""


obj = TimeMap()
print(obj.set("foo","bar",1),obj.get("foo",1),obj.get("foo",3),obj.set("foo","bar2",4),obj.get("foo",4),obj.get("foo",5))

# Time Complexity : set() - O(1) , get() - O(n) , n = number of entries
# Space Complexity : O(n)

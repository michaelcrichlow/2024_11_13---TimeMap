class TimeMap:

    def __init__(self):
        self.dict = dict()
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.dict.get(key, [])

        # fundamental binary search
        first, last = 0, len(values) - 1

        while first <= last:
            mid = first + (last - first) // 2

            if values[mid][1] == timestamp:
                res = values[mid][0]
                return res

            elif values[mid][1] < timestamp:
                res = values[mid][0]
                first = mid + 1
            
            elif values[mid][1] > timestamp:
                last = mid - 1

        return res

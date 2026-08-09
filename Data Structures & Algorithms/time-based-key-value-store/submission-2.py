class TimeMap:

    def __init__(self):
        # Initialize a hashmap
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if the key doesn't exist already,
        # create an empty list for that key
        if key not in self.key_store:
            self.key_store[key] = []

        # append values for that key
        self.key_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.key_store.get(key, [])
        l, r = 0, len(values) - 1

        while l <= r:
            m = (l + r) // 2

            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res

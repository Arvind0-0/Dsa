class TimeMap:

    def __init__(self):
        self.dictionary = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
		# Accessing the list associated with the key.
        data = self.dictionary[key]
        for val,time in reversed(data):
            if time <= timestamp:
                return val
        return ""
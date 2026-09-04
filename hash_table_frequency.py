class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)

        bucket = self.table[index]

        for pair in bucket:

            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])

    def get(self, key):
        index = self._hash(key)

        bucket = self.table[index]

        for pair in bucket:

            if pair[0] == key:
                return pair[1]

        return None

    def contains(self, key):
        return self.get(key) is not None


def count_word_frequency(text):

    table = HashTable()

    words = text.lower().split()

    for word in words:

        current_count = table.get(word)

        if current_count is None:
            table.put(word, 1)
        else:
            table.put(word, current_count + 1)

    return table


if __name__ == "__main__":

    text = """
    cloud systems need reliable systems
    reliable systems need monitoring
    monitoring improves cloud systems
    """

    frequency_table = count_word_frequency(text)

    words = [
        "cloud",
        "systems",
        "reliable",
        "monitoring",
        "security"
    ]

    for word in words:
        print(
            f"{word}:",
            frequency_table.get(word)
        )
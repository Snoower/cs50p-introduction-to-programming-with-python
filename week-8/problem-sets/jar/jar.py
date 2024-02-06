class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0:
            raise ValueError("Too many cookies")
        self._capacity = int(capacity)
        self._size = 0

    def __str__(self):
        if self.size == 0:
            return ""
        number_of_cookies = int(self.size) * "🍪"
        return f"{number_of_cookies}"

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies")
        self._size += n


    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

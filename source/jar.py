cookie = '🍪'


class Jar:
    def __init__(self, capacity=12):
        if not capacity > 0:
            raise ValueError
        self.cookies = 0
        self.capacity = capacity

    def __str__(self):
        return cookie * self.cookies

    def deposit(self, n):
        self.cookies += n
        if self.cookies > self.capacity:
            raise ValueError
        else:
            return self.cookies

    def withdraw(self, n):
        self.cookies -= n
        if self.cookies < 0:
            raise ValueError
        else:
            return self.cookies

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies

    @capacity.setter
    def capacity(self, value):
        self._capacity = value


def main():
    jar = Jar()
    print(jar)
    print(jar.capacity)
    print(jar.size)
    jar.deposit(3)
    print(jar)
    print(jar.size)


if __name__ == "__main__":
    main()

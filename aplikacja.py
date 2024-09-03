class Film:
    def __init__(self):
        self.liczba_wyp = 0

    def setter(self, tytul):
        self.tytul = tytul

    def getter(self):
        return self.tytul

    def getter_wyp(self):
        return self.liczba_wyp

    def increment(self):
        self.liczba_wyp += 1

film1 = Film()
film1.setter("adassda")
print(film1.getter())
print(film1.getter_wyp())
film1.increment()
print(film1.getter_wyp())

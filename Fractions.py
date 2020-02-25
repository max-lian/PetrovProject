import NskNsd
class Fractions(object):
    def __init__(self, top: int, bottom: int):
        if(bottom == 0):
            raise ZeroDivisionError
        self.top = int(top)
        self.bottom = int(bottom)
        Fractions.simplify(self)

    def __add__(self, otherfraction):
        newBottom = NskNsd.NskNsd.nsk(self.bottom, otherfraction.bottom)
        newTop = self.top*(newBottom//self.bottom) + otherfraction.top*(newBottom//otherfraction.bottom)
        return Fractions(newTop, newBottom)

    def __sub__(self, otherfraction):
        newBottom = NskNsd.NskNsd.nsk(self.bottom, otherfraction.bottom)
        newTop = self.top * (newBottom // self.bottom) - otherfraction.top * (newBottom // otherfraction.bottom)
        return Fractions(newTop, newBottom)

    def __str__(self):
        if(self.top % self.bottom != 0):
            return str(self.top)+"/"+str(self.bottom)
        return str(self.top//self.bottom)

    def simplify(self):
        nsd = NskNsd.NskNsd.nsd(self.top, self.bottom)
        if(self.bottom < 0): nsd = -nsd
        self.top = self.top//nsd
        self.bottom = self.bottom//nsd
if __name__ == "__main__":
    try:
        a = Fractions(1, 2)
        b = Fractions(4, 8)
        print(a + b)
    except ZeroDivisionError as err:
        print("Убери с знаменателя 0, дебил")

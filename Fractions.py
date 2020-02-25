from NskNsd import NskNsd
class Fractions(object):
    def __init__(self, top: int, bottom: int):
        if(bottom == 0):
            raise ZeroDivisionError
        self.top = top
        self.bottom = bottom
        Fractions.simplify(self)

    def __add__(self, otherfraction):
        newBottom = NskNsd.nsk(self.bottom, otherfraction.bottom)
        newTop = self.top*(newBottom//self.bottom) + otherfraction.top*(newBottom//otherfraction.bottom)
        return Fractions(newTop, newBottom)

    def __sub__(self, otherfraction):
        newBottom = NskNsd.nsk(self.bottom, otherfraction.bottom)
        newTop = self.top * (newBottom // self.bottom) - otherfraction.top * (newBottom // otherfraction.bottom)
        return Fractions(newTop, newBottom)

    def __mul__(self, otherfraction):
        nsd1 = NskNsd.nsd(self.top, otherfraction.bottom)
        nsd2 = NskNsd.nsd(otherfraction.top, self.bottom)
        newTop = (self.top//nsd1)*(otherfraction.top//nsd2)
        newBottom = (otherfraction.bottom // nsd1) * (self.bottom // nsd2)
        return Fractions(newTop, newBottom)

    def __truediv__(self, otherfraction):
        nsd1 = NskNsd.nsd(self.top, otherfraction.top)
        nsd2 = NskNsd.nsd(otherfraction.bottom, self.bottom)
        newTop = (self.top//nsd1)*(otherfraction.bottom//nsd2)
        newBottom = (otherfraction.top // nsd1) * (self.bottom // nsd2)
        return Fractions(newTop, newBottom)

    def __str__(self):
        if(self.top % self.bottom != 0):
            return str(self.top)+"/"+str(self.bottom)
        return str(self.top//self.bottom)

    def simplify(self):
        nsd = NskNsd.nsd(self.top, self.bottom)
        if(self.bottom < 0): nsd = -nsd
        self.top = self.top//nsd
        self.bottom = self.bottom//nsd

if __name__ == "__main__":
    try:
        a = Fractions(1, 3)
        b = Fractions(-2, 9)
        print(a / b)
    except ZeroDivisionError as err:
        print("Убери с знаменателя 0, дебил")

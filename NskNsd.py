class NskNsd:
    def nsk(int1 : int, int2: int):
        int1 = abs(int1)
        int2 = abs(int2)
        m = int1 * int2
        while int1 != 0 and int2 != 0:
            if int1 > int2:
                int1 %= int2
            else:
                int2 %= int1
        return m // (int1 + int2)
    def nsd(int1: int, int2: int):
        int1 = abs(int1)
        int2 = abs(int2)
        while int1 != 0 and int2 != 0:
            if int1 > int2:
                int1 %= int2
            else:
                int2 %= int1
        return int1 + int2

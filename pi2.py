from decimal import *
getcontext().prec = 69

def calcPi(calcTo):
    pi = Decimal(1)
    index = 3
    while index <= calcTo:
        if (index % 2) == 1:
            if ((index + 1) / 2 % 2) == 1:
                pi += (Decimal(1)/Decimal(index))
            else:# ((index + 1) / 2 % 2) == 1:
                pi -= (Decimal(1)/Decimal(index))
        index += 1
    print(pi * (4))

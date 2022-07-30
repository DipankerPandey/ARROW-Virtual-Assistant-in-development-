
def extract_from_text(text):
    l = []

    for t in text.split(' '):

        try:

            l.append(float(t))

        except ValueError:

            pass

    return l


# calculating LCM

def lcm(x, y):
    L = x if x > y else y

    while L <= x * y:

        if L % x == 0 and L % y == 0:
            return L

        L += 1


# calculating HCF

def hcf(x, y):

    H = x
    if x != 1:
        pass
    else:
        if x % H == 0 and y % H == 0:
            return H

    H -= 1


# Addition

def add(x, y):
    return x + y


# Subtraction

def sub(x, y):
    return x - y


# Multiplication

def mul(x, y):
    return x * y


# Division

def div(x, y):
    return x / y


# Remainder

def mod(x, y):
    return x % y

def sub2(x, y):
    return y - x


def calc(text):

    operations = {'ADD': add, 'PLUS': add, 'SUM': add, 'ADDITION': add,

                  'SUB': sub, 'SUBTRACTED': sub, 'MINUS': sub, 'SUBTRACT': sub2,

                  'DIFFERENCE': sub, 'LCM': lcm, 'HCF': hcf,

                  'PRODUCT': mul, 'TIMES': mul, 'MULTIPLY': mul, 'MULTIPLICATION': mul, 'DIVIDED': div,

                  'DIVISION': div, 'MOD': mod, 'REMAINDER': mod, 'MODULAS': mod}

    for word in text.split(' '):

        if word.upper() in operations.keys():


            l = extract_from_text(text)

            r = operations[word.upper()](l[0], l[1])

            return r

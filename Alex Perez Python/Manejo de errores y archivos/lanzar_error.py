class OperadorException(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)



def divir(a, b):
    if b == 0:
        raise OperadorException('La division con cero no esta definida!')
    else:
        return a / b

divir(4, 0)

"""
def divir(a, b):
    if b == 0:
        raise ZeroDivisionError('La division con cero no esta definida!')
    else:
        return a / b
"""
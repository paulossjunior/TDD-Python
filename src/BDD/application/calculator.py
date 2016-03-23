##Exemplo retirado do site http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137

class Calculator(object):

    def add(self, x, y):

        number_types = (int, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

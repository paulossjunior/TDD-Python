##Exemplo retirado do site http://code.tutsplus.com/tutorials/beginning-test-driven-development-in-python--net-30137
##//lhekheklqhlekhqkehqkehqkhelqw
##//ljkfhjdhfjkdhfkjlsdhlfkhslkjkljdflksgflsgdf
##//lkhdsklfskfgshgfsjhgfs

class Calculator(object):
    def add(self, x, y):

        number_types = (int, float, complex)
        if instance(x, number_types) and instance(y, number_types):
            return x + y
        else:
            raise ValueError

    def sub(self, x, y):

        number_types = (int, float, complex)
        if instance(x, number_types) and instance(y, number_types):
            return x + y
        else:
            raise ValueError            
            
    def mult(self, x, y):

        number_types = (int, float, complex)
        if instance(x, number_types) and instance(y, number_types):
            return x + y
        else:
            raise ValueError
            
            
    def div(self, x, y):

        number_types = (int, float, complex)
        if instance(x, number_types) and instance(y, number_types):
            return x + y
        else:
            raise ValueError            

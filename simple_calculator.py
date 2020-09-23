from time import clock

INF = 1e20
eps = 1e-10

class Calculator:
    def __init__(self, init_value=0):
        self.value = init_value


    def add(self, *args):
        self.value += sum(args)
        return self


    def multiply(self, *args):
        for x in args:
            self.value *= x
        return self


    def divide(self, *args, integer_divide=False):
        for x in args:
            if integer_divide:
                self.value //= x
            else:
                self.value /= x
        return self


    def subtract(self, *args):
        self.value -= sum(args)
        return self


    def power(self, deg):
        if(str(deg).isdigit()):
            if (deg == 0):
                self.value = 1
                return self
            if (self.value < 0):
                print('Степень из отрицателнього числа не определёна')
                return self


        base = self.value

        if deg >= 0:
            for cur in range(deg - 1):
                self.value *= base
        else:
            deg = -deg
            for cur in range(deg - 1):
                self.value /= base
        return self


    def root(self, root):
        if (str(root).isdigit()):
            if (root == 0):
                print('Корень 0 степени не существует')
                return self
            if(self.value < 0):
                print('Корень из отрицателнього числа не определён')
                return self


        left, right = 0, 10000000
        while(right - left > eps):
            middle = (left + right)/2
            res_now = 1
            for i in range(root):
                res_now *= middle
            if(res_now < self.value):
                left = middle
            else:
                right = middle
        self.value = left
        return self


    def assign(self, val):
        self.value = val
        return self


    def __repr__(self):
        return self.value


    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    # time_start = clock()
    # print(time_start)
    calculator = Calculator(100)
    print(calculator)
    print(calculator.add(1, 2, 3, 5.1).multiply(4, 0.123).subtract(4, 1, -100).divide(5, integer_divide=True))
    print(Calculator(100).value + 10)
    print(calculator.assign(5).value)
    print(calculator.assign(10).power(15).add(214).root(5).divide(5,21).power(8))


    # time_finish = clock()
    # print(time_finish)
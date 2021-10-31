class Calculator:
    """example simple calculator"""
    i = 12345

    def f(self):
        return 'hello world'


Calculator.i = 1024  # redefine attribut of class

k = Calculator()  # instance object of class Calculator
print(k.i, k.f())

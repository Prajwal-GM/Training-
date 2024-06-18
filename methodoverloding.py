class Calculator:
    def add(self,*args):
        total=0
        for i in args:
            total=total+i
        return total
calculator=Calculator()
print(calculator.add(2,3))
print(calculator.add(2,3,4))
print(calculator.add(2,3,4,5))
print(calculator.add(2,3,4,5,6))
print(calculator.add(2,3,4,5,6,7))
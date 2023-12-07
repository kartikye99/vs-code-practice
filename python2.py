import math
class Operation():
    def __init__(self):
        a = input("how many operation yoy need: ")
    def __fac(self,num):
        self.num=num
        f = math.factorial(num)
        return f
    def check(self,num):
        self.num=num
        sum=0
        for i in num:
            sum = sum+(self.__fac(int(i)))
        if sum == int(num):
            print("yess")
        else:
            print("no")
class Factorial(Operation):
    pass
facto = Factorial()
facto.check(input("enter: "))
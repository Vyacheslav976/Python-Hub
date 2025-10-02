class Calculator:
    def sum(self, a, b):
        result = a + b
        return result

    def sub(self, a, b):
        result = a - b
        return result

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if (b == 0):
            raise ArithmeticError("На ноль делить нельзя")  #поднять ошибку
        return a / b  #возвращение результата деления

    def pow(self, a, b=2):  #задали значение по умолчанию
        return a ** b

    def avg(self, nums):
            if (len(nums) == 0):
                    return 0

            s = 0
            for num in nums:
                s = s + num

            l = len(nums)
            return self.div(s, l)

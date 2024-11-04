class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        if a <=0 or b <=0:
            return "you can not multiply by ZERO"
        for i in range(a):
            result = self.add(result, b)
        return result

    def divide(self, a, b):
        result = 0
        if a <=0 or b <=0:
            return "you can not devide by ZERO"
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            return "Error"
        while a >= b:
            a = self.subtract(a, b)

        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
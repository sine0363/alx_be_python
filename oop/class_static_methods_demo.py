class Calculator:
    calculation_type = "Arithmetic Operations"
    staticmethod
    def add(a,b):
        return a + b
    
    
    def multiply(self,a,b):
        self.a = a
        self.b =b

    @classmethod
    def multiply (cls,a ,b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


    

class MathDojo(object)
    def __init__(self):
        self.result = 0

    def add(self, num, *restOfNum):

        if type(num) == list or type(num) == tuple:
            for var in num:
                self.result += var
        else:
            self.result += num
        if restOfNum:
            for num in restOfNum:
                if type(num) == list or type(num) == tuple:
                    for var in num:
                        self.result += var
                else:
                    self.result += num
        return self

    def subtract(self, num, *restOfNum):

        if type(num) == list or type(num) == tuple:
            for var in num:
                self.result -= var
        else:
            self.result -= num
        if restOfNum:
            for num in restOfNum:
                if type(num) == list or type(num) == tuple:
                    for var in num:
                        self.result -= var
                else:
                    self.result -= num
        return self

md = MathDojo()
print md.add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result

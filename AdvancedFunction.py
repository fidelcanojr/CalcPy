class AdvancedFunction:

    def __init__(self, type, operations):
        self.type = type
        self.operations = operations

    def __add__(self,other):
        if ((self.type == 'summation') and (other.type == 'summation')):
            return AdvancedFunction('summation',self.operations+other.operations)
        return AdvancedFunction('summation',[self, other])

    def __mul__(self,other):
        if ((self.type == 'multiplication') and (other.type == 'multiplication')):
            return AdvancedFunction('multiplication',self.operations+other.operations)
        return AdvancedFunction('multiplication',[self, other])

    def compose(self,other):
        return AdvancedFunction('composition',[other, self])

    def eval(self, x):
        if self.type == 'summation':
            out = 0
            for f in self.operations:
                out += f.eval(x)
            return out
        elif self.type == 'multiplication':
            out = 1
            for f in self.operations:
                out *= f.eval(x)
            return out
        elif self.type == 'composition':
            tmp = x
            for f in self.operations:
                tmp = f.eval(tmp)
            return tmp

    def diff(self):
        if self.type == 'summation':
            return AdvancedFunction('summation',[f.diff() for f in self.operations])
        elif self.type == 'multiplication':
            summands = []
            for i in range(len(self.operations)):
                f = self.operations[i]
                summand = self.operations[:]
                summand[i] = f.diff()
                summands.append(AdvancedFunction('multiplication',summand))
            return AdvancedFunction('summation',summands)
        elif self.type == 'composition':
            elements = [self.operations[0].diff()]
            for i in range(len(self.operations)-1):
                j = len(self.operations) - i - 1
                f = self.operations[j]
                elements.append(f.diff().compose(AdvancedFunction('composition',self.operations[:j])))
            return AdvancedFunction('multiplication',elements)

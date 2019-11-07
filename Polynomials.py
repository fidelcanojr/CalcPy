from AdvancedFunction import AdvancedFunction

class Polynomial:

    def __init__(self, coefficients):
        self.type = 'polynomial'
        self.coeffs = coefficients
        self.degree = len(coefficients) - 1

    def __add__(self, other):
        if other.type == 'polynomial':
            out = []
            larger = self if self.degree > other.degree else other
            ddegree = abs(self.degree - other.degree)
            for i in range(larger.degree - ddegree + 1):
                out.append(self.coeffs[i] + other.coeffs[i])
            for i in range(larger.degree - ddegree + 1, max(self.degree, other.degree)+1):
                out.append(larger.coeffs[i])
            return Polynomial(out)
        else:
            return AdvancedFunction('summation',[self,other])

    def __mul__(self, other):
        return AdvancedFunction('multiplication',[self,other])

    def compose(self, other):
        return AdvancedFunction('composition', [other, self])

    def eval(self,x):
        out = self.coeffs[0]
        for i in range(1,len(self.coeffs)):
            out += self.coeffs[i]*x**i
        return out

    def diff(self):
        out = self.coeffs[1:]
        for i in range(len(out)):
            out[i] *= (i+1)
        return Polynomial(out)

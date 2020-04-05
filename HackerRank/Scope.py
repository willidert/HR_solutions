class Difference:
    def __init__(self, a):
        self.__elements = a
    
    def computeDifference(self):
        self.__comb__ = []
        for i in range(len(self.__elements)):
            if i != len(self.__elements) - 1:
                j = i+1
                while j < len(self.__elements):
                    self.__comb__.append([self.__elements[i], self.__elements[j]])
                    j += 1
        self.maximumDifference = max([abs(x[0] - x[1]) for x in self.__comb__])


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

import heapq

class SomeN:
    def __init__(self, h, name):
        self.h = h
        self.name = name
    def __eq__(self, other):
        return self.h == other.h
    def __lt__(self, other):
        return self.h < other.h

n1 = SomeN(7, "seven")
somelist = [(n1)]
heapq.heapify(somelist)

n2 = SomeN(5, "shuvo")
n3 = SomeN(6, "nafiur")
heapq.heappush(somelist, (n2))
heapq.heappush(somelist, (n3))
n4 = SomeN(2, "tanqir")
n5 = SomeN(3, "mohsin")
heapq.heappush(somelist, (n4))
heapq.heappush(somelist, (n5))

while somelist:
    n = heapq.heappop(somelist)
    print(f"{n.h} -> {n.name}")
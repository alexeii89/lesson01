class Plate(object):
    limit = 10
    elements = [0]

    def add_el(self, el):
        while el > 0:
            if self.elements[-1] < self.limit:
                self.elements[-1] += 1
                el = el - 1
            else:
                self.elements.append(0)
        print(self.elements)

    def del_el(self, el):
        while el > 0:
            if self.elements[-1] > 0:
                self.elements[-1] -= 1
                el -=1
            else:
                self.elements.pop(-1)
        print(self.elements)


obj = Plate()
obj.add_el(43)
obj.del_el(7)

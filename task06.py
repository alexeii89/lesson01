class QueueClass:
    def __init__(self):
        self.elems = []
        self.correct = []
        self.complite = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.complite.append(self.elems.pop())

    def size_base(self):
        return len(self.elems)

    def in_correct(self):
        return self.correct.append(self.elems.pop())

    def complited(self):
        return len(self.complite)



if __name__ == '__main__':
    qc_obj = QueueClass()
    print(qc_obj.is_empty())  # -> True. Очередь пустая

    # помещаем объекты в очередь
    qc_obj.to_queue('my_obj')
    qc_obj.to_queue(4)
    qc_obj.to_queue(True)

    print(qc_obj.is_empty())  # -> False. Очередь пустая

    print(qc_obj.size_base())  # -> 3

    print(qc_obj.from_queue())  # -> my_obj

    print(qc_obj.size_base())  # -> 2
    print(qc_obj.complite)
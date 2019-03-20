class ReverseIterator:
    def __init__(self, sequence):
        self._seq = sequence
        self._k = 0

    def __next__(self):
        self._k -= 1
        if self._k > -len(self._seq)-1:
            return(self._seq[self._k])
        else:
            raise StopIteration

    def __iter__(self):
        return self


if __name__ == '__main__':
    seq = [0, 1, 2, 3, 4, 5]
    my_reviter = ReverseIterator(seq)
    for i in range(len(seq)):
        print(next(my_reviter))

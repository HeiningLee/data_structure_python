from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(self, item):
        """Return the element at index j of the sequence."""

    def __contains__(self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:
                return True
        return False

    def __eq__(self, other):
        """Return True if every element of the two sequences are equal."""

        if len(self) != len(other):
            raise ValueError('Dimension must agree')
        for j in range(len(self)):
            if self[j] != other[j]:
                return False
        return True

    def index(self, val):
        """Return leftmost index at which val is found (or raise ValueError)"""
        for j in range(len(self)):
            if self[j] == val:
                return j
        raise ValueError('Value not in sequence')

    def count(self, val):
        """Return the number of elements equal to given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k


if __name__ == '__main__':
    my_seq = Sequence

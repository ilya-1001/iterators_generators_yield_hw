class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.index_list = 0
        self.index_lists = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.index_list == len(self.list_of_lists):
            raise StopIteration
        element = self.list_of_lists[self.index_list][self.index_lists]
        self.index_lists += 1
        if self.index_lists == len(self.list_of_lists[self.index_list]):
            self.index_lists = 0
            self.index_list += 1
        return element


def test_1():

    list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
    FlatIterator(list_of_lists_1),
    ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

        assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
 test_1()


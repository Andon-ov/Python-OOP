class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class TestIntegerList(TestCase):
    # init
    def test__data(self):
        test_num = IntegerList()
        result = []
        self.assertEqual(result, test_num._IntegerList__data)

    def test__data_wrong_data(self):
        test_num = IntegerList("asd", "5")
        result = []
        self.assertEqual(result, test_num._IntegerList__data)

    def test__data_correct_data(self):
        test_num = IntegerList(1, 2, 3)
        result = [1, 2, 3]
        self.assertEqual(result, test_num._IntegerList__data)

    # get_data
    def test_get_data(self):
        test_num = IntegerList(1, 2, 3)

        self.assertEqual(test_num.get_data(), test_num._IntegerList__data)

    # add
    def test_raise_value_error_when_add__data(self):
        test_num = IntegerList()

        with self.assertRaises(ValueError) as ex:
            test_num.add("5")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_when_add__data_correct(self):
        test_num = IntegerList()

        test_num.add(5)
        self.assertEqual(5, 5)

    # remove_index
    def test_remove_index_correct(self):
        test_num = IntegerList(1, 2, 3)

        test_num.remove_index(0)
        self.assertEqual([2, 3], test_num._IntegerList__data)

    def test_raise_value_error_when_remove_index(self):
        test_num = IntegerList()

        with self.assertRaises(IndexError) as ex:
            test_num.remove_index(0)
        self.assertEqual("Index is out of range", str(ex.exception))

    # get
    def test_get_index_correct(self):
        test_num = IntegerList(1, 2, 3)
        result = test_num.get(0)
        self.assertEqual(result, 1)

    def test_raise_index_error_when_get_wrong_index(self):
        test_num = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            test_num.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    # insert
    def test_insert_index_correct(self):
        test_num = IntegerList(1, 2, 3)
        test_num.insert(2, 100)
        self.assertEqual([1, 2, 100, 3], test_num._IntegerList__data)

    def test_raise_index_error_when_insert_wrong_index(self):
        test_num = IntegerList(1, 2, 3)

        with self.assertRaises(IndexError) as ex:
            test_num.insert(4, 100)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_raise_value_error_when_insert_wrong_type(self):
        test_num = IntegerList(1, 2, 3)

        with self.assertRaises(ValueError) as ex:
            test_num.insert(2, "2")
        self.assertEqual("Element is not Integer", str(ex.exception))

    # get_biggest
    def test_get_biggest_work_correct(self):
        test_num = IntegerList(0, 1, 2, -3, 100)

        result = test_num.get_biggest()

        self.assertEqual(100, result)

    # get_index
    def test_get_index_work_correct(self):
        test_num = IntegerList(1, 2, 3)
        result = test_num.get_index(2)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    main()

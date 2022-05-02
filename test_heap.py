from unittest import TestCase
from app.heap import Heap


class TestHeap(TestCase):
    def setUp(self):
        self._heap = Heap()

    def test_empty(self):
        self.assertEqual(self._heap.empty(), True)

    def test_not_empty(self):
        self._heap.add(10)
        self.assertEqual(self._heap.empty(), False)

    def test_remove_min_empty_heap(self):
        with self.assertRaises(Exception):
            self._heap.remove_min()

    def test_remove_min(self):
        """ add the numbers 1, 2, 3, 4, expected result: 1  """
        self._heap.add(1)
        self._heap.add(5)
        self._heap.add(10)
        self.assertEqual(self._heap.remove_min(), 1)

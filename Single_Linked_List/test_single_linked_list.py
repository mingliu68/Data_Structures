import unittest
from single_linked_list import ListNode
from single_linked_list import SingleLinkedList

class SingleLinkedListTest(unittest.TestCase):

    # setUp will run before each test, all test will start with a list of single node, with key equals to 1
    def setUp(self):
        self.node = ListNode(1)
        self.sll = SingleLinkedList(self.node)
        self.assertIsNot(self.sll.head, None)
        self.assertEqual(self.sll.head.next, None)
        self.assertIsInstance(self.sll, SingleLinkedList)
        self.assertIsInstance(self.node, ListNode)
        self.assertIs(self.sll.head, self.node)

    # testing removing the last item in list
    def test_remove_from_back(self):
        self.assertEqual(self.sll.popBack().key, 1)
        self.assertEqual(self.sll.max, 0)
        self.assertIsNone(self.sll.head)

        self.sll.pushBack(10)
        self.assertEqual(self.sll.head.key, 10)
        self.assertEqual(self.sll.max, 1)
        self.assertEqual(self.sll.head.next, None)
        self.assertEqual(self.sll.popBack().key, 10)
        self.assertEqual(self.sll.max, 0)

        self.sll.pushBack(25)
        self.assertEqual(self.sll.max, 1)
        self.sll.pushBack(35)
        self.assertEqual(self.sll.max, 2)
        self.assertEqual(self.sll.popBack().key, 35)
        self.assertEqual(self.sll.max, 1)
        self.assertEqual(self.sll.popBack().key, 25)
        self.assertEqual(self.sll.max, 0)
        self.assertIsNone(self.sll.head)
        
    def test_remove_from_front(self):
        self.assertEqual(self.sll.popFront().key, 1)
        self.assertEqual(self.sll.head, None)
        self.assertEqual(self.sll.max, 0)

        self.sll.pushFront(2)
        self.sll.pushFront(3)
        self.assertEqual(self.sll.head.key, 3)
        self.assertEqual(self.sll.head.next.key, 2)
        self.assertEqual(self.sll.max, 2)
        self.assertEqual(self.sll.popFront().key, 3)
        self.assertEqual(self.sll.head.key, 2)
        self.assertEqual(self.sll.max, 1)
        self.assertEqual(self.sll.popFront().key, 2)
        self.assertEqual(self.sll.max, 0)
        self.assertIsNone(self.sll.head)

        self.sll.pushFront(2)
        self.sll.pushFront(1)
        self.sll.pushBack(3)
        self.assertEqual(self.sll.max, 3)
        self.assertEqual(self.sll.head.key, 1)
        self.assertEqual(self.sll.popFront().key, 1)
        self.assertEqual(self.sll.max, 2)
        self.assertEqual(self.sll.popFront().key, 2)
        self.assertEqual(self.sll.max, 1)
        self.assertEqual(self.sll.head.key, 3)
        self.assertEqual(self.sll.max, 1)
        self.assertEqual(self.sll.popFront().key, 3)
        self.assertEqual(self.sll.max, 0)
        self.assertIsNone(self.sll.head)

    def test_add_to_back(self):
        pass

    def test_add_to_front(self):
        pass


    def test_add_before_a_node(self):
        pass


    def test_add_after_a_node(self):
        pass


    def test_remove_a_node(self):
        pass





if __name__ == '__main__':
    unittest.main()
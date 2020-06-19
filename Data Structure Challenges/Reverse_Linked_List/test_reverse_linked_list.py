import unittest, sys
sys.path.insert(0, '/Users/mliu/Documents/CS_Study/Data_Structures/Single_Linked_List')

from reverse_linked_list import reverse_list
from single_linked_list import SingleLinkedList
from single_linked_list import ListNode

class ReverseSingleLinkedListTests(unittest.TestCase):

    def setUp(self):
        self.node = ListNode(1)
        self.sll = SingleLinkedList(self.node)
        self.assertIsNot(self.sll.head, None)
        self.assertEqual(self.sll.head.next, None)

    # testing removing the last item in list
    def test_popBack(self):
        result = self.sll.popBack()
        self.assertEqual(result.key, 1)
        self.assertEqual(self.sll.max, 0)
        self.assertIsNone(self.sll.head)
    
    

if __name__ == '__main__':
    unittest.main()
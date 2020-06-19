import sys
sys.path.insert(0, '/Users/mliu/Documents/CS_Study/Data_Structures/Single_Linked_List')
from single_linked_list import SingleLinkedList
from single_linked_list import ListNode

def reverse_list(list):
    if list.head is None or list.head.next is None:
        return list
    
    current = list.head
    prev = None
    next = current.next

    while current.next is not None:
        current.next = prev
        prev = current 
        current = next
        next = current.next

    current.next = prev
    list.head = current

    return list


def display_list(list):
    if list.head is None:
        print("Empty List")
    else:
        current = list.head
        print("---- Beginning of List ----")
        while current:
            print(current.key, None if current.next is None else current.next.key)
            current = current.next
        print("---- Ending of List ----")


def create_single_linked_list_from_arr(arr):

    new_list = SingleLinkedList()
    for item in arr:
        new_list.pushBack(item)
    display_list(new_list)
    return new_list

        
def run_test():
    new_arr = [1,2,3,4,5,6,7,8,9,10]

    new_list = create_single_linked_list_from_arr(new_arr)
    rev_list = reverse_list(new_list)
    
    display_list(rev_list)

#run_test()
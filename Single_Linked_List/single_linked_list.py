# single linked list with no tail


class ListNode:
    def __init__(self, key, next = None):
        self.key = key
        self.next = next

    def remove(self):
        self.next = None


class SingleLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.max = 0 if head is None else 1


    #pushFront - add to beginning of the list, return  list.max (list length)
    def pushFront(self, key):
        new_node = ListNode(key, self.head)
        self.head = new_node
        self.max += 1
        return self.max


    #topFront - return list.head
    def topFront(self):
        return self.head


    #popFront - remove first node of the list, return the removed node
    def popFront(self):
        # empty list? return null
        if self.head is None:
            return null
        else:
            old_head = self.head
            self.head = old_head.next
            old_head.remove()
            self.max -= 1
            return old_head


    #addAfter - add to the back of a specific node, return list.max (list length)
    def addAfter(self, node, key):
        # check if node exist in list
        if self.findNode(node) is None:
            return None
        new_node = ListNode(key, node.next)
        node.next = new_node
        self.max += 1
        return self.max


    #addBefore - add to the front of a specific node, return list.max (list length)
    def addBefore(self, node, key):
        # if list is empty return None
        # loop thru the list to see if node exist and keep track of the previous node
        # if node exist, create new node, else return None
        # if node is head node, update head node
        # if not head node, add new node before the node, update previous node next 
        # update list.max (length)
        # return list.max
        if self.head is None:
            return None

        prev = None
        current = self.head

        while current is not node and current.next is not None:
            prev = current
            current = current.next
        
        if current is not node:
            return None
        
        new_node = ListNode(key, node)

        if self.head is node:
            self.head = new_node
        else:
            prev.next = new_node
        
        self.max += 1 
        return self.max

    #pushBack - add to the end of the list, return list.max (list length)
    def pushBack(self, key):
        # create new node
        # if list is empty, update head node point to new node
        # else loop thru list to get to the last node, update last node 's next pointing to new node
        # update length (self.max)
        # return self.max
        new_node = ListNode(key, None)
        if self.head is None:
            self.head = new_node
        
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        self.max += 1
        return self.max


    #topBack - return the last node of the list
    def topBack(self):
        if self.head is None:
            return None
        current = self.head
        while current.next is not None:
            current = current.next
        
        return current


    #popBack - remove the last node of the list, return the removed node
    def popBack(self):
        # if list is empty, return None
        # else loop thru list and keep track of previous node
        # if list head is the last node (only one node in list), update head
        # else update previous node's next pointer to None
        # update self.max (length)
        # return the removed node

        if self.head is None:
            return None
        
        current = self.head
        prev = None

        while current.next is not None:
            prev = current
            current = current.next
        
        if self.head is current:
            self.head = None
        else:
            prev.next = None

        self.max -= 1
        return current
            

    #findKey - find the first occurance of the node with matching key, return node if found, None if not
    def findKey(self, key):
        if self.head is None:
            return None

        current = self.head
        while current.key is not key and current.next is not None:
            current = current.next
        
        return current if current.key is key else None


    #findNode - find the specific node, return node if found, None if not
    def findNode(self, node):
        # if it's an empty list, return None
        # else loop thru the list and find the matching node
        # return node if found, else return None

        if self.head is None:
            return None
        current = self.head
        while current is not node and current.next is not None:
            current = current.next
        
        return None if current is not node else current


    #eraseKey - erase the first occurance of the node with matching key, return removed node if it exist, else return null
    def eraseKey(self, key):
        # if head is None, return None
        # if head node's key value is equal to key, update head pointer to node.next, remove node 
        # else loop thru list to find a node with matching key value, while keeping track of the previous node
        # if a matching node is not found, return None
        # else update previous node's next pointer and remove matching node
        # update list.max (length)
        # return removed node
        if self.head is None: 
            return None
        
        if self.head.key is key:
            old_head = self.head
            self.head = old_head.next
            old_head.remove()
            self.max -= 1   
            return old_head
        else:
            current = self.head
            prev = None
            while current.key is not key and current.next is not None:
                prev = current
                current = current.next
            if current.key is key:
                prev.next = current.next
                current.remove()
                self.max -= 1
            return None if current.key is not key else current
        

    #eraseNode - erase the specific node, return removed node if it exist, else null
    def eraseNode(self, node):
        if self.head is None: 
            return None
        
        if self.head is node:
            old_head = self.head
            self.head = old_head.next
            old_head.remove()
            self.max -= 1
            return old_head
        else:
            current = self.head
            prev = None
            while current is not node and current.next is not None:
                prev = current
                current = current.next

            if current is node:
                prev.next = current.next
                current.remove()
                self.max -= 1
            return None if current is not node else current


    #isEmpty - return whether the list is empty
    def isEmpty(self):
        return True if self.head is None else False


def main():
    new_list = SingleLinkedList()

    new_list.pushFront(3)
    print(new_list.head.key, new_list.max)

    new_list.pushFront("A")
    print(new_list.head.key, new_list.max)

    new_list.popFront()
    print(new_list.head.key, new_list.max)
    
    new_list.addBefore(new_list.head, "AA")
    print(new_list.head.key, new_list.max)

    new_list.addAfter(new_list.head, "B")
    print(new_list.head.key, new_list.max)

    new_list.pushBack(10)
    print(new_list.head.key, new_list.max)

    last_node = new_list.topBack()
    print(None if last_node is None else last_node.key, last_node.next)

    popBack = new_list.popBack()
    print(popBack if popBack is None else popBack.key, new_list.max)    
    
    display_list(new_list)

    print(new_list.findKey(2))
    print(new_list.findKey("AA").key)

    print(new_list.eraseKey("AA").key)
    print(new_list.head.key, new_list.max)

    display_list(new_list)

    print(new_list.eraseNode(new_list.head).key)
    print(new_list.head.key, new_list.max)
    
    display_list(new_list)


def display_list(list):
    print("===== Beginning of List =====")
    if list.head is None:
        print("Empty List")
    current = list.head
    while current is not None:
        print(current.key, current.next.key if current.next is not None else None)
        current = current.next   
    print("=====    End of List    =====")


main()
// single linked list with no tail


class Node {
    constructor(key, next) {
        this.key = key;
        this.next = next;
    }
}

class List {
    constructor(head = null) {
        this.head = head
        this.max = 0
    }

    // add a node to front of the list, return list.max (length)
    pushFront(key) {
        let node = new Node(key, this.head)
        this.head = node
        this.max += 1
        return this.max
    }

    // return front item
    topFront() {
        return this.head
    }

    // remove front item, return old node
    popFront() {
        if(this.max_length < 1) return
        let oldHead = this.head
        this.head = oldHead.next
        oldHead.next = null
        this.max -= 1
        return oldHead   
    }
    // add a node after a specific node
    addAfter(node, key){
        if (node == null) return null
        
        let newNode = new Node(key, node.next)
        node.next = newNode
        this.max += 1
    }

    // add a node before a specific node
    addBefore(node, key) {
        if (node == null) return null

        let [current, prev] = [list.head, null]
        while(current != node && current.next) {
            prev = current
            current = current.next
        }
        if (current != node) {
            return null
        }
        else {
            let newNode = new Node(key, current)
            if (this.head == current) {
                this.head = newNode
            } 
            else {
                prev.next = newNode
            }
            this.max += 1
            return this.max
        }
    } 

    // add to back, return list.max (list length)
    pushBack(key) {
        let node = new Node(key, null)
        if(this.head == null) {
            this.head = node
            this.max += 1
        }
        else {
            let current = this.head
            while(current.next){
                current = current.next
            }
            current.next = node
            this.max += 1
        }            
        return this.max
    }

    // return back item
    topBack() {
        if(this.head == null) {
            return null
        }
        else {
            let current = this.head
            while(current.next) {
                current = current.next
            }
            return current
        }
    }

    // remove back item, return removed node
    popBack() {
        if(this.head == null) {
            return null
        }
        else {
            let [current, pre] = [this.head, null]
            while(current.next) {
                pre = current
                current = current.next
            }
            pre.next = null
            this.max -= 1
            return current
        }
    }

    // is key in list? return node if true, return null if not in list
    find(key) {
        if(this.head == null) {
            return null
        }
        else {
            let current = this.head
            while(current.key != key && current.next){
               current = current.next
            } 
            return current.key == key? current : null
        }
    }


    // remove key from list, return the removed node
    erase(key) {
        if (this.head == null) {
            return null
        }
        if (this.head.key == key) {
            let oldHead = this.head
            this.head = this.head.next
            oldHead.next = null
            this.max -= 1
            return oldHead
        }

        else {
            let [current, pre] = [list.head, null]
            while(current.key != key && current.next) {
                pre = current
                current = current.next

            }
            if (current.key == key) {
                // if the matching node is the head
                if (this.head == current) {
                    this.head = current.next
                    current.next = null
                }   
                else {
                    pre.next = current.next
                    current.next = null
                }
                this.max -= 1
                return current   
            }
            else {
                return null
            }
        }
    }

    // is list empty?
    empty() {
        return this.max == 0
    }
}


module.exports = {
    Node, 
    List
}

// export {
//     Node,
//     List
// }








// let elem = [1,2,3,4,5,6,7,8,9,10]
// let list = new List()

// for (let el of elem) {
//     list.pushBack(el)
// }

// list.pushFront(0)
// list.pushFront(-1) 
// list.addAfter(list.find(10), 11)
// list.addBefore(list.head, -3)
// console.log(list.topFront())
// list.pushFront(-2)
// list.pushBack(12)

// console.log(list.topFront())

// let node = list.head

// while(node) {
//     console.log(`Node Value: ${node.key}, Next Value: ${node.next? node.next.key : node.next}`)
//     node = node.next
// }

// console.log(list.popFront())
// console.log(list.head)
// console.log(list.topBack())
// console.log(list.popBack())
// console.log(list.topBack())
// console.log(list.max)
// console.log(list.erase(9))

// node = list.head
// while(node) {
//     console.log(`Node Value: ${node.key}, Next Value: ${node.next? node.next.key : node.next}`)
//     node = node.next
// }

// console.log(list.max)



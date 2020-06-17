// ↓↓↓ import does not work in node.js environment ↓↓↓
// import { List, Node } from '../../Single_Linked_List/single_linked_list.js';

// ↓↓↓ require with module.exports works ↓↓↓
// const Single = require('../../Single_Linked_List/single_linked_list.js')

const {List, Node} = require('../../Single_Linked_List/single_linked_list.js')


// reverse a single linked list with no tail
function reverse_linked_list(list) {
    if (list.head == null || list.head.next == null) return list
    let [current, prev, next] = [list.head, null, list.head.next]
    while(next) {
        current.next = prev
        prev = current
        current = next
        next = current.next
    }
    list.head = current
    current.next = prev
    return list
}



// ↓↓↓   basic testing   ↓↓↓

let elem = [1,2,3,4,5,6,7,8,9,10]
let short_elem = [1]
let empty_elem = []

let list = creating_list_from_array(elem)
display_list(list)
let rev_list = reverse_linked_list(list)
display_list(rev_list)


let list_short = creating_list_from_array(short_elem)
display_list(list_short)
let rev_list_short = reverse_linked_list(list_short)
display_list(rev_list_short)


let list_empty = creating_list_from_array(empty_elem)
display_list(list_empty)
let rev_list_empty = reverse_linked_list(list_empty)
display_list(rev_list_empty)



function creating_list_from_array(arr) {
    let list = new List()
    for (let el of arr) {
        list.pushBack(el)
    }
    return list
}

function display_list(list) {
    console.log('===== beginning of list =====')

    let current = list.head
    while(current) {
        console.log(`Node Value:  ${current.key}, Next Value: ${current.next? current.next.key : current.next}`)
        current = current.next
    }
    console.log('===== end of list =====')
    console.log('          ')
}





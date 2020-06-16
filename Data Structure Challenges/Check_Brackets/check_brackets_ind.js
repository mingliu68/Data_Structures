// 1. Check the string and see if there is mismatching brackets [], (), {}
   // Return index of first mismatching occurance (first closing bracket or first opening bracket)
   // Return "All Brackets Matching" if all brackets are matching
// 2. String can contain letters, digits, and punctuation marks
// 3. String can be empty, can have nested brackets 


function check_brackets_ind(str) {              // O(n) linear time complexity
    const brackets = ['{', '(', '[', '}', ')', ']'];

    // using a stack to keep track of opening brackets
    // each item will be an object tracking the index and type of opening bracket {index: 3, bracket: "["}
    const open = [];

   
    for(let i = 0; i < str.length; i++) {       // O(n) time complexity
        // check and see if str[i] is a bracket, return -1 if not
       
        let ind = brackets.indexOf(str[i])      // O(brackets.length) or O(6) constant time complexity
        
        // str[i] is not a bracket, skip the following steps and continue to next iteration
        if (ind == -1) continue;
        
        // if str[i] is an opening bracket, push to stack
        if (ind < 3 && ind >= 0) {
            open.push({index: i, bracket: str[i]})
        }
        
        // if str[i] is a closing bracket
        else {
            // if there is no matching opening bracket to match this closing bracket
            if(open.length == 0) {
                return i                    
            }

            // pop the last item (object) in stack, get the bracket value and comparing it with str[i]
            let last = open.pop().bracket
            if (last === "(" && str[i] != ")" || last === "{" && str[i] != "}" || last === "[" && str[i] != "]") {
                return i
            }
        }
    }

    return open.length == 0 ? "All Brackets Matching" : open[0].index;
}

let test_1 = '(()())';
let test_2 = '()()[]{}{()}';
let test_3 = 'f(a,b)-g[c]';
let test_4 = '1bsoiuj()(({}[]}}';
let test_5 = '(foo[bar])';

console.log(check_brackets_ind(test_1))
console.log(check_brackets_ind(test_2))
console.log(check_brackets_ind(test_3))
console.log(check_brackets_ind(test_4))
console.log(check_brackets_ind(test_5))
console.log(check_brackets_ind(""))
console.log(check_brackets_ind("abc"))
console.log(check_brackets_ind("abc["))
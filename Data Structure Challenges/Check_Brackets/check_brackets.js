// 1. Return false if there is mismatching brackets [], (), {}
   // Return true if all brackets are matching
// 2. String can contain letters, digits, and punctuation marks
// 3. String can be empty, can have nested brackets 

function check_brackets(str) {
    const brackets = ['{', '(', '[', '}', ')', ']'];

    // using a stack to keep track of opening brackets
    const open = [];

    // O(n)
    for (let char of str) {
        // check if char is one of the brackets, returns -1 if not - O(brackets.length) 
        let ind = brackets.indexOf(char);

        // if char is not one of the brackets
        if (ind == -1) continue;

        // if char is one of the open brackets, push to items
        if (ind >= 0 && ind < 3) {
           open.push(char)
        } 

        // if char is one of the closing brackets, follow the steps below
        else { 
            // return false if there is no open brackets left
            if (open.length == 0) {
                return false;
            }
            // pop the last item in items and comparing it with char
            let last = open.pop()
            if (char === '}' && last != '{' || char === ')' && last != '(' || char === ']' && last != '['){
                return false;
            }
        }
    }
    return open.length === 0;
}




let test_1 = '(()())';
let test_2 = '()()[]{}{()}';
let test_3 = 'f(a,b)-g[c]';
let test_4 = '1bsoiuj()(({}[]}}';
let test_5 = '(foo[bar])';

console.log(check_brackets(test_1))
console.log(check_brackets(test_2))
console.log(check_brackets(test_3))
console.log(check_brackets(test_4))
console.log(check_brackets(test_5))
console.log(check_brackets(""))
console.log(check_brackets("abc"))
console.log(check_brackets("["))
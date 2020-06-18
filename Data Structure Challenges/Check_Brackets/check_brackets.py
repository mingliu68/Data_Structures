# 1. Return False if there is mismatching brackets [], (), {}
   # Return True if all brackets are matching
# 2. String can contain letters, digits, and punctuation marks
# 3. String can be empty, can have nested brackets 

def check_brackets(str):
    brackets = "({[)}]"
    open_stack = []
    for char in str:
        index = brackets.find(char)
        if index == -1:
            continue
        if index < 3 and index >= 0:
            open_stack.append(char)
        else:
            if len(open_stack) == 0:
                return False
            last = open_stack.pop()
            if last == "(" and char != ")" or last == "{" and char != "}" or last == "[" and char != "]":
                return False
    
    return True if len(open_stack) == 0 else False


test_1 = '(()())';
test_2 = '()()[]{}{()}';
test_3 = 'f(a,b)-g[c]';
test_4 = '1bsoiuj()(({}[]}}';
test_5 = '(foo[bar])';

print(check_brackets(test_1))
print(check_brackets(test_2))
print(check_brackets(test_3))
print(check_brackets(test_4))
print(check_brackets(test_5))
print(check_brackets(""))
print(check_brackets("abc"))
print(check_brackets("abc["))
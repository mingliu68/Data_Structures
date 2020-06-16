# 1. Check the string and see if there is mismatching brackets [], (), {}
   # Return the index of first mismatching occurance (first closing bracket or first opening bracket if there is no closing brackets left)
   # Return "All Brackets Matching" if all brackets are matching
# 2. String can contain letters, digits, and punctuation marks
# 3. String can be empty, can have nested brackets 

def check_brackets_ind(str):
    brackets = "({[)}]"
    items = []
    for i, char in enumerate(str):
        index = brackets.find(char)
        if index == -1: 
            continue
        if index < 3 and index >= 0:
            items.append({"ind":i, "bracket": char})
        else:
            if len(items) == 0:
                return i
            last = items.pop()["bracket"]
            if last == "(" and char != ")" or last == "{" and char != "}" or last == "[" and char != "]":
                return i

    return "All Brackets Matching" if len(items) == 0 else items[0]["ind"] 






test_1 = '(()())';
test_2 = '()()[]{}{()}';
test_3 = 'f(a,b)-g[c]';
test_4 = '1bsoiuj()(({}[]}}';
test_5 = '(foo[bar])';

print(check_brackets_ind(test_1))
print(check_brackets_ind(test_2))
print(check_brackets_ind(test_3))
print(check_brackets_ind(test_4))
print(check_brackets_ind(test_5))
print(check_brackets_ind(""))
print(check_brackets_ind("abc"))
print(check_brackets_ind("abc["))
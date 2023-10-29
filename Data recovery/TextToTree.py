
word_list = ['apple', 'app', 'banana', 'banish', 'cat', 'car', 'dog', 'deer']

root = []
    
for word in word_list:
    node = root
    for char in word:
        found = False
        for child in node:
            if isinstance(child, list) and child[0] == char:
                node = child
                found = True
                break
        if not found:
            new_node = [char]
            node.append(new_node)
            node = new_node

def print_list(lst, level = -1):
    for l in lst:
        if type(l) is not list:
            print('    ' * (level - 1) + '|___' * (level > 0) + l)
        elif type(l) is list:
            print_list(l, level + 1)
        else:
            print('    ' * level + '+---' + l)

#print(root)
print_list(root)

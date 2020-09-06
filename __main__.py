from bs4 import BeautifulSoup, Tag
import hashlib

def nest_tags(names):
    current = Tag(name=names[0])
    root = current
    for i in range(1, len(names)):
        new_tag = Tag(name=names[i])
        current.append(new_tag)
        current = new_tag
    return root

def get_plaintext(known_values, test_value):
    attempt_values = known_values + [test_value]
    html = nest_tags(attempt_values)
    return str(html)

def get_hashtext(known_values, test_value):
    plaintext = get_plaintext(known_values, test_value)
    return hashlib.sha256(plaintext.encode('utf-8')).hexdigest()


print(get_hashtext([], 'H'))
print(get_hashtext(['H'], 'e'))
print(get_hashtext(['H', 'e'], 'l'))
print(get_hashtext(['H', 'e', 'l'], 'l'))
print(get_hashtext(['H', 'e', 'l', 'l'], 'o'))
print(get_hashtext(['H', 'e', 'l', 'l', 'o'], ' '))
print(get_hashtext(['H', 'e', 'l', 'l', 'o', ' '], 'w'))
print(get_hashtext(['H', 'e', 'l', 'l', 'o', ' ', 'w'], 'o'))
print(get_hashtext(['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o'], 'r'))
print(get_hashtext(['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r'], 'l'))
print(get_hashtext(['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l'], 'd'))
print(get_hashtext(['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'], '!'))
def to_number(word):
    num = 0
    for w in word:
        value = ord(w) - 64
        num += value
    return num


def detail(word):
    for w in word:
        value = ord(w) - 64
        yield str(value)


with open('words.txt') as f:
    for line in f:
        line = line.rstrip().upper()
        if to_number(line) == 100:
            print(line + ' = ' + '+'.join(detail(line)))

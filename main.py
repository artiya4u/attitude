def to_number(word):
    num = 0
    for w in word:
        value = ord(w)
        num += (value - 64)
    return num

with open('words.txt') as f:
    for line in f:
        line = line.rstrip().upper()
        if to_number(line) == 100:
            print(line)

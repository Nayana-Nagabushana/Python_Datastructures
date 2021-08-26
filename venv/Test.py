def rev_str(s):

    words=s.split()
    length = len(words) - 1
    rev_list = []
    while length >= 0:
        rev_list.append(words[length])
        length -= 1

    return " ".join(rev_list)

print(rev_str('my name is nayana'))


def sen_rev(sentence):
    words = sentence.split()
    length = len(words) - 1
    rev_list = []
    while length >= 0:
        rev_list.append(words[length])
        length -= 1
    return " ".join(rev_list)

print(sen_rev("my name is nayana"))
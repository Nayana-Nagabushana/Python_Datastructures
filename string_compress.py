def string_compress(string):
    r = ''
    length = len(string)
    if length == 0:
        return ''
    if length == 1:
        return string + "1"

    count = 1
    i = 1
    last = string[0]
    while i < length :
        if string[i] == string[i-1]:
            count += 1
        else:
            r = r + string[i-1] + str(count)
            count = 1
        i += 1
    return r+string[i-1]+str(count)

print(string_compress("AAAABBBCC"))
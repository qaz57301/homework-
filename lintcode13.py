def contain_word(source,target):
    if source == "" and target=="":
        return 0

    for i in target:
        if i in source:
            return source.index(i)
    return -1

print(contain_word('abcd','ef'))
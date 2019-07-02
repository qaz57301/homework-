"""
For a given source string and a target string, you should output the first index(from 0) of target string in source string.
If target does not exist in source, just return -1.
"""
def contain_word(source,target):
    if source == "" and target=="":
        return 0

    for i in target:
        if i in source:
            return source.index(i)
    return -1

print(contain_word('abcd','bc'))
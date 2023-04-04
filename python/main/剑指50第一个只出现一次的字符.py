def firstUniqChar(s: str) -> str:
    counter = dict()

    for ch in s:
        if ch not in counter.keys():
            counter[ch] = 1
        else:
            counter[ch] += 1

    for k in counter:
        if counter[k] == 1:
            return k

    return " "


print(firstUniqChar("lleetcode"))

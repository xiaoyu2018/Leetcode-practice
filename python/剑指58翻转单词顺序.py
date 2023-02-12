
def reverseWords(s: str) -> str:
    return " ".join(reversed([i for i in s.split(" ") if i not in [""," "]]))
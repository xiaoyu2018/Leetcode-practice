

def reverseWords(s: str) -> str:
    return " ".join(reversed([i.strip() for i in s.split(" ") if i]))



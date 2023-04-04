s="   fly me   to   the moon  "

def lenthOfLastWord(s:str):
    s=s.strip()
    return len(s.split(" ")[-1])

print(lenthOfLastWord(s))
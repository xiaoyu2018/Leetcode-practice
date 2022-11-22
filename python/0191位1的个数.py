
def hammingWeight(n: int) -> int:

    return bin(n).count("1")

def hammingWeight1(n: int) -> int:
    return sum([n&(1<<i)!=0 for i in range(len(bin(n))-2)])


print(0o010)
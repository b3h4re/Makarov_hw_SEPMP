def construct_prefix(string: str, prefix: list) -> None:
    for i in range(1, len(string)):
        j = prefix[i - 1]
        while j > 0 and string[i] != string[j]:
            j = prefix[j - 1]
        if string[i] == string[j]:
            prefix[i] = j + 1


def get_power(string: str) -> int:
    prefix = [0] * len(string)
    construct_prefix(string, prefix)
    k = len(string) - prefix[len(string) - 1]
    if len(string) % k:
        n = 1
    else:
        n = len(string) // k
    return n


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t+1):
        s = input()
        print(get_power(s))
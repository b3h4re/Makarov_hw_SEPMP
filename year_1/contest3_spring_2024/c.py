p = 27


def calculate_hash(arr: list, string: str) -> None:
    arr[0] = ord(string[0]) - 96
    for i in range(1, len(string)):
        arr[i] = (ord(string[i]) - ord('a') + 1) + arr[i - 1] * p


def get_string_from_hash(hash_value: int, length: int) -> str:
    res = ''
    mod = p ** (length - 1)
    while hash_value > 0:
        res += chr(hash_value // mod + ord('a') - 1)
        hash_value %= mod
        mod //= p
    return res


def find_password(length: int, string: str) -> str:
    mod = p ** (length - 1)
    hash_func = [0] * len(string)
    calculate_hash(hash_func, string)
    hashes = [hash_func[length - 1]]
    for i in range(len(string) - length):
        hashes.append(
            (hashes[-1] % mod) * p + (ord(string[i + length]) - ord('a') + 1)
        )
    hashes.sort()

    count = 1
    mx = 1
    freq_hash = hashes[0]
    for i in range(1, len(hashes)):
        if hashes[i] != hashes[i - 1]:
            count = 1
        else:
            count += 1
        if count > mx:
            freq_hash = hashes[i]
            mx = count

    return get_string_from_hash(freq_hash, length)


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t+1):
        n, s = (lambda x: (int(x[0]), x[1]))(input().split())
        print(find_password(n, s))

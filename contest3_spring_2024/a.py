def z_function(s: str, out: list):
    left, right = 0, 0
    for i in range(1, len(s)):
        out[i] = max(0, min(right - i, out[i - left]))
        while i + out[i] < len(s) and s[out[i]] == s[i + out[i]]:
            out[i] += 1
        if i + out[i] > right:
            left = i
            right = i + out[i]


def process_test(n, string):
    s = string + ''.join(list(reversed(string)))
    z = [0] * len(s)
    z_function(s, z)
    for i in range(1, len(string)+1):
        yield z[-i]


if __name__ == "__main__":
    for elem in process_test(int(input()), input()):
        print(elem, end=' ')
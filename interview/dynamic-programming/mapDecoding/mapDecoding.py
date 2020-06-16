# Bottom-up approach
def mapDecoding(message):
    arr = [0] * (len(message) + 1)
    arr[-1] = 1
    for i in reversed(range(len(message))):
        if message[i] == '0':
            arr[i] = 0
            continue
        x = arr[i + 1]
        y = 0
        if i <= len(message) - 2:
            num = int(message[i] + message[i + 1])
            if num <= 26:
                y = arr[i + 2]
        arr[i] = x + y
    return arr[0] % (10 ** 9 + 7)


# Top-down approach
def mapDecoding(message):
    return helper(message, 0, {}) % (10 ** 9 + 7)

def helper(message, idx, cache):
    if idx in cache:
        return cache[idx]
    if idx >= len(message):
        return 1
    if message[idx] == '0':
        return 0
    x = helper(message, idx + 1, cache)
    y = 0
    if idx <= len(message) - 2:
        num = int(message[idx] + message[idx + 1])
        if num <= 26:
            y = helper(message, idx + 2, cache)
    cache[idx] = x + y
    return x + y
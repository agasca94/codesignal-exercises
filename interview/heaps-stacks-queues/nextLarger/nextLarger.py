def nextLarger(a):
    stack = []
    final_arr = []

    for i in range(len(a)):
        final_arr.append(-1)

        while stack and a[stack[-1]] < a[i]:
            final_arr[stack.pop()] = a[i]

        stack.append(i)

    return final_arr
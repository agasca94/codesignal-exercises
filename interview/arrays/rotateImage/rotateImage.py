def rotateImage(a):
    n = len(a)
    beginning = 0
    
    while n > 1:
        start = beginning
        end = start + n - 1

        for i in range(end - start):
            top = a[start][start + i]
            right = a[start + i][end]
            bottom = a[end][end - i]
            left = a[end - i][start]
            
            # Rotate elements clockwise
            a[start + i][end] = top # Top to right
            a[end][end - i] = right # Right to bottom
            a[end - i][start] = bottom # Bottom to left
            a[start][start + i] = left # Left to top

        n -= 2
        beginning += 1
            
    return a
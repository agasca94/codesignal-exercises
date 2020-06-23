def findProfession(level, pos):
    professions = ['Engineer', 'Doctor']
    current = 0
    n_nodes = 2 ** (level - 1)
    for x in range(level - 1):
        mid = n_nodes // 2

        if pos <= mid:
            # Move to left
            n_nodes = mid
        else:
            # Move to right
            n_nodes = mid
            pos -= mid
            current = not current
    
    return professions[current]
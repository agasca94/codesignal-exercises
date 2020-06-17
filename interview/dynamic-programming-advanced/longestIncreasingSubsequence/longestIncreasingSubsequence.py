def longestIncreasingSubsequence(seq):
    mat = [0 for i in range(len(seq))]
    m = 0
    for c in reversed(range(len(seq))):
        for p in range(c + 1):
            sol = max(mat[c] + 1, mat[p]) if seq[c] > seq[p] else mat[p]
            mat[p] = sol
            if sol > m:
                m = sol
    return m + 1
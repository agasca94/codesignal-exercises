def climbingStairs(n):
    return helper(n, {})

def helper(n, cache):
    if n in cache:
        return cache[n]
    if n <= 1:
        return 1
    sol = helper(n  - 1, cache) + helper(n - 2, cache)
    cache[n] = sol
    
    return sol
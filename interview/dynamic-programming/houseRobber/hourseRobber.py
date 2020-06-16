def houseRobber(nums):
    return helper(nums, -2, {})

def helper(nums, idx, cache):
    if idx in cache:
        return cache[idx]

    if idx >= len(nums):
        return 0

    x = helper(nums, idx + 2, cache)
    y = helper(nums, idx + 3, cache)

    sol = max(x, y) + (nums[idx] if idx >= 0 else 0)
    cache[idx] = sol

    return sol
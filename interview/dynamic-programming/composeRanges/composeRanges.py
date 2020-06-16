def composeRanges(nums):
    ranges = []
    if nums:
        first = prev = nums[0]
        for i in range(1, len(nums) + 1):
            num = nums[i] if i < len(nums) else prev
            if num - prev == 1:
                prev = num
                continue
            
            range_summary = str(first) if first == prev else f"{first}->{prev}"
            ranges.append(range_summary)
            
            first = prev = num
    return ranges
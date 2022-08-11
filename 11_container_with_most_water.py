height = [1, 3, 2, 5, 25, 24, 5]


def maxArea(height):
    res = 0
    l, r = 0, len(height) - 1
    while l < r:
        res = max(res, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res


print(maxArea(height))

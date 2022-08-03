nums = [100, 4, 200, 201, 202, 203, 204, 1, 3, 2]

numsSet = set(nums)
longest = 0

for num in nums:
    if num - 1 not in numsSet:
        length = 1
        while num + 1 in numsSet:
            num = num + 1
            length = length + 1
        longest = max(longest, length)
        if longest > (len(nums) / 2):
            break
print(longest)

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         hashMap = {}
#         for i, n in enumerate(numbers):
#             if (target - n) in hashMap:
#                 return [hashMap[target - n] + 1, i + 1]
#             hashMap[n] = i


numbers = [2, 7, 11, 15]
target = 9

l, r = 0, len(numbers) - 1
while l < r:
    sum = numbers[l] + numbers[r]
    if sum > target:
        r -= 1
    elif sum < target:
        l += 1
    else:
        print([l + 1, r + 1])

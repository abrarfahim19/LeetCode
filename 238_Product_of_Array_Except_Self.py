def productExceptSelf(self, nums: List[int]) -> List[int]:
    output = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        output[i] = prefix
        prefix = prefix * nums[i]

    postfix = 1
    for j in range(len(nums),0,-1):
        output[j-1] = output[j-1] * postfix
        postfix = postfix * nums[j-1]
    return output
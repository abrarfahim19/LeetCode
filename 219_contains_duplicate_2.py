def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    prevMap = {}  # initiate the HashTable

    for i, n in enumerate(nums):  # Use i,n because position and value both is involved
        if nums[i] in prevMap:  # if the nums were seen before
            if k >= abs(i - prevMap[n]):  # if the nums are in close proximity
                return True
        prevMap[n] = i  # previous seen discarded with new one
    return False

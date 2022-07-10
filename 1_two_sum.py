def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashTable = {}  # Initiate the hash table
    for i, n in enumerate(nums):
        diff = target - n
        if diff in hashTable:
            return [hashTable[diff], i]
        hashTable[n] = i
    return

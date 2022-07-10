def containsDuplicate(self, nums: List[int]) -> bool:
    hashTable = set()
    for each in nums:
        if each in hashTable:
            return True
        hashTable.add(each)
    return False

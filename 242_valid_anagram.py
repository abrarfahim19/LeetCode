def isAnagram(self, s: str, t: str) -> bool:
    tTable = {}
    sTable = {}

    for each1 in t:
        if each1 in tTable:
            tTable[each1] = tTable[each1] + 1
        else:
            tTable[each1] = 1

    for each2 in s:
        if each2 in sTable:
            sTable[each2] = sTable[each2] + 1
        else:
            sTable[each2] = 1

    if sTable == tTable:
        return True
    return False

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups ={}
        for s in strs:
            key = "".join(sorted(s))

            groups[key] = groups.get(key,[])+[s]

        return list(groups.values())

            

        
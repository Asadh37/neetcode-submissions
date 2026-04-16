class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d_ana = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in d_ana:
                d_ana[key] = []

            d_ana[key].append(word)

        return list(d_ana.values())
        
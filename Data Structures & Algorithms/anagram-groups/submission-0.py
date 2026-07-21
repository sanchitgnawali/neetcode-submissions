class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            # create a frequency counter
            count = [0] * 26
            # loop thorugh each character and increment frequency counter
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # add count as key and word as value
            result[tuple(count)].append(s)
        
        # return grouped list
        return list(result.values())
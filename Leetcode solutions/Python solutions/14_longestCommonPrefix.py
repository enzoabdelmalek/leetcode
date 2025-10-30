class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        preflen = len(prefix)
        while len(prefix) > -1 :
            for i in strs[1:] :
                while prefix != i[0:preflen] :
                    preflen -= 1
                    prefix = prefix[:-1]
            if prefix == [] :
                prefix = ""
            return prefix
        
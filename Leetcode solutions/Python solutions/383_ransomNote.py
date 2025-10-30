class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        magazine = list(magazine)
        target = []
        for i in range(len(ransomNote)) :
            for j in range(len(magazine)) :
                if ransomNote[i] == magazine[j] :
                    target.append(magazine[j])
                    magazine.pop(j)
                    break
                else :
                    continue
        if ransomNote == target :
            return True
        else :
            return False
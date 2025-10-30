class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        output = ''
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i>=0 or j>= 0 or carry :
            valA = int(a[i]) if i >= 0 else 0
            valB = int(b[j]) if j >= 0 else 0

            total = valA + valB + carry
            result += str(total%2)
            carry = total // 2
            i-=1
            j-=1
        k = len(result)-1
        while k>=0 :
            output += str(result[k])
            k-=1

        return output
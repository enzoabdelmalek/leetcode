class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        # Inverser les chiffres
        reversed_x = int(str(x)[::-1]) * sign
        
        # Vérifier les limites de 32 bits
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
        
        return reversed_x
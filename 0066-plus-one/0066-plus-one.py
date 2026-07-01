class Solution:
    def plusOne(self, digits):
        n = len(digits)
        # last se start karte hain
        for i in range(n - 1, -1, -1):
            digits[i] += 1          # current digit me 1 add
            digits[i] %= 10         # 10 hua toh 0 + carry
            if digits[i] != 0:      # agar 0 nahi, carry khatam
                return digits       # yahi final answer
        
        # yahan tak aaye matlab sab 9 the, ab [1] + zeros
        return [1] + digits
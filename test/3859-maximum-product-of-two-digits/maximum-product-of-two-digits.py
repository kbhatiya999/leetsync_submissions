class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]  # Convert number to list of digits
        max_product = 0

        # Try all pairs of digits (including same index)
        for i in range(len(digits)):
            for j in range(len(digits)):
                if i != j:
                    product = digits[i] * digits[j]
                    max_product = max(max_product, product)

        return max_product

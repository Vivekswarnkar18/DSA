class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1

        while n > 0:

            # If n is odd, one extra x is left after dividing by 2,
            # so include it in the answer.
            if n % 2 == 1:
                ans *= x

            # Square the base for the next power
            x *= x

            # Reduce the exponent by half
            n //= 2

        return ans
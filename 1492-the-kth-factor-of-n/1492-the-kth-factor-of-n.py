class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = set([])
        for i in range(1, int(sqrt(n+1))+1):
            if n % i == 0:
                factors.add(i)
                factors.add(n//i)
        factors = sorted(list(factors))
        return factors[k-1] if k-1 < len(factors) else -1
class Solution(object):
    def countPrimes_sol_1(self, n):
        count = 0
        primes = [False for i in range(n + 1)]
        for i in range(2, n):
            if primes[i] == False:
                count += 1
                j = 2
                while j * i < n:
                    primes[j * i] = True
                    j += 1
        return count

    def countPrimes_sol_2(self, n):
        count = 0
        for num in range(n):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes_sol_1(10))
    print(s.countPrimes_sol_2(10))
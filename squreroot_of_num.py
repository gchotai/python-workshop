class Solution(object):
    # 'solution - 1'
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = x
        while not abs(result * result - x) < 1:
            result = (result + x / result) / 2

        return int(result)

    # 'solution - 2'
    def sqrt(num):
        sqrt = num / 2
        temp = 0
        while(sqrt!=temp):
            temp = sqrt
            sqrt = (num / temp + temp) / 2
        return sqrt

if __name__ == '__main__':
    s = Solution()
    print(s.mySqrt(9))
    print(s.sqrt(9))


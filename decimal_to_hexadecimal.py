class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        num = num if num >= 0 else 0xffffffff + num + 1
        b = bin(num)[2:]
        b = b.zfill(((len(b) - 1) // 4 + 1) * 4)
        dc = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
              '1000': '8', '1001': '9', '1010': 'a', '1011': 'b', '1100': 'c', '1101': 'd', '1110': 'e', '1111': 'f'}
        ret = ''
        for i in range(0, len(b), 4):
            ret += dc[b[i:i + 4]]
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.toHex(15))

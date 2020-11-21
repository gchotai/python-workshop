from collections import Counter
class soluction:
    # 'solution - 1'
    def top_k_frequency(self, nums, k):
        cnt = Counter(nums)
        most_common_k = cnt.most_common(k)
        res = [num[0] for num in most_common_k]
        return res

    # 'solution - 2'
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num in counts.keys():
            buckets[counts[num]].append(num)
        ans = []
        for i in range(len(nums), 0, -1):
            ans += buckets[i]
            if len(ans) == k:
                return ans
        return ans


if __name__ == '__main__':
    s = soluction()
    print(s.top_k_frequency([1,1,2,2,2,4],2))
    print(s.topKFrequent([1, 1, 2, 2, 2, 4], 2))





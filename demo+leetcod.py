class Solution:
    def containsDuplicate(self, nums) -> bool:
        if len(nums) == 0:
            return False
        mapping = {}
        for num in nums:
            # 创建了hashmap{1:1, 5:1, 3:1, 4:1}
            if num not in mapping:
                mapping[num] = 1
            else:
                # 获得该索引的value值
                mapping[num] = mapping.get(num) + 1
        for v in mapping.values():
            if v > 1:
                return True
        return False

# nums = [1, 5, 3, 4]
nums = [2, 3, 2, 5, 2, 7]
sol = Solution()
sol.containsDuplicate(nums)
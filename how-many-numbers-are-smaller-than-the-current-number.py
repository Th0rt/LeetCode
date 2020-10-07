# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

import unittest
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        temp = sorted(nums)
        mapping = {}
        for i in range(length):
            if temp[i] not in mapping:
                mapping[temp[i]] = i
        return [mapping[nums[i]] for i in range(length)]


class TestSolution(unittest.TestCase):
    def test_1(self):
        nums = [8, 1, 2, 2, 3]
        expect = [4, 0, 1, 1, 3]
        assert Solution().smallerNumbersThanCurrent(nums) == expect

    def test_2(self):
        nums = [6, 5, 4, 8]
        expect = [2, 1, 0, 3]
        assert Solution().smallerNumbersThanCurrent(nums) == expect

    def test_3(self):
        nums = [7, 7, 7, 7]
        expect = [0, 0, 0, 0]
        assert Solution().smallerNumbersThanCurrent(nums) == expect


if __name__ == "__main__":
    unittest.main()

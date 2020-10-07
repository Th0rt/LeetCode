# https://leetcode.com/problems/shuffle-string/

import unittest
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ["x"] * len(indices)
        for char, i in zip(s, indices):
            res[i] = char
        return "".join(res)


class TestSolution(unittest.TestCase):
    def test_1(self):
        s = "codeleet"
        indices = [4, 5, 6, 7, 0, 2, 1, 3]
        expect = "leetcode"
        assert Solution().restoreString(s, indices) == expect

    def test_2(self):
        s = "abc"
        indices = [0, 1, 2]
        expect = "abc"
        assert Solution().restoreString(s, indices) == expect

    def test_3(self):
        s = "aiohn"
        indices = [3, 1, 4, 2, 0]
        expect = "nihao"
        assert Solution().restoreString(s, indices) == expect

    def test_4(self):
        s = "aaiougrt"
        indices = [4, 0, 2, 6, 7, 3, 1, 5]
        expect = "arigatou"
        assert Solution().restoreString(s, indices) == expect

    def test_5(self):
        s = "art"
        indices = [1, 0, 2]
        expect = "rat"
        assert Solution().restoreString(s, indices) == expect


if __name__ == "__main__":
    unittest.main()

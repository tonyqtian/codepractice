# -*- encoding: utf-8 -*-

"""
@version: 0.01
@author: Tony Qiu
@contact: tony.qiu@liulishuo.com
@file: lock_patterns.py
@time: 2018/04/16 午後0:58
"""


class Solution:
    """
    @param m: an integer
    @param n: an integer
    @return: the total number of unlock patterns of the Android lock screen
    """

    def __init__(self):
        self.patterns = {}

    def numberOfPatterns(self, m, n):
        # Write your code here
        total_count = 0
        for idx in xrange(m,n+1):
            total_count += len(self.total_lock_pattern(idx))
        return total_count

    def total_lock_pattern(self, n):
        if n == 1:
            total_current_patterns = [[1, ], [2, ], [3, ], [4, ], [5, ], [6, ], [7, ], [8, ], [9, ]]
            return total_current_patterns
        elif n - 1 in self.patterns:
            total_pre_patterns = self.patterns[n - 1]
        elif n - 1 == 1:
            total_pre_patterns = [[1, ], [2, ], [3, ], [4, ], [5, ], [6, ], [7, ], [8, ], [9, ]]
        else:
            total_pre_patterns = self.total_lock_pattern(n - 1)

        total_current_patterns = []
        try:
            for ptn in total_pre_patterns:
                total_current_patterns += self.get_valid_pattern(ptn)
        except TypeError:
            print("Error")
            print(total_pre_patterns)
            raise

        self.patterns[n] = total_current_patterns
        return total_current_patterns

    def get_valid_pattern(self, ptn):
        valid_patterns = []
        for idx in xrange(1, 10):
            if idx not in ptn:
                if self.check_valid(ptn, idx):
                    valid_patterns.append(ptn + [idx,])
        return valid_patterns

    def check_valid(self, ptn, idx):
        path = self.get_walk_path(ptn[-1], idx)
        for ptn_idx in path:
            if not ptn_idx in ptn:
                return False
        return True

    def get_walk_path(self, start, end):
        if start == end:
            raise Exception("Undefind pattern {0} {1}".format(start, end))

        elif start in [5, ]:
            return []

        elif start in [1, 3, 7, 9]:
            if end in [2, 4, 5, 6, 8]:
                return []
            elif end in [1, 3, 7, 9]:
                if sorted([start, end]) == [1, 3]:
                    return [2, ]
                if sorted([start, end]) == [1, 7]:
                    return [4, ]
                if sorted([start, end]) == [3, 9]:
                    return [6, ]
                if sorted([start, end]) == [7, 9]:
                    return [8, ]
                if sorted([start, end]) in [[1, 9], [3, 7]]:
                    return [5, ]
            else:
                raise Exception("Undefind pattern {0} {1}".format(start, end))

        elif start in [2, 4, 6, 8]:
            if end in [1, 3, 5, 7, 9]:
                return []
            elif end in [2, 4, 6, 8]:
                if sorted([start, end]) in [[2, 4], [2, 6], [4, 8], [6, 8]]:
                    return []
                if sorted([start, end]) in [[2, 8], [4, 6]]:
                    return [5, ]
            else:
                raise Exception("Undefind pattern {0} {1}".format(start, end))

        else:
            raise Exception("Undefind pattern {0} {1}".format(start, end))


if __name__ == '__main__':
    mylock = Solution()
    print(mylock.numberOfPatterns(7, 9))
